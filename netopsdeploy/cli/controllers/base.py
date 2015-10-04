"""Netops Deploy base controller."""

from cement.core.controller import CementBaseController, expose

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
    @expose(hide=True)
    def default(self):
        print("Inside NetopsDeployBaseController.default().")
        print "Configuration items:"
        print("Testing? : %r" % self.app.pargs.test)
        print("hostname : %s" % self.app.pargs.hostname)
        print("ip       : %s" % self.app.pargs.ip)
        print("domain   : %s" % self.app.config.get('netopsdeploy', 'domain'))
        print "\r\nSolar Winds:"
        print("Server   : %s" % self.app.config.get('netopsdeploy', 'sw_server'))
        print("Username : %s" % self.app.config.get('netopsdeploy', 'sw_username'))
        print("Password : %s" % self.app.config.get('netopsdeploy', 'sw_password'))
        print "\r\nInfoblox:"
        print("Server   : %s" % self.app.config.get('netopsdeploy', 'ib_server'))
        print("Username : %s" % self.app.config.get('netopsdeploy', 'ib_username'))
        print("Password : %s" % self.app.config.get('netopsdeploy', 'ib_password'))

        # Add Node to Solarwinds

        # Add Node to Infoblox DNS

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``netopsdeploy.cli.templates``, or ``/var/lib/netopsdeploy/templates/``.
        #
