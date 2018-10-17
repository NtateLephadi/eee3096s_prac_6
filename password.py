from character import character
import sys

class password:
    
    def __init__(self, code):
        self.code=[]
        
    def set_code(self, code):
        self.code=code
        
    def get_code(self, code):
        return self.code
    
    def add_character(self, character):
        self.code.append(character)
        
    def validate_secure(self, code):
        return str(self.to_string()) == str(code.to_string())
    
    def validate_unsecure(self, other_password):
        return sorted(self.code)==sorted(other_password.code)          
        
    def to_string(self):
        s=""
        for i in self.code:
            s = i.to_string() + " " + s
        return s
        
c1=character('A', 2) 
c2=character('C', 3)

c3=character('A', 2) 
c4=character('C', 3)

p1=password([])
p2=password([])

p2.add_character(c1)
p2.add_character(c2)
p1.add_character(c3)
p1.add_character(c4)


print(p1.validate_secure(p2))
print(p1.validate_unsecure(p2))