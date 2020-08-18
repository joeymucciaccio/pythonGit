#Joseph Mucciaccio
#This program consists of requirements to demonstare the predator-prey example

import random
import pylab 
import numpy as np

#Island class
class Island (object):
    
    #This function creates the n by n grid
    def __init__(self, n, prey_count = 0, predator_count = 0, human_count = 0):
        self.grid_size = n
        self.grid = []
        for i in range(n):
            grid_row = [0] * n
            self.grid.append(grid_row)
        self.init_animals(prey_count,predator_count, human_count)

    #This function puts initial predators, prey, and humans on the island
    def init_animals(self, prey_count, predator_count, human_count):
        count = 0
        while count < prey_count:
            x = random.randint(0,self.grid_size-1)
            y = random.randint(0,self.grid_size-1)
            if not self.animal(x,y):
                prey_new = Prey(island = self, x = x, y = y)
                count = count + 1
                self.register(prey_new)
                
        count = 0
        while count < predator_count:
            x = random.randint(0,self.grid_size - 1)
            y = random.randint(0,self.grid_size - 1)
            if not self.animal(x,y):
                predator_new = Predator(island = self, x = x, y = y)
                count = count + 1
                self.register(predator_new)
                
        count = 0
        while count < human_count:
            x = random.randint(0,self.grid_size - 1)
            y = random.randint(0,self.grid_size - 1)
            if not self.animal(x, y):
                human_new = Human(island = self, x = x, y = y)
                count = count + 1
                self.register(human_new)

    #This function clears to allow for the next turn
    def clear_all_moved_flags(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[x][y]:
                    self.grid[x][y].clear_moved_flag()
    
    #This functon represents the size of the island
    def size(self):
        return self.grid_size

    #This function puts animals at coords
    def register(self, animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    #This function removes an animal from the island
    def remove(self,animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = 0

    #This function returns the coords of the animal or determines if it is in the bounds
    def animal(self,x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        else:
            return -1 # outside island boundary

    #This function helps represent (0,0)
    def __str__(self):
        string = ""
        for i in range(self.grid_size -1 , -1 , -1):
            for j in range(self.grid_size):
                if not self.grid[j][i]:
                    string = string + "{:<2s}".format('.' + " ")
                else:
                    string = string + "{:<2s}".format((str(self.grid[j][i])) + " ")
            string = string + "\n"
        return string
    
    #This function counts all the current prey on the island
    def count_prey(self):
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x, y)
                if animal:
                    if isinstance(animal, Prey):
                        count = count + 1
        return count

    #This function counts all the current predators on the island
    def count_predators(self):
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x, y)
                if animal:
                    if isinstance(animal, Predator):
                        count = count + 1
        return count

    #This function counts all the current humans on the island
    def count_humans(self):
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x, y)
                if animal:
                    if isinstance(animal,Human):
                        count = count + 1
        return count



#Animal class
class Animal(object):
    
    #This function gives animals positions and initializes them
    def __init__(self, island, x = 0, y = 0, string = "A"):
        self.island = island
        self.name = string
        self.x = x
        self.y = y
        self.moved = False
          
    #This function returns the current position
    def position(self):
        return self.x, self.y

    #This function returns name str
    def __str__(self):
        return self.name
  
    #This function checks for the animals first location in the grid (8 different directions) or does not if the location DNE
    def check_grid(self,type_looking_for=int):
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)] #8 different directions
        result = 0
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if not 0 <= x < self.island.size() or \
               not 0 <= y < self.island.size():
                continue
            if type(self.island.animal(x, y)) == type_looking_for:
                result = (x, y)
                break
        return result

    def move(self):
        '''Move to an open, neighboring position '''
        if not self.moved:
            location = self.check_grid(int)
            if location:
                self.island.remove(self)
                self.x = location[0]
                self.y = location[1]
                self.island.register(self)
                self.moved = True
    
    #This function creates a new pret at one of the 8 locations or makes them wait if none are available
    def breed(self):
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                self.breed_clock = self.breed_time
                the_class = self.__class__
                new_animal = the_class(self.island, x = location[0], y = location[1])
                self.island.register(new_animal)

    #This function clears moved flags
    def clear_moved_flag(self):
        self.moved = False



