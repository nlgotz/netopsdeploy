"""Netops Deploy bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as NetopsDeployBaseController.

from cement.core import handler
from netopsdeploy.cli.controllers.base import NetopsDeployBaseController

def load(app):
    handler.register(NetopsDeployBaseController)
