"""Example Plugin for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
import infoblox

"""
Extends the Infoblox API found here:
https://github.com/Infoblox-Development/Infoblox-API-Python
"""
class InfobloxSubclass(infoblox.Infoblox):
    def create_a_record(self, address, fqdn):
        """ Implements IBA REST API call to create IBA a record
        :param address: IP v4 address or NET v4 address in CIDR format to get next_available_ip from
    	:param fqdn: hostname in FQDN
        """
        rest_url = 'https://' + self.iba_host + '/wapi/v' + self.iba_wapi_version + '/record:a'
        payload = '{"ipv4addr": "' + address + '","name": "' + fqdn + '","view": "' + self.iba_dns_view + '"}'
        try:
            r = requests.post(url=rest_url, auth=(self.iba_user, self.iba_password), verify=self.iba_verify_ssl, data=payload)
            r_json = r.json()
            if r.status_code == 200 or r.status_code == 201:
                return
            else:
                if 'text' in r_json:
                    raise InfobloxGeneralException(r_json['text'])
                else:
                    r.raise_for_status()
        except ValueError:
            raise Exception(r)
        except Exception:
            raise

    def create_ptr_record(self, address, fqdn):
        """ Implements IBA REST API call to create IBA ptr record
        :param address: IP v4 address or NET v4 address in CIDR format to get next_available_ip from
	    :param fqdn: hostname in FQDN
        """
        rest_url = 'https://' + self.iba_host + '/wapi/v' + self.iba_wapi_version + '/record:ptr'
        payload = '{"ipv4addr": "' + address + '","ptrdname": "' + fqdn + '","view": "' + self.iba_dns_view + '"}'
        try:
            r = requests.post(url=rest_url, auth=(self.iba_user, self.iba_password), verify=self.iba_verify_ssl, data=payload)
            r_json = r.json()
            if r.status_code == 200 or r.status_code == 201:
                return
            else:
                if 'text' in r_json:
                    raise InfobloxGeneralException(r_json['text'])
                else:
                    r.raise_for_status()
        except ValueError:
            raise Exception(r)
        except Exception:
            raise

    def create_device_record(self, address, fqdn):
        """ Implements IBA REST API call to create IBA a and ptr record
        :param address: IP v4 address or NET v4 address in CIDR format to get next_available_ip from
	    :param fqdn: hostname in FQDN
        """
        try:
            self.create_a_record(address, fqdn)
        except ValueError:
            raise Exception(r)
        except Exception:
            raise
        try:
            self.create_ptr_record(address, fqdn)
        except ValueError:
            raise Exception(r)
        except Exception:
            raise

"""
Adds device A and PTR records. This could probably be extended further if you
record other information in Infoblox
"""
def infoblox_plugin_hook(app):
    # do something with the ``app`` object here.
    IP_input = app.pargs.ip.strip()
    server = app.config.get('infoblox', 'ib_server')
    username = app.config.get('infoblox', 'ib_username')
    password = app.config.get('infoblox', 'ib_password')
    version = app.config.get('infoblox', 'ib_version')

    hostname = app.pargs.hostname
    domain = app.config.get('netopsdeploy', 'domain')
    # Create the fqdn for the host
    fqdn = hostname + "." + domain

    # Print basic information
    print "Infoblox:"
    print("Server   : %s" % server)
    print("Version  : %s\r\n" % version)

    # Create Connection to Infoblox
    iba_api = InfobloxSubclass(server, username, password, version, 'default', 'default')

    try:
        ip = iba_api.create_device_record(IP_input, fqdn)
        print ip
    except Exception as e:
        print e

    print("Created A and PTR records for:   %s" % fqdn)
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
                #['-f', '--foo'],
                #dict(
                #    help='Notorious foobar option',
                #    action='store',
                #    )
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
