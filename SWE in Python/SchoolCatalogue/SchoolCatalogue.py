# Filename : SchoolCatalogue.py
# Author   : LR Steele
# Info     : Coding project/objective for "SWE in Python I" section of SWE for
#          : ML/AI Engineers course in Machine Learning/AI Engineer Career Path
#          : on Codecademy.

class School():
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_numberOfStudents(self):
        return self.numberOfStudents
    
    def set_numberOfStudents(self, number):
        self.numberOfStudents = number
    
    def __repr__(self):
        return "A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)
    
# Test
# ACHS = School("ACHS", "High", 160)
# print(ACHS.get_name())
# print(ACHS.get_level())
# print(ACHS.get_numberOfStudents())
# print(ACHS)

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, level="Primary", numberOfStudents=numberOfStudents)
        self.pickupPolicy = pickupPolicy
    
    def get_pickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        super_repr = super().__repr__()
        return super_repr + ", with a pickup policy of {pickupPolicy}".format(pickupPolicy=self.pickupPolicy)

# Test
# ACES = PrimarySchool("ACES", 200, "line-up at 2:50pm")
# print(ACES.get_pickupPolicy())
# print(ACES.get_name())
# print(ACES.get_level())
# print(ACES.get_numberOfStudents())
# print(ACES)

class MiddleSchool(School):
    def __init__(self, name, numberOfStudents):
        super().__init__(name, level="Middle", numberOfStudents=numberOfStudents)

# Test
# ACMS = MiddleSchool("ACMS", 80)
# print(ACMS.get_name())
# print(ACMS.get_level())
# print(ACMS.get_numberOfStudents())
# print(ACMS)

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, level="High", numberOfStudents=numberOfStudents)
        self.sportsTeams = sportsTeams
    
    def get_sportsTeams(self):
        return self.sportsTeams
    
    def __repr__(self):
        super_repr = super().__repr__()
        return super_repr + ", with sports teams {sportsTeams}".format(sportsTeams=self.sportsTeams)

# Test
# ACHS = HighSchool("ACHS", 160, ["XC", "Football", "Volleyball", "Basketball", "Track & Field", "Golf", "Baseball", "Softball"])
# print(ACHS.get_name())
# print(ACHS.get_level())
# print(ACHS.get_numberOfStudents())
# print(ACHS.get_sportsTeams())
# print(ACHS)