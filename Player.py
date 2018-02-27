class Player():
    def __init__(self):
        self.lifeTotal = 20
        self.InfectResistance = 10;

    def apply_damage(self, damage):
        '''damage can only be an int, if damage is negative, life will be added'''
        self.lifeTotal -= damage

    def apply_infect(self, infect):
        '''infect must be an int, it can't be negative'''
        self.InfectResistance -= infect

    def still_alive(self):
        '''returns a boolean value. True if the player is still alive.'''
        if (self.lifeTotal>0 and self.InfectResistance>0):
            return True
        return False




New_player = Player()
New_player.apply_damage(15)
print(New_player.still_alive())
New_player.apply_damage(15)
print(New_player.still_alive())
