"""Test for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook

class TestPluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'test'

        # text displayed next to the label in ``--help`` output
        description = 'Shows what changes will be made'

        # stack this controller on-top of ``base`` (or any other controller)
        stacked_on = 'base'

        # determines whether the controller is nested, or embedded
        stacked_type = 'nested'

        # these arguments are only going to display under
        # ``$ netopsdeploy example --help``
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

    @expose(hide=True)
    def default(self):
        # setup variables variables
        hostname    = self.app.pargs.hostname
        ip          = self.app.pargs.ip
        domain      = self.app.config.get('netopsdeploy', 'domain')

        # make sure that an IP and hostname are supplied
        if(ip and hostname):
            RunPluginController.printConfiguration(self, hostname, ip, domain)
        else:
            raise Exception('No IP or hostname supplied')


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

def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(TestPluginController)
    # register a hook (function) to run after arguments are parsed.
    #hook.register('post_argument_parsing', solarwinds_plugin_hook)
