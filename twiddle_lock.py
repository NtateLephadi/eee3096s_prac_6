from password import password
from character import character

class twiddle_lock:
    """ dialed lock """

c1=character('A', 3)
c2=character('C', 3)

p1=password([])
p2=password([])

p1.add_character(c1)
p2.add_character(c2)

print(p1.to_string())
print(p2.to_string())
print(p1.validate_unsecure(p2))
