from datetime import datetime

class Patient:
    def __init__(self, name, ailment):
        self.name = name
        self.ailment = ailment
        self.timestamp =datetime.now().strftime("%H:%M")

    def get_details(self): 
        return f"Patient {self.name} arrived at {self.timestamp} with {self.ailment}."
