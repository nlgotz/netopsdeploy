"""CLI tests for netopsdeploy."""

from netopsdeploy.utils import test

class CliTestCase(test.NetopsDeployTestCase):
    def test_netopsdeploy_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()
