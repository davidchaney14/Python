

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
