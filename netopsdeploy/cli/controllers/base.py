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
            (['-c', '--community'],
             dict(help='SNMP Community String', dest='community', action='store',
                  metavar='TEXT') ),
            (['-d', '--domain'],
             dict(help='DNS domain of the device', dest='domain', action='store',
                  metavar='TEXT') ),
            (['-ib', '--infoblox'],
             dict(help='Add device to Infoblox', dest='infoblox', action='store_true')),
            (['-s', '--solarwinds'],
             dict(help='Add device to Solar Winds', dest='solarwinds', action='store_true')),
            ]

    @expose(hide=False)
    def run(self):
        # setup variables variables
        hostname    = self.app.pargs.hostname
        ip          = self.app.pargs.ip
        domain      = self.app.config.get('netopsdeploy', 'domain')



        # make sure that an IP and hostname are supplied
        if(ip and hostname):
            NetopsDeployBaseController.printConfiguration(self, hostname, ip, domain)

            if(self.app.pargs.infoblox):
                # run infoblox
                import netopsdeploy.cli.plugins.ib as ib
                ib.ib_plugin_hook(self.app)
            
            if(self.app.pargs.solarwinds):
                print "Solarwinds"
                # run solarwinds
                import netopsdeploy.cli.plugins.solarwinds as sw
                sw.solarwinds_plugin_hook(self.app)

        else:
            raise Exception('No IP or hostname supplied')
    
    @expose(hide=False)
    def test(self):
        # setup variables variables
        hostname    = self.app.pargs.hostname
        ip          = self.app.pargs.ip
        domain      = self.app.config.get('netopsdeploy', 'domain')



        # make sure that an IP and hostname are supplied
        if(ip and hostname):
            NetopsDeployBaseController.printConfiguration(self, hostname, ip, domain, test)
            return("Test successful")
        else:
            raise Exception('No IP or hostname supplied')


    @expose(hide=True)
    def default(self):
        print("Inside NetopsDeployBaseController.default().")





    def printConfiguration(self, hostname, ip, domain):
        print("Configuration:")
        print("--------------")
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
