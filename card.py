class Card:

    def __init__(self, ID, value, suite, sv, ss, abs_val):
        self.ID = ID
        self.suite = suite
        self.value = value
        self.ss = ss
        self.sv = sv
        self.abs_val = abs_val

        
        
    def print_long(self):
        print(self.value, " of ", self.suite, end = ' ')

    def print_short(self):
        print(self.ss + "" + self.sv, end = ' ')