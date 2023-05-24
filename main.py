class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name} is {self.age} years old."



person = Human("John", 36)
print(person)
