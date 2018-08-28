# For managing and logging all connections to devices.


class ConnectionManager:
    # Constant returned when there is an error.
    EXECUTE_SUCCESS = 0
    EXECUTE_FAIL = 1

    # Constructor.
    def __init__(self, connection):
        # Netmiko connection for executing commands.
        self.connection = connection
        # Record of all commands executed and each one's result (for debugging).
        self.commands_executed = list()
        self.command_responses = list()
        # True if an error has occurred.
        self.error_status = False

    # Execute a command, log it, and return the associated error code.
    def execute(self, command):
        pass

    # Split each command at a newline and call execute method.
    def execute_block(self):
        pass

    # Prints the last command and response before the error occurred.
    def print_error(self):
        pass
