# How to Use WARP on HiddifyApp
WARP is a service based on WireGuard provided by Cloudflare. By using this protocol, you can bypass the filtering system through creating a proxy. The HiddifyApp also supports this protocol. Below are the instructions for setting up and using this protocol.

## WARP Parameters
In the HiddifyApp, various parameters can be set, which are explained in order below.

### Different Modes:
There are 6 main modes and 2 advanced modes that create a header (noise) for WARP to help bypass filtering.

- m1: In this mode, the header is created randomly.
- m2: In this mode, the header is created randomly and remains unchanged, with no traces of WireGuard and WARP in the header.
- m3: In this mode, the QUIC protocol is used to create the header.
- m4: This mode uses QUIC and is unchangeable, with no traces of WireGuard and WARP in the header.
- m5: This mode uses LQUIC.
- m6: This mode uses LQUIC and remains unchanged, with no traces of WireGuard and WARP in the header.
- gHEX: This advanced mode uses a HEX number for the WARP header to create noise.
- hHEX: This advanced mode also uses a HEX number for the WARP header but remains unchanged, with no traces of WireGuard and WARP in the header.

These headers are defined with the IFPM parameter in WARP. For example: `ifpm=m4` or `ifpm=h04ad5d` or `ifpm=g04ad5d`

!!! tip "Tip"
     The recommended mode is `m4`.

### Number, Size, and Delay of Noise Packets
These parameters are as follows:

- Number of noise packets: The number of noise packets can be defined in WARP using `ifp`, which is defined as a range, and each time a random number within this range is selected. For example: `ifp=40-80` means between 40 to 80 noise packets are created randomly.
- Size of noise packets: The size of the packets can be defined with the `ifps` parameter, which is also defined as a range, and each time a random size within this range is selected. For example: `ifps=40-100` means each time a noise packet with a random size between 40 to 100 bits is created.
- Delay in sending noise packets: The delay is defined using the `ifpd` parameter, which is also defined as a range, and each time the packets are sent with a random delay within this range. For example: `ifpd=4-8` means the packets are sent with a random delay between 4 to 8 seconds. Obviously, the smaller this range, the better.

### IP Settings
IP configuration settings are done in several ways:

- auto4: An automatic IPv4 is assigned to the config by Cloudflare.
- auto6: An automatic IPv6 is assigned to the config by Cloudflare.
- auto: Both IPv4 and IPv6 ranges are assigned to the config by Cloudflare.
- Clean IPv4: IPv4 can be directly entered into the config. For example: `188.114.97.170`
- Clean IPv6: IPv6 must be entered into the config using `[]`. For example: `[2a01:4ef:f0:10a5::1]`

!!! tip "Tip"
     To find clean IPs, various scanners can be used. For example, these scanners: [1](https://github.com/MortezaBashsiz/CFScanner), [2](https://github.com/azavaxhuman/Quick_WARP_on_WARP), [3](https://github.com/Ptechgithub/WARP)

### Display Name for Config:
To create a display name or remark the config, a `#` can be used at the end of the config followed by the desired name. The name should be a single piece. For example:

`warp://auto#NAME`

### WARP in WARP
With this feature, you can use two different WARPs and place one at the end of the other. In this way, you first connect to the first WARP, then connect to the second WARP from there, and the final IP becomes the IP of the second WARP. To use this feature, the `detour` parameter should be used, and it should be added at the end of the first WARP with `&&`, followed by the second WARP. For example:

`warp://auto&&detour=WARP://auto`

### General Formula for WARP Config:
The WARP config can be built using this formula. In this case, a fixed config is imported into the software.

`warp://License@IP:port?ifp=s1-s2&ifpd=d1-d2&ifpm=mode`

Example:

`warp://auto?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m4#m4`

In this case, a WARP config with the display name `m4` is imported into the software.

You can also detour two WARPs. For example:
`warp://auto?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m4#m4&&detour=WARP://188.114.97.170:894?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m3#m3`

In this case, a config with the name `m4` and a detoured config for WARP in WARP (WoW) with the name `m3` is created in the software.

Finally, it is recommended to check out sample WARP configs from [here](https://raw.githubusercontent.com/hiddify/hiddify-next/main/test.configs/WARP) and [here](https://raw.githubusercontent.com/hiddify/hiddify-next/main/test.configs/WARP2).

!!! tip "Final Tip"
    - To achieve a suitable configuration, use the above scanners to find a clean IP suitable for your network and then build the Warp configuration according to the formula.
    - Also, adjust the range of parameters to achieve the desired result.
