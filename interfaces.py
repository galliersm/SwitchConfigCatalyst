# For managing all interface related operations.


# Instance held by main configurator module, handles all interface operations.
class Interfaces:
    # Constructor.
    def __init__(self, active_cmd, passive_cmd):
        # For executing active and passive commands.
        self.active_cmd = active_cmd
        self.passive_cmd = passive_cmd
        # Associated interfaces with the switch.
        self.ints = list()


# For maintaining and organizing information about individual interfaces.
class Interface:
    def __init__(self):
        # Port of the interface.
        self.port = None
        # Description on the interface.
        self.name = None
        # Interface status.
        self.status = None
        # Interface Vlan.
        self.vlan = None
        # Interface Duplex mode.
        self.duplex = None
        # Interface speed.
        self.speed = None
        # Interface type.
        self.type = None
        # Commands listed under the running config.
        self.run = list()