#Prey class
class Prey(Animal):
    
    #This function
    def __init__(self, island, x = 0, y = 0, string = "O"):
        Animal.__init__(self,island, x, y, string)
        self.breed_clock = self.breed_time
       
    #This function updates the breed clock
    def clock_tick(self):
        self.breed_clock -= 1



#Predator class
class Predator(Animal):
    
    #This function 
    def __init__(self, island, x = 0, y = 0, string = "X"):
        Animal.__init__(self, island, x, y, string)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time

    #This function updates the breed and starve clock
    def clock_tick(self):

        self.breed_clock -= 1
        self.starve_clock -= 1

        if self.starve_clock <= 0:
            self.island.remove(self)
            
    #This function looks in the 8 locations for prey and eats them, removing the prey and updating the starve
    def eat(self):
        if not self.moved:
            location = self.check_grid(Prey)
            if location:
                self.island.remove(self.island.animal(location[0],location[1]))
                self.island.remove(self)
                self.x = location[0]
                self.y = location[1]
                self.island.register(self)
                self.starve_clock=self.starve_time
                self.moved = True



#Human class
class Human(Animal):
    
    
    def __init__(self, island, x = 0, y = 0, string = "H"):
        Animal.__init__(self,island, x, y, string)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        self.hunt_time = self.hunt_time

    #This function updates both the breed and starve clock
    def clock_tick(self):
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)


    #This function looks in the 8 locations for predators, moves to that location and removes the predator and updates the starve
    def eat(self):
        ''' Human looks for one of the 8 locations with Predator. If found
        moves to that location, updates the starve clock, removes the Predator
        '''
        if not self.moved and self.hunt_time == 0:
            location = self.check_grid(Predator)
            if location:
                self.island.remove(self.island.animal(location[0],location[1]))
                self.island.remove(self)
                self.x = location[0]
                self.y = location[1]
                self.island.register(self)
                self.starve_clock=self.starve_time
                self.moved = True

#Main
def main(predator_breed_time = 8, predator_starve_time = 4, initial_predators = 12, prey_breed_time = 4, initial_prey = 50, \
         human_breed_time = 8, human_starve_time = 40, human_hunt_time = 10, initial_human = 12, size = 12, ticks = 300):

    Human.breed_time = human_breed_time
    Human.starve_time = human_starve_time
    Human.hunt_time = human_hunt_time
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time

    predator_list=[]
    prey_list=[]
    human_list=[]

    isle = Island(size,initial_prey, initial_predators, initial_human)
    print(isle)

    for i in range(ticks):
        isle.clear_all_moved_flags()
        for x in range(size):
            for y in range(size):
                animal = isle.animal(x,y)
                if animal:
                    if isinstance(animal, Predator) or isinstance(animal, Human):
                        animal.eat()
                    animal.move()
                    animal.breed()
                    animal.clock_tick()

        prey_count = isle.count_prey()
        predator_count = isle.count_predators()
        human_count = isle.count_humans()
        if prey_count == 0:
            print("The Prey population has been lost.")
            break
        if predator_count == 0:
            print("The Predator population has been lost.")
            break
        if human_count == 0:
            print("The Human population has been lost.")
            break
        prey_list.append(prey_count)
        predator_list.append(predator_count)
        predator_list.append(predator_count)
        human_list.append(human_count)

        if not i % 10:
            print(prey_count, predator_count, human_count)
            print("v v v")
    
    pylab.plot(np.array(range(0,len(predator_list))), np.array(predator_list), label = "Predators")
    pylab.plot(np.array(range(0,len(prey_list))), np.array(prey_list), label = "Prey")
    pylab.plot(np.array(range(0,len(human_list))), np.array(human_list), label = "Human")
    pylab.legend(loc = "best", shadow = True)
    pylab.show()

main()