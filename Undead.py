class Undead:
    
    def __init__(self, name = None, hp = None):
        if name != None and hp != None:
            self.__hp = hp
            self.__name = "Undead" + name
        else:
            self.__hp = 300
            self.__name = "Undead"
            self.__isDead = False
    
    # dead is a boolean
    def isDead(self, dead = None):
        if dead == None:
            return self.__isDead
        else:
            self.__isDead = dead
        
    def getName(self):
        return self.__name
    
    def getHP(self):
        return self.__hp
    
    def setName(self, name):
        self.__name = name
    
    def setHP(self, hp = None, multiplier = None):
        if multiplier == None:
            self.__hp = hp
        else:
            self.__hp = round(self.__hp * multiplier)

class Zombie(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.5) # zombie has 1/2 of undead default
        print("I am Zombie")
    
    def attack(self):
        return round(super().getHP()*0.5) # zombie attack is half of hp
    
    def zombieAbility(attack):
        #putability
        pass
    
class Vampire(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.4)#vampire has base hp of 120
        print("I am Vampire")
    
    def attack(self):
        return round(super().getHP()*1) # vampire attack is same as its hp
    
    def vampireAbility(attack):
        #put ability
        pass
            
class Skeleton(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.267)#skeleton has 80 base hp
        print("I am Skeleton")
    def attack(self):
        return round(super().getHP()*0.7)#skeleton has attack damage 70% of its hp
    def skeletonAbility():
        #put ability
        pass

class Ghost(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.5)#Ghost initial HP would be the half of the initial HP of the undead
        print("I am Ghost")
    def attack(self):
        return round(super().getHP()*0.20)#Ghost may attack other undead. Its attack damage is only 20% of its hp
    def ghostAbility():
        #put ability
        pass
        
class Lich(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 1)#no multiplier
        print("I am Lich")
    def attack(self):
        return round(super().getHP()*0.70)# Lich attack damage is equal to 70 percent of its Hp
    def Lich():
        #put ability
        pass
        
class Mummy(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 1)#no multiplier
        print("I am Mummy")
    def attack(self):
        return round(super().getHP()*0.5)#attack damage is equal to the half of its HP plus 10%
    def Lich():
        #put ability
        pass    
               
#pancheck               
t = Mummy()
print(t.getHP())
print(t.attack())


        
