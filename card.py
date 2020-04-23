
class Card:

    def __init__(self, ID, value, suite, sv, ss):
        self.ID = ID
        self.suite = suite
        self.value = value
        self.ss = ss
        self.sv = sv

    def print_long(self):
        print(self.value, " of ", self.suite, end = ' ')

    def print_short(self):
        print(self.ss + "" + self.sv, end = ' ')