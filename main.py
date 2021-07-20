# Test Task for Intersog

class Human:

    """This is the human from TikTok and she can entertain you.
    Available methods:
    1. drink
    2. travel
    3. sum calculate
    4. sleep
    5. show hobbies"""
    age = 28
    sex = "F"
    hobbies = ["Music", "Cinema", "Active leisure"]
    country = "Ukraine"
    job = "TikTok Bloger"
    hair = "Blue"
    height = 168

    @classmethod
    def __init__(cls):
        print(f"Hello, my name is Zuzie, that's Zuzie with a Z! I'm {cls.age} years old")

    def __call__(self, username):
        return f'Hello, my name is Zuzie! Nice to meet you, {username}'

    def __str__(self, username, friendname):
        return f'My name is Zuzie, your name is {username}, name of your friend is {friendname}'

    @staticmethod
    def drink(name):
        return f'So, I drunk {name}'

    @classmethod
    def travel(cls, place):
        return f'I travelled from {cls.country} to the {place}'

    @staticmethod
    def calculate(a, b):
        return f"I'm very smart, so I can calculate sum of given numbers.\n" \
               f"Given numbers is {a} and {b}.\n" \
               f"So, your answer is {a + b} \n"

    @staticmethod
    def sleep(hours):
        return f"Ok, dear, I will sleep for {hours} hours"

    @classmethod
    def showhobbies(cls):
        print("My hobbies is")
        for hobby in cls.hobbies:
            print(hobby)

        return "Great, that's all"