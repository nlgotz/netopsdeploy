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
            ]
    @expose(hide=True)
    def default(self):
        print("Inside NetopsDeployBaseController.default().")
        print("test? = %r" % self.app.pargs.test)
        print("hostname = %s" % self.app.pargs.hostname)
        print("ip = %s" % self.app.pargs.ip)
        print("domain = %s" % self.app.pargs.domain)

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
