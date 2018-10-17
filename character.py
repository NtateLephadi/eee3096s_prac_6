""" a single character in password """
class character():

    """ initialise code character """
    def __init__(self, direction, duration):
        self.direction=direction
        self.duration=duration

    """ set code direction """
    def set_direction(self, direction):
        self.direction=direction

    """ set code duration """
    def set_duration(self, duration):
        self.duration=duration

    """ get character direction """
    def get_direction(self):
        return self.direction

    """ get character duration """
    def get_duration(self):
        return self.duration

    def to_string(self):
        """ get character as string """
        return str(self.direction) + " " + str(self.duration)

    """ define greater than operator """
    def __gt__(a, b):
        return a.get_duration() > b.get_duration()

    """ define less than operator """
    def __lt__(a, b):
        return a.get_duration() < b.get_duration()

    """ define equals to operator """
    def __eq__(a, b):
        return a.get_duration() == b.get_duration()
