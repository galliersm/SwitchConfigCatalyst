# Handles all configuration operations on switch connections.
from decouple import config

from netmiko import ConnectHandler
from connection_manager import ConnectionManager


# Top level class for interacting with a device.
class CatalystConfigurator:
    # Default device type for Cisco Catalyst switches.
    NETMIKO_DEV_TYPE = 'cisco_ios'

    # Constructor.
    def __init__(self,
                 ip_addr,
                 username=config('USER'),
                 password=config('PASSWORD'),
                 port=config('PORT', cast=int),
                 secret=config('SECRET'),
                 verbose=False
                 ):
        # Create an ssh connection to the device.
        self.connection = ConnectHandler(
            device_type=self.NETMIKO_DEV_TYPE,
            ip=ip_addr,
            username=username,
            password=password,
            port=port,
            secret=secret,
            verbose=verbose
        )
        # Create connection manager objects for active and passive commands.
        self.active_cmd = ConnectionManager(self.connection)
        self.passive_cmd = ConnectionManager(self.connection)

