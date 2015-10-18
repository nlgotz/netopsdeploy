Netops Deploy
==============================================================================

About
-----
The purpose of this project is to automate the deployment of network devices.
There are currently 2 plugins: Solarwinds and Infoblox

The Solarwinds plugin will add a device to Solarwinds and start polling on it. It may take up to 30 minutes to see all device information as it takes a while for Solarwinds to start polling.

The Infoblox plugin will create an A and PTR record for the device.

There is no error checking or unit testing, so this may not work correctly in your environment.

Installation
------------

```
$ pip install -r requirements.txt

$ pip install git+git://github.com/Infoblox-Development/Infoblox-API-Python

$ python setup.py install

$ ln -s config/netopsdeploy.conf ~/.netopsdeploy.conf
```

Future Plans for netopsdeploy
------------
These are in no particular order
1. Start adding unit testing
2. Make it so you can run a single plugin
3. Add Cisco ACS support for TACACS+
4. Create a wrapper to add multiple devices all at once (Automate the automation)
