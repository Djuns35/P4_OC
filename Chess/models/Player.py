### Docstring ###

class Player:

### Docstring ###
 
    def __init__(self):
        self.last_name = None
        self.first_name = None
        self.birth_date = None
        self.gender = None
        self.ranking = None
    
    def is_winner(self):
        self.ranking += 1
    
    def is_equal(self):
        self.ranking += 0.5

    def is_loser(self):
        self.ranking += 0
        