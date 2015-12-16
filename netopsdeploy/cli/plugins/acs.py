"""Cisco ACS 5.6 Plugin for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook

def acs_plugin_hook(app):
    # do something with the ``app`` object here.

    pass

class ACSPluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'acs'

        # text displayed next to the label in ``--help`` output
        description = 'Add node to Cisco ACS 5.6'

        # stack this controller on-top of ``base`` (or any other controller)
        stacked_on = 'run'

        # determines whether the controller is nested, or embedded
        stacked_type = 'embedded'



def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(ACSPluginController)
    # register a hook (function) to run after arguments are parsed.
    #hook.register('post_argument_parsing', solarwinds_plugin_hook)
