#class that represents a scedule
import json
class Schedule:
    def __init__(self, json_info = None):
        self.fitness = None
        #The actual schedule information
        self.content = [] #WIll be an array of sets
        
    def from_json(self, json_data):
        pass

    def __str__(self):
        pass

    def to_json(self):
        pass
