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
    def __init__(self, start = 100):
                """this def start the intial value from 100"""
                self.start = start
                self.current = start


    def generate (self):
            """this def generate the seriel number by incementing 1"""
            self_number = self.current
            self.current += 1
            return self_number
    
    def reset (self):
            """this def reset the generator back to intial value"""
            self.current = self.start

