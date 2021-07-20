# Test Task for Intersog

class Human:

    """This is the human from TikTok and she can to entertain you"""

    def __init__(self):
        print("Hello, my name is Zuzie, that's Zuzie with a Z! O_O")

    def __call__(self, username):
        print(f"Hello, my name is Zuzie! Nice to meet you, {username}")

    def __str__(self, username, friendname):
        return f'My name is Zuzie, your name is {username}, name of your friend is {friendname}'

h = Human()
h("Kyrylo")
h.__str__("Kyrylo", "Vladyslav")
print(h.__doc__)
