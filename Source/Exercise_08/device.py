# Base class, this will never be instantiated
class Device():

    # Define a class object attribture, it will be the same for all instance of the class
    pi = 3.142

    # Constructre, called for use whenever an instance ofthe class is created
    def __int__(self) -> None:
        print("Running constructore for base class")
        # Create attributes and set inital values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame:str) -> int:
        print("Checking CRC from base")
        # Put real code in here, this is a dummy value for setup
        crc = 123456789
        return crc

# my_devices = Device()
# my_devices.calculate_crc("dummy")
# y_devices.run()

# Create child classes which in turn then access the methods and properties of the base class 'device.py'
class Firewall(Device):

    # Constuctor, called whenver an instance of the class is created
    # Use parameter 1 as a tag to id the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set inital values
        self.parameter1 = parameter1
        self.test_mesage = ""

    def configure_firewall(self):
        print("Configuring Firewall")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from child")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc

# Part of exercise try adding other devices
# I will try add a Cisco Switch

class CiscoSwitch(Device):
    # Constructor
    # Para2 as tag to ID CiscoSwitch
    def __init__(self, parameter2) -> None:
        # Call back
        Device.__init__(self)
        print(f"Running constructor for {parameter2}")
        # Create atributes and set values
        self.parameter2 = parameter2
        self.test_message2 = ""

    def configuring_CiscoSwitch(self):
        print("Configuring Cisco Switch")


hostname = "firewall3"
my_firewall = Firewall(hostname)
my_firewall.calculate_crc("dummy")
my_firewall.configure_firewall()

hostname2 = "Cisco Switch"
my_cisco_switch = CiscoSwitch(hostname2)
my_cisco_switch.configuring_CiscoSwitch()
