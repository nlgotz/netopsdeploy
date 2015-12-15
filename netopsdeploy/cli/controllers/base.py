"""Netops Deploy base controller."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
import sys
import os.path, pkgutil

class NetopsDeployBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Admin functions for Netops Device Deployment'

    @expose(hide=True)
    def default(self):
        print("Inside NetopsDeployBaseController.default().")
