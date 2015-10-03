"""Netops Deploy exception classes."""

class NetopsDeployError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class NetopsDeployConfigError(NetopsDeployError):
    """Config related errors."""
    pass

class NetopsDeployRuntimeError(NetopsDeployError):
    """Generic runtime errors."""
    pass

class NetopsDeployArgumentError(NetopsDeployError):
    """Argument related errors."""
    pass
