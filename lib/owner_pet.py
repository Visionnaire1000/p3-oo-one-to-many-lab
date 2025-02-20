class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner if it's an instance of Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        pet.owner = self  # Assign this owner to the pet

    def get_sorted_pets(self):
        """Returns a list of the owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)  # Store the instance in the class variable
