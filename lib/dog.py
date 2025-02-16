class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", 
        "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Unknown", breed="Mutt"):
        self.name = name
        self._breed = None  # Initialize _breed to None
        self.breed = breed  # Use the setter to validate breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Set to None if invalid

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None  # Set to None if invalid