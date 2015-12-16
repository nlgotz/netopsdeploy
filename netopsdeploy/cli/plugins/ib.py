"""Example Plugin for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
import infoblox
import requests

def ib_plugin_hook(app):
    IP_input = app.pargs.ip.strip()
    server = app.config.get('ib', 'ib_server')
    username = app.config.get('ib', 'ib_username')
    password = app.config.get('ib', 'ib_password')
    version = app.config.get('ib', 'ib_version')

    hostname = app.pargs.hostname
    domain = app.config.get('netopsdeploy', 'domain')
    # Create the fqdn for the host
    fqdn = hostname + "." + domain

    print("Starting to add DNS records")

    # Create Connection to Infoblox
    iba_api = InfobloxSubclass(server, username, password, version, 'default', 'default')

    try:
        ip = iba_api.create_device_record(IP_input, fqdn)
        print ip
        print("Created A and PTR records for:   %s" % fqdn)
    except Exception as e:
        print e
    pass


class IbPluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'ib'

        # text displayed next to the label in ``--help`` output
        description = 'Add A and PTR record to Infoblox'

        # stack this controller on-top of ``base`` (or any other controller)
        stacked_on = 'run'

        # determines whether the controller is nested, or embedded
        stacked_type = 'embedded'

        # these arguments are only going to display under
        # ``$ netopsdeploy example --help``
        arguments = [
            (['--ib-server'],
             dict(help='Infoblox Server Name', dest='ib_server', action='store',
                  metavar='TEXT') ),
            (['--ib-username'],
             dict(help='Infoblox Username', dest='ib_username', action='store',
                  metavar='TEXT') ),
            (['--ib-password'],
             dict(help='Infoblox Password', dest='ib_password', action='store',
                  metavar='TEXT') ),
        ]

def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(IbPluginController)
    # register a hook (function) to run after arguments are parsed.
    #hook.register('post_argument_parsing', ib_plugin_hook)


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
