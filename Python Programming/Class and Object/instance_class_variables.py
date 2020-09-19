class Shark:
    # Class Variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")


def main():
    # First object, set up instance variable of constructor method
    sammy = Shark("Sammy", 5)    

    # Print out instance variable name
    print(sammy.name)

    # Print out class variable location
    print(sammy.location)

    # Second object
    stevie = Shark("Stevie", 8)
    
    # Print out instance variable name
    print(stevie.name)

    stevie.set_followers(77)
    



if __name__ == "__main__":
    main()
