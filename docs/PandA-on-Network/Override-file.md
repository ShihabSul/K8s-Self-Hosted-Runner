# Override file

If a static IP address needs to be set this can be configured after installation
via the following override mechanism.

If a USB drive is plugged into PandA while it is booting, and if the drive
contains this file: 

``panda-config.txt``

then this file will be used for network configuration instead of ``config.txt``
on the SD card.

This override file can be made permanent by using the Show Network Configuration function of the Web Admin as explained below.
