class Animal:
    """ Can be placed inside cages, and according to its place in food chain
    it has a list attribute of its prey (what it likes to eat).
    """

    prey = []

    def __init__(self):
        self.name = 'Unnamed'       # Default naming, to be modified

    def __repr__(self):
        """ Identifies the Animal by its name and species (subclass).
        """
        return str(self.name) + " " + type(self).__name__


class Mouse(Animal):

    def __init__(self):
        super().__init__()


class Goat(Animal):

    def __init__(self):
        super().__init__()


class Rabbit(Animal):

    prey = [Mouse]     # Animal subclasses that Rabbits eat

    def __init__(self):
        super().__init__()


class Jackal(Animal):

    prey = [Goat, Rabbit]      # Animal subclasses that Jackals eat

    def __init__(self):
        super().__init__()


class Owl(Animal):

    prey = [Mouse]     # Animal subclasses that Owls eat

    def __init__(self):
        super().__init__()


class Snake(Animal):

    prey = [Mouse]     # Animal subclasses that Snakes eat

    def __init__(self):
        super().__init__()


class Kite(Animal):

    prey = [Snake]     # Animal subclasses that Kites eat

    def __init__(self):
        super().__init__()


class WildCat(Animal):

    prey = [Rabbit, Mouse]     # Animal subclasses that WildCats eat

    def __init__(self):
        super().__init__()


class Lion(Animal):

    prey = [Goat, Jackal, WildCat, Kite]
    # Animal subclasses that Lions eat

    def __init__(self):
        super().__init__()


class Cage:
    """ Contains a list of animals inside and performs methods to check
    intern competition where there might be a conflict of prey and predator,
    where a prey gets eaten.
    """

    def __init__(self):
        self.animals_list = []
        self.name = 'Cage'      # Default name configuration

    def __repr__(self):
        if len(self.animals_list) > 0:      # Checks if cage isn't empty
            return "{} contains {} animal(s): {}".format(self.name,
                                                         len(self.animals_list),
                                                         self.animals_list)
        else:
            return "{} (empty)".format(self.name)

    def check_prey(self):
        """ Method for checking the animals chain food competition inside a
        cage: iterates through its animals list and kills (deletes) the
        predator's prey.
        """
        death_statements = []
        # Check if any animals in the list have listed prey inside this cage:
        for predator in self.animals_list:
            prey_index = 0
            for prey in range(self.animals_list[]):      # Parses animal's prey list
                """ Compares the listed classes in an animal's prey list
                with the class of each other animal on the cage. """
                if type(prey) in predator.prey:
                    del self.animals_list[prey_index]       # Kills the prey
                    death_statements.append("{} got eaten by {}.".format(
                        prey, predator))
                prey_index += 1     # Increases index number for iterator
        self.animals_list.remove(prey) for animal in self._animals_list
        if len(death_statements) > 0:
            print("Oops! Seems like you put predator and prey on same cage.")
            for statement in death_statements:
                print(statement)
        print('Now ' + str(self))       # Shows updated list of animals in cage

    def add_animals(self, add_list):
        """ Inserts animals inside the Cage object. """
        duplicate_animals = []
        for animal in add_list:
            if animal.__class__.__base__ != Animal:
                print("{} could not be added because it's not an Animal object"
                      .format(animal))
            elif animal not in self.animals_list:
                # Inserts Animal object in cage if not already inside
                self.animals_list.append(animal)
            elif animal not in duplicate_animals:
                    duplicate_animals.append(animal)
        if len(duplicate_animals) > 0:
            duplicates = str(duplicate_animals[0])
            if len(duplicate_animals) > 1:
                for animal in duplicate_animals[1:]:
                    duplicates += (', ' + str(animal))
            print("Duplicate animal(s) found: {} already inside.".format(
                duplicates))
            print(self)
        return self.check_prey()
        # Starts check on whether there is prey and predator on the same cage


class Zoo:
    """ Contains a list of Cage objects and informs about the animals inside
    itself.
    """

    def __init__(self):
        super().__init__()
        self.name = 'Zoo'       # Default name
        self.cages = []

    def __repr__(self):
        if len(self.cages) > 0:
            return '{} contains {} cage(s) and a total of {} animal(s)'.format(
                self.name, len(self.cages), self.animals_count())
        else:
            return '{} (empty)'.format(self.name)

    def add_cages(self, list_to_add):       # Takes list of cages as argument
        for cage in list_to_add:
            if type(cage) == Cage:
                self.cages.append(cage)
            else:
                print("{} is not a Cage object.".format(cage))
        return self

    def n_of_cages(self):       # User method to find out number of cages
        return len(self.cages)

    def animals_count(self):
        """ Accessing attributes from instances of class Cage, it calculates
        how many animals are in total inside all cages of the zoo.
        """
        self.n_of_animals = 0
        for item in self.cages:
            # Appends to attribute sum of animals inside each cage
            self.n_of_animals += len(item.animals_list)
        return self.n_of_animals
