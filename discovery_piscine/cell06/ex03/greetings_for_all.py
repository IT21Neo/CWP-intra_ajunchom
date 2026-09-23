def greetings(name="noble stranger"):
    if isinstance(name, str):
        print("Hello, {}.".format(name))
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)