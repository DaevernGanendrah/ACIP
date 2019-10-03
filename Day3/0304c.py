#Arbitrary Argument Lists
def cheeseshop(kind, *messages, client="Anonymous", **roles):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for msg in messages: print(msg)
    print("-" * 40)
    for role in roles: print(role, ":", roles[role])
    print("-" * 40)
    print("The client is",client)

cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
