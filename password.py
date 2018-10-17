from character import character
import sys

class password:
    """ A single password """

    """ __init__ """
    def __init__(self, code):
        self.code=[]

    """ set code """
    def set_code(self, code):
        self.code=code

    """ return current code """
    def get_code(self, code):
        return self.code

    """ add a character to code """
    def add_character(self, character):
        self.code.append(character)

    """ validate code in secure mode """
    def validate_secure(self, code):
        return str(self.to_string()) == str(code.to_string())

    def validate_unsecure(self, other_password):
        """ validate code in unsecure mode """
        return sorted(self.code)==sorted(other_password.code)

    """ return code as string """
    def to_string(self):
        s=""
        for i in self.code:
            s = i.to_string() + " " + s
        return s
