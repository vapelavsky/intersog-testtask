# Test Task for Intersog

class Human:
    """This is the human from TikTok and she can entertain you.
    Available methods:
    1. drink
    2. travel
    3. sum calculate
    4. sleep
    5. show hobbies"""
    name: str
    age: int
    sex: str
    hobbies: list
    country: str
    job: str
    hair: str
    height: int

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        self.age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex: str):
        self.__sex = sex

    def get_height(self):
        return self.__height

    def set_height(self, height: float):
        self.__height = height

    def get_hair(self):
        return self.__hair

    def set_hair(self, hair: str):
        self.__hair = hair

    def get_job(self):
        return self.__job

    def set_job(self, job: str):
        self.__job = job

    def get_hobbies(self, hobbies: list):
        return self.__hobbies

    def set_hobbies(self, hobbies: list):
        self.__hobbies = hobbies

    def __init__(self, name, age, sex, hobbies, country, job, hair, height):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__hobbies = hobbies
        self.__country = country
        self.__job = job
        self.__hair = hair
        self.__height = height
        print(f"Hello! My name is {self.__name} with {self.__hair} hair. \n"
              f"I'm {self.__age} years old and my height is {self.__height}. \n"
              f"My sex is {self.__sex}. \n"
              f"I'm from {self.__country}. \n"
              f"I'm working as {self.__job}")
        print("My hobbies is")
        for hobby in self.__hobbies:
            print(hobby)

    def __call__(self, username):
        return f'Hello, my name is Zuzie! Nice to meet you, {username}'

    def __str__(self, username, friendname):
        return f'My name is Zuzie, your name is {username}, name of your friend is {friendname}'

    @staticmethod
    def drink(name):
        return f'So, I drunk {name}'

    def travel(self, place):
        return f'I travelled from {self.__country} to the {place}'

    @staticmethod
    def calculate(a, b):
        return f"I'm very smart, so I can calculate sum of given numbers.\n" \
               f"Given numbers is {a} and {b}.\n" \
               f"So, your answer is {a + b} \n"

    @staticmethod
    def sleep(hours):
        return f"Ok, dear, I will sleep for {hours} hours"

    def showhobbies(self):
        print("My hobbies is")
        for hobby in self.__hobbies:
            print(hobby)

        return "Great, that's all"


class Child(Human):
    def __init__(self, name, age, sex, hobbies, country, job, hair, height):
        if age < 16:
            job = "Unemployed"
        super(Child, self).__init__(name, age, sex, hobbies, country, job, hair, height)

    def set_job(self, job: str):
        if self.__age < 16:
            self.__job = "Unemployed"

    def walk(self):
        print(f"{self.get_name()} walked successfully")

    def work(self):
        if self.get_job() == "Unemployed":
            print(f"I'm child, come on.")


if __name__ == "__main__":
    human = Human(name="Zuzie",
                  age=26,
                  sex="Female",
                  hobbies=["Music", "Active leisure", "TikTok"],
                  country="Ukraine",
                  job="Database crasher on production",
                  hair="Blue",
                  height=180)
    print(human.drink("Cola"))
    print(human.travel("Switzerland"))
    print(human.calculate(12, 14))
    print(human.sleep(12))
    print(human.showhobbies())

    child = Child(name="Zizzie",
                  age=13,
                  sex="Male",
                  hobbies=["TikTok", "Active leisure", "Computers"],
                  country="Ukraine",
                  job="Database crasher on production",
                  hair="Yellow",
                  height=156)
    child.walk()
    child.work()
