"""Tests for Example Plugin."""

from netopsdeploy.utils import test

class ExamplePluginTestCase(test.NetopsDeployTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
