"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """make new generator starting at start"""
        self.start = start
        self.value = self.start - 1

    def generate(self):
        """generate sequential value"""
        self.value += 1
        return self.value

    def reset(self):
        """rselt number to orignal start"""
        self.value = self.start-1

