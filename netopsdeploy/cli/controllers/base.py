"""Netops Deploy base controller."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
import sys
import os.path, pkgutil

class NetopsDeployBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Admin functions for Netops Device Deployment'


        arguments = [
            (['-n', '--hostname'],
             dict(help='hostname of the device', dest='hostname', action='store',
                  metavar='TEXT') ),
            (['-i', '--ip'],
             dict(help='IP address of the device', dest='ip', action='store',
                  metavar='TEXT') ),
            (['-d', '--domain'],
             dict(help='DNS domain of the device', dest='domain', action='store',
                  metavar='TEXT') ),
            (['-T', '--test'],
             dict(help='Test the variables. Does not actually insert data', dest='test',
                  action='store_true',) ),
            (['--solarwinds-server'],
             dict(help='Solarwinds Server Name', dest='sw_server', action='store',
                  metavar='TEXT') ),
            (['--solarwinds-username'],
             dict(help='Solarwinds Username', dest='sw_username', action='store',
                  metavar='TEXT') ),
            (['--solarwinds-password'],
             dict(help='Solarwinds Password', dest='sw_password', action='store',
                  metavar='TEXT') ),
            (['--infoblox-server'],
             dict(help='Infoblox Server Name', dest='ib_server', action='store',
                  metavar='TEXT') ),
            (['--infoblox-username'],
             dict(help='Infoblox Username', dest='ib_username', action='store',
                  metavar='TEXT') ),
            (['--infoblox-password'],
             dict(help='Infoblox Password', dest='ib_password', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=False)
    def run(self):
        # setup variables variables
        test        = self.app.pargs.test
        hostname    = self.app.pargs.hostname
        ip          = self.app.pargs.ip
        domain      = self.app.config.get('netopsdeploy', 'domain')



        # make sure that an IP and hostname are supplied
        if(ip and hostname):
            NetopsDeployBaseController.printConfiguration(self, hostname, ip, domain, test)
            if(test):
                return("Test successful")
                pass

            # run infoblox
            import netopsdeploy.cli.plugins.ib as ib
            ib.ib_plugin_hook(self.app)

            # run solarwinds
            import netopsdeploy.cli.plugins.solarwinds as solarwinds
            solarwinds.solarwinds_plugin_hook(self.app)

        else:
            raise Exception('No IP or hostname supplied')



    @expose(hide=True)
    def default(self):
        print("Inside NetopsDeployBaseController.default().")





    def printConfiguration(self, hostname, ip, domain, test):
        print("Configuration:")
        print("--------------")
        print("Testing? : %r" % test)
        print("hostname : %s" % hostname)
        print("ip       : %s" % ip)
        print("domain   : %s" % domain)
        print("")
        print("Solarwinds:")
        print("-----------")
        print("Server   : %s" % self.app.config.get('solarwinds', 'sw_server'))
        print("Username : %s" % self.app.config.get('solarwinds', 'sw_username'))
        print("")
        print("Infoblox:")
        print("---------")
        print("Server   : %s" % self.app.config.get('ib', 'ib_server'))
        print("Username : %s" % self.app.config.get('ib', 'ib_username'))
        print("Version  : %s" % self.app.config.get('ib', 'ib_version'))
