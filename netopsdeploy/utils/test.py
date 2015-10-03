"""Testing utilities for Netops Deploy."""

from netopsdeploy.cli.main import NetopsDeployTestApp
from cement.utils.test import *

class NetopsDeployTestCase(CementTestCase):
    app_class = NetopsDeployTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(NetopsDeployTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(NetopsDeployTestCase, self).tearDown()

