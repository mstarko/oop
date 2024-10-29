
class Person:
    def __init__(self, name, age, city):
        self.name = name      # Ім'я людини
        self.age = age        # Вік людини
        self.city = city      # Місто людини

    def introduce(self):
        print(f"здоров, мене звати {self.name}, мені {self.age} років, і я живу в місті {self.city}.")
