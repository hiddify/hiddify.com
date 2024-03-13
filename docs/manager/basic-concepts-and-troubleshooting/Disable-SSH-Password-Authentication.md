
## Disable SSH Password Authentication
Disabling SSH password authentication is a good practice for enhancing security, especially on a public-facing server. Here is a step-by-step tutorial on how to disable SSH password authentication. This guide assumes you are using a Linux-based system.

### Step 1: Ensure You Have Key-Based Authentication Set Up
Before you disable password authentication, make sure you have key-based authentication configured and working. If you disable password authentication without having an alternative way to log in, you could lock yourself out of the server.

1. **Generate an SSH Key Pair** (if you haven't already):
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
   Press Enter to accept the default file location. Optionally, you can set a passphrase for additional security.

2. **Copy the Public Key to Your Server**:

- Windows:
   ```bash
   cat $HOME\.ssh\id_rsa.pub | ssh username@your_server_ip 'cat >> ~/.ssh/authorized_keys'
   ```

- Linux & Mac:
   ```bash
   ssh-copy-id username@your_server_ip
   ```

   Replace `username` with your actual username and `your_server_ip` with your server's IP address.

3. **Test Key-Based Login**: Try to log in using your SSH key.
   ```bash
   ssh username@your_server_ip
   ```
   If you can log in without being prompted for a password, key-based authentication is working.

# Warning! If the last step has error, do not start Step 2
### Step 2: Edit the SSH Configuration File

1. **Access the SSH Configuration File**:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```
   You can replace `nano` with your preferred text editor (like `vi` or `vim`).

2. **Find the Line for Password Authentication**: Look for a line that says `PasswordAuthentication`. It might be commented out (starting with `#`).

3. **Disable Password Authentication**: Change this line to
   ```bash
   PasswordAuthentication no
   ```
   If the line is not there, you can add it at the end of the file.

4. **Save and Exit the Editor**: If you are using `nano`, you can save by pressing `Ctrl + O` and exit by pressing `Ctrl + X`.

### Step 3: Restart the SSH Service

After making changes to the `sshd_config` file, you need to restart the SSH service for the changes to take effect.

```bash
sudo systemctl restart sshd
```

### Step 4: Test the Configuration

1. **Test SSH Access**: Try to log in via SSH again. This time, the server should not allow password authentication.
   ```bash
   ssh username@your_server_ip
   ```
   Ensure that you can still log in using key-based authentication.

2. **Optional - Test from Another Machine**: If possible, try to SSH from a different machine where your SSH key is not configured. The server should not allow you to log in using a password.

### Step 5: Additional Security Measures

- Consider changing the SSH port from the default (port 22) to a non-standard port to reduce the chance of automated attacks. [read more ...](https://github.com/hiddify/Hiddify-Manager/wiki/How-to-change-SSH-port-on-your-server)
- Regularly update your server and SSH software.
- Set up a firewall and limit access to necessary ports only. [read more ...](https://github.com/hiddify/Hiddify-Manager/wiki/How-to-setup-Firewall-on-Hiddify-panel)
- Monitor login attempts and set up intrusion detection systems.

By following these steps, you should have successfully disabled SSH password authentication, enhancing the security of your server. Just ensure you have a backup method (like key-based authentication) set up to avoid being locked out.