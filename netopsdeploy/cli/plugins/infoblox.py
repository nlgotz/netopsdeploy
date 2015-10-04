"""Example Plugin for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook

def infoblox_plugin_hook(app):
    # do something with the ``app`` object here.
    print "Infoblox:"
    print("Server   : %s" % app.config.get('infoblox', 'ib_server'))
    print("Username : %s" % app.config.get('infoblox', 'ib_username'))
    print("Password : %s\r\n" % app.config.get('infoblox', 'ib_password'))

    pass

class InfobloxPluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'infoblox'

        # text displayed next to the label in ``--help`` output
        description = 'Add node to Infoblox DNS'

        # stack this controller on-top of ``base`` (or any other controller)
        stacked_on = 'base'

        # determines whether the controller is nested, or embedded
        stacked_type = 'nested'

        # these arguments are only going to display under
        # ``$ netopsdeploy example --help``
        arguments = [
            (
                ['-f', '--foo'],
                dict(
                    help='Notorious foobar option',
                    action='store',
                    )
            )
        ]

    @expose(hide=True)
    def default(self):
        print("Inside InfobloxPluginController.default()")


def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(InfobloxPluginController)

    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', infoblox_plugin_hook)
