# Getting a PandA on the network

The SD card inside a PandA contains a config.txt file that allows control of networking and other configuration settings

```
# This file contains configuration settings.  In this file network and other
# settings can be adjusted.

# If ADDRESS and NETMASK are not both specified DHCP will be used instead.
# The ADDRESS field can be set to a four part dotted IP address followed by a
# network mask specification thus:
#
#   ADDRESS = 172.23.252.202
#   NETMASK = 255.255.240.0

# If the ADDRESS field has been set then the GATEWAY and DNS fields should be
# set:
#
#   GATEWAY = 172.23.240.254
#   DNS = 172.23.5.13 172.23.4.1 130.246.8.13

# Optionally the DNS search domain can be set:
#
#   DNS_SEARCH = diamond.ac.uk

# The NTP server or servers can be specified here:
#
#   NTP = 172.23.240.2 172.23.199.1

# The machine hostname can be specified here:
#
#   HOSTNAME = panda

# To skip loading any zpackages at startup, either for testing or as an
# override to recover from a faulty zpkg install:
#
#   NO_ZPKG
```
During startup the network will be configured as follows:

- If `ADDRESS` and `NETMASK` are set then a static IP will be assigned, and the remaining keys should also be set. Additionally, `NTP` can be set to specify a list of `NTP` servers.
- Otherwise `DHCP` will be attempted. If successful this will assign the `IP` address, gateway and `DNS` settings, and may assign hostname. If the `DHCP` server provides the `NTP` option, it will be used to set the `NTP` servers. This will take priority over the `NTP` parameter.
- If DCHP fails then “ZeroConf” is attempted. If this also fails then PandA will not be reachable on the network.

Note that in the default configuration PandA will attempt to contact NTP servers at `0.pool.ntp.org` etc.

```{toctree}
:maxdepth: 1
:glob:

tutorials/*
```
