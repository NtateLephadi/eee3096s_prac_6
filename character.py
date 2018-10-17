class character():
    def __init__(self, direction, duration):
        self.direction=direction
        self.duration=duration
    
    def set_direction(self, direction):
        self.direction=direction
        
    def set_duration(self, duration):
        self.duration=duration
    
    def get_direction(self):
        return self.direction
    
    def get_duration(self):
        return self.duration
    
    def to_string(self):
        return str(self.direction) + " " + str(self.duration)
    
    def __gt__(a, b):
        return a.get_duration() > b.get_duration()
    
    def __lt__(a, b):
        return a.get_duration() < b.get_duration()
        
    def __eq__(a, b):
        return a.get_duration() == b.get_duration()        
        