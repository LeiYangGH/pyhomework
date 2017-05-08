"""so hard"""
class Animal:
    """sad"""
    def __init__(self, identifier, species, age, sex, zoo, notes):
        """sad"""
        self.identifier = identifier
        self.species = species
        self.age = age
        self.sex = sex
        self.zoo = zoo
        self.notes = notes
        
    def __str__(self):
        """sgkjnrhb"""
        print('==============================')
        print('#{} - {}'.format(self.identifier, self.species))
        print('------------------------------')
        print('Age:', self.age)
        print('Sex:', self.sex)
        print('Zoo:', self.zoo)
        print('------------------------------')
        print('Notes:')
        if self.notes == []:
            print('No notes to display.')
        else:
            num = 1
            for i in self.notes:
                print('{}) {}'.format(num, i))
                num += 1
        return '=============================='            

    def add_note(self, note):
        """lirhkjndsgvihew"""
        return self.notes.append(note)         
                                          
                
def read_data_file(filename):
    """ewtrfdg"""
    file = open(filename).readlines()
    dic = {}
    for i in file[1:]:
        fff = i.strip('\n').split(',')
        identifier = fff[0] 
        species = fff[1]
        age = fff[2]
        sex = fff[3]
        zoo = fff[4]
        if len(fff) > 4:
            notes = fff[5:]        
        dic[int(fff[0])] = Animal(identifier, species, age, sex, zoo, notes)
    return dic

def get_filename():
    """Return the name of the data file to be processed
    This value is hard coded in for testing reasons"""
    return 'new_zealand_animals.csv'

def display_animal_information(animals):
    """input"""
    num = [str(x) for x in range(1, 675)] 
    while True:
        animal_identifier = input("Enter an animal identifier: ")
        if animal_identifier in num:
            print(animals[int(animal_identifier)])  
            break
        else:
            print('Error: Identifiers must be between 1 and 674.')

validzoos = ["Auckland Zoo", "Wellington Zoo", "Orana Wildlife Park"]

class Zoo:
    def calcanimalsnumbersinzoo(self):
        return sum([1 for a in self.lst if a.zoo == self.zooname])
    def calcspeciesnumbersinzoo(self):
        return len(set([a.species for a in self.lst if a.zoo == self.zooname]))
    def calcuniquespecies(self):
        myspecies = set([a.species for a in self.lst if a.zoo == self.zooname])
        otherspecies = set([a.species for a in self.lst if a.zoo != self.zooname])
        return list(set(myspecies) - set(otherspecies))

    def __init__(self,animals,zooname):
        """sad"""
        self.lst = list(animals.values())
        self.zooname = zooname
        self.animalsnumbers = self.calcanimalsnumbersinzoo()
        self.speciesnumbers = self.calcspeciesnumbersinzoo()
        self.uniquespecies = self.calcuniquespecies()

    def __str__(self):
        print('==============================')
        print('Zoo Statistics for ', self.zooname)
        print('------------------------------')
        print('Number of animals: ', self.animalsnumbers)
        print('Number of species: ', self.speciesnumbers)
        print('Unique species:')
        for u in self.uniquespecies:
            print('-', u)
        return '=============================='


def display_zoo_information(animals):
    while True:
        zoo = input("Enter a zoo: ")
        if zoo in validzoos:
            print(Zoo(animals,zoo))  
            break
        else:
            print('Error: Zoo not recognised.')
def main():
    """main_function"""
    animals = read_data_file(get_filename())
    while True:
        view = input('Enter a command: ')
        if view == 'view':
            display_animal_information(animals)
        elif view == 'stats':
            display_zoo_information(animals)
        elif view == 'quit':
            break
        else:
            print('Error: Invalid input.')
main()
#animals = read_data_file(get_filename())
#zoo = "Orana Wildlife Park"
#print(Zoo(animals,zoo))
