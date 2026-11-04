# SSH: inbound and Hiddify additions

[All Hiddify features](../../index.md)

Upstream sing-box can only connect to an SSH server. Hiddify adds an SSH server (inbound,
`"type": "ssh"` in the `inbounds` list), UDP for the SSH outbound through UDP over TCP, and a
background connection that keeps the outbound ready. The rest of the SSH outbound works as in
upstream sing-box and is documented there. This page covers only the Hiddify parts.

## Why use it

- You want a server that any SSH client can use as a proxy, with port forwarding
  (`ssh -L`) or as a SOCKS proxy (`ssh -D`), without giving users a shell on the machine.
- You want UDP (for example DNS, QUIC or voice calls) through an SSH outbound. Plain SSH carries
  only TCP.
- You want the SSH outbound connected, tested and shown as ready before the first connection
  goes through it.

## How it gets past filtering

SSH is a common protocol for managing servers, and many networks leave it open. The traffic is
encrypted, so a filter cannot see the sites you open.

It does not hide that the traffic is SSH. A filter can see the SSH handshake, and some networks
slow down or block long or busy SSH sessions. Use it where SSH is allowed.

## How it works

### Inbound

- The server listens on TCP and runs the SSH handshake with its `host_key`.
- A user logs in with a password or a public key from `users`. Both checks look up the user by
  name.
- The server accepts only port forwarding requests (`direct-tcpip` channels). Requests for a
  shell, a command or a subsystem are rejected. A forward request the server cannot read is
  refused alone; the SSH connection and its other forwards go on.
- Each forwarded connection is routed like a connection from any other inbound. The user name is
  set, so stats and `auth_user` route rules work. Read and write deadlines work on forwarded
  connections.
- A forwarded connection to the UDP over TCP address of sing-box carries UDP. So a Hiddify SSH
  outbound with `udp_over_tcp` can send UDP through this server. When `network` does not list
  `udp`, this is turned off.

### Outbound: UDP over TCP

With `udp_over_tcp` turned on, the outbound sends each UDP session inside a forwarded TCP
connection, in the sing-box UDP over TCP format. The server must understand this format: the
Hiddify SSH inbound does, a normal OpenSSH server does not.

Without `udp_over_tcp`, the outbound does not accept UDP, even when `network` lists `udp`.
Route UDP to another outbound.

### Outbound: background connection

- After start, the outbound connects to the server in the background, without waiting for
  traffic. When the session drops, it connects again, waiting 1 second after a failure, then
  twice as long after each new failure, up to 1 minute.
- When it connects, the outbound is tested at once by [monitoring](../groups/monitoring.md).
- While it is not connected, the app shows it as connecting, and the last connection error as
  the proxy's error (not in its type). Monitoring skips the outbound until it is connected.
- When the app does not ask to keep idle connections, the session closes after its last
  connection ends, and it is not opened again until the next connection.

## Configuration

### Inbound

```json
{
  "inbounds": [
    {
      "type": "ssh",
      "tag": "ssh-in",
      "listen": "::",
      "listen_port": 2222,
      "host_key": [
        "-----BEGIN OPENSSH PRIVATE KEY-----\n...\n-----END OPENSSH PRIVATE KEY-----"
      ],
      "users": [
        { "user": "alice", "password": "<password>" },
        { "user": "bob", "public_key": "ssh-ed25519 AAAA... bob@laptop" }
      ]
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `host_key` | list of strings | required | Private keys of the server, in PEM or OpenSSH format. A server without a host key cannot complete a handshake. |
| `users` | list of objects | none | Users who can log in. |
| `users[].user` | string | none | User name. |
| `users[].password` | string | none | Password. Leave it empty to turn off password login for this user. |
| `users[].public_key` | string | none | One public key, as a line of an `authorized_keys` file. Leave it empty to turn off key login for this user. |
| `server_version` | string | Go SSH default | The version string the server sends, such as `SSH-2.0-OpenSSH_9.6`. Without the `SSH-2.0-` prefix, it is added. |
| `host_key_algorithms` | list of strings | all | Host key algorithms the server offers. An RSA key signs only with the listed `rsa-sha2-512`, `rsa-sha2-256` or `ssh-rsa`. Another key is used only when its type is listed, such as `ssh-ed25519`. If no host key is left, the config fails to load. |
| `network` | `"tcp"` or `"udp"` | both | Without `udp`, the server does not carry UDP over TCP. The server always listens on TCP. |

The usual listen fields (`listen`, `listen_port` and the rest) work as for other inbounds.

### Outbound

```json
{
  "outbounds": [
    {
      "type": "ssh",
      "tag": "ssh-out",
      "server": "203.0.113.10",
      "server_port": 2222,
      "user": "alice",
      "password": "<password>",
      "udp_over_tcp": true
    }
  ]
}
```

| Field | Type | Default | Meaning |
|---|---|---|---|
| `udp_over_tcp` | bool or object | off | Send UDP inside forwarded TCP connections. `true` uses version 2. The object form is `{"enabled": true, "version": 1}` or `2`. |
| `network` | `"tcp"` or `"udp"` | both | Networks the outbound accepts. Upstream accepts only TCP. UDP is accepted only when `udp_over_tcp` is on. |

## See also

- [Monitoring](../groups/monitoring.md)
- [PROXY protocol](../proxy-protocol.md)
