### Docstring ###

class Tournament:

### Docstring ###

    def __init__(self):
        self.name = None
        self.location = None
        self.start_date = None
        self.rounds_number = 4
        self.rounds = None
        self.players = None
        self.time_control = None
        self.description = None
        self.status = None
    
    def add_player(self):
        pass

    def is_start(self):
        self.status = "Started"

    def is_stop(self):
        self.status = "Stopped"
    
    def is_finish(self):
        self.status = "Finished"
    
    def start_round(self):
        pass

    def get_round_list(self):
        pass

    def get_match_list(self):
        pass
