"""SolarWinds Orion Plugin for Netops Deploy."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
import swisclient

def ip_to_guid(IPAddress):
    ip = IPAddress.split('.')
    ip_guid = ""
    for part in reversed(ip):
        ip_guid += (format(int(part), '02x'))
    ip_guid += '-0000-0000-0000-000000000000'
    return ip_guid


def solarwinds_plugin_hook(app):
    # do something with the ``app`` object here.

    server = app.config.get('solarwinds', 'sw_server')
    username = app.config.get('solarwinds', 'sw_username')
    password = app.config.get('solarwinds', 'sw_password')

    print "Solar Winds:"
    print("Server   : %s" % server)

    print "Starting"
    swis = swisclient.SwisClient(server,username,password)

    ip = app.pargs.ip
    IP_input = ip.strip()
    EntityType = "Orion.Nodes"

    uri = swis.create(EntityType,
        IPAddress = IP_input,
        IPAddressGUID = ip_to_guid(IP_input),
        DynamicIP = False,
        EngineID = 2,
        Status = 1,
        UnManaged = False,
        Allow64BitCounters = True,
        ObjectSubType = "SNMP",
        MachineType = "",
        VendorIcon = "",
        RediscoveryInterval = 30,
        PollInterval = 60,
        StatCollection = 1,
        Community = 'wine1headache',
        SNMPVersion = 2,
        BufferNoMemThisHour = -2,
        BufferNoMemToday = -2,
        BufferSmMissThisHour = -2,
        BufferSmMissToday = -2,
        BufferMdMissThisHour = -2,
        BufferMdMissToday = -2,
        BufferBgMissThisHour = -2,
        BufferBgMissToday = -2,
        BufferLgMissThisHour = -2,
        BufferLgMissToday = -2,
        BufferHgMissThisHour = -2,
        BufferHgMissToday = -2)

    print "Created Device"

    # Get all object properties for new node added
    # This adds all possible pollers except for Wireless Controllers
    obj = swis.read(uri)
    obj001 = swis.create("Orion.Pollers", PollerType = "N.Details.SNMP.Generic", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj018 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoCadant", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj019 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoExtreme", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj020 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoFoundry", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj021 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoGen1", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj022 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoGen2", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj023 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoGen3", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj024 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoNexus", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj025 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoRapid", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj026 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.CiscoRiverDelta", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj029 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.H3CGen1", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj030 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.H3CGen2", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj031 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.H3CRouter", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj032 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.H3CSwitch", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj033 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.HpColubrisUsageInfo", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj034 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.HrProcessorLoad", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj035 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.JuniperERX", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj036 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.JuniperJunOS", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj037 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.JuniperSSGNetScreen", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj038 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.NetSnmpCpuIdle", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj039 = swis.create("Orion.Pollers", PollerType = "N.Cpu.SNMP.NetSnmpSystemStats", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj053 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoCadant", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj054 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoExtreme", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj055 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoFoundry", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj056 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoGen1", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj057 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoGen3", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj058 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoGen3SystemMemory", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj059 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoGen4", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj060 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoRapid", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj061 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CiscoRiverDelta", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj062 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.CpqHostPhysicalMemory", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj063 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.F5BigIpSystemHost", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj064 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.F5BigIpSystemTmm", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj065 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.H3CGen1", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj066 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.H3CGen2", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj067 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.HpColubrisUsageInfo", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj068 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.HrStorage", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj069 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.HrSwRunPerf", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj070 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.HuaweiH3CRouter", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj071 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.HuaweiH3CSwitch", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj072 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.JuniperERX", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj073 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.JuniperJunOS", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj074 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.JuniperSSGNetScreen", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj075 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.MemoryCiscoNexus", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj076 = swis.create("Orion.Pollers", PollerType = "N.Memory.SNMP.NetSnmpReal", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj079 = swis.create("Orion.Pollers", PollerType = "N.IPAddress.ICMP.Generic", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj080 = swis.create("Orion.Pollers", PollerType = "N.IPAddress.SNMP.Generic", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj082 = swis.create("Orion.Pollers", PollerType = "N.Topology_Vlans.SNMP.Dot1q", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj083 = swis.create("Orion.Pollers", PollerType = "N.Topology_Vlans.SNMP.VmMembershipSummary", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj084 = swis.create("Orion.Pollers", PollerType = "N.Topology_Vlans.SNMP.VtpVlan", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj085 = swis.create("Orion.Pollers", PollerType = "N.Topology_PortsMap.SNMP.Dot1dBase", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj086 = swis.create("Orion.Pollers", PollerType = "N.Topology_PortsMap.SNMP.Dot1dBaseNoVLANs", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj087 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer2.SNMP.Dot1dTpFdb", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj088 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer2.SNMP.Dot1dTpFdbNoVLANs", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj089 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer2.SNMP.Dot1qTpFdb", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj090 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer2.SNMP.Dot1qTpFdbNoVLANs", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj091 = swis.create("Orion.Pollers", PollerType = "N.Topology_CDP.SNMP.cdpCacheTable", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj092 = swis.create("Orion.Pollers", PollerType = "N.Topology_LLDP.SNMP.lldpRemoteSystemsData", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj093 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer3.SNMP.ipNetToMedia", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj094 = swis.create("Orion.Pollers", PollerType = "N.Remap.SNMP.Apresia", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj095 = swis.create("Orion.Pollers", PollerType = "N.Remap.SNMP.NetScreen", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj104 = swis.create("Orion.Pollers", PollerType = "N.EnergyWise.SNMP.Cisco", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj108 = swis.create("Orion.Pollers", PollerType = "N.Status.ICMP.Native", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj109 = swis.create("Orion.Pollers", PollerType = "N.Routing.SNMP.Ipv4CidrRoutingTable", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj110 = swis.create("Orion.Pollers", PollerType = "N.RoutingNeighbor.SNMP.BGP", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj111 = swis.create("Orion.Pollers", PollerType = "N.RoutingNeighbor.SNMP.OSPF", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj112 = swis.create("Orion.Pollers", PollerType = "N.Topology_CDP.SNMP.cdpCacheTable", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj113 = swis.create("Orion.Pollers", PollerType = "N.Topology_STP.SNMP.Dot1dStp", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj114 = swis.create("Orion.Pollers", PollerType = "N.Topology_PortsMap.SNMP.Dot1dBase", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj115 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer3.SNMP.ipNetToMedia", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj116 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer3_IpRouting.SNMP.rolesRouter", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj117 = swis.create("Orion.Pollers", PollerType = "N.Topology_Layer3_IpRouting.SNMP.ipCidrRouter", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj118 = swis.create("Orion.Pollers", PollerType = "N.Uptime.SNMP.Generic", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])
    obj118 = swis.create("Orion.Pollers", PollerType = "N.ResponseTime.ICMP.Native", NetObject="N:" + str(obj["NodeID"]), NetObjectType="N", NetObjectID=obj["NodeID"])

    print "Created Pollers"

    print "Adding to NCM"
    ### Add Node to NCM
    ncm = swis.invoke("Cirrus.Nodes", "AddNodetoNCM", str(obj["NodeID"]))
    print "Added to NCM"

    print "Discovering Interfaces"
    ### Add Discovered Nodes
    discovered =  swis.invoke("Orion.NPM.Interfaces", "DiscoverInterfacesOnNode", str(obj["NodeID"]))
    print "Discovered Interfaces"

    addint = swis.invoke("Orion.NPM.Interfaces", "AddInterfacesOnNode", str(obj["NodeID"]), discovered["DiscoveredInterfaces"], "AddDefaultPollers")
    print "Added Interfaces"

    print "Done!"

    print("Node ID  :   %s" % str(obj["NodeID"]))




    pass

class SolarwindsPluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'solarwinds'

        # text displayed next to the label in ``--help`` output
        description = 'Add node to Solar Winds Orion'

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
        print("Inside SolarwindsPluginController.default()")


def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(SolarwindsPluginController)

    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', solarwinds_plugin_hook)
