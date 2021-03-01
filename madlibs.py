youtuber = "Adeoluwa" #This is how the variable is defined.
# The following are different ways to concatenate
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}") #This (the f-string) is the cleanest way to concatenate for the sake of this madlib.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! You rock 🤘🏾"

print(madlib)

#Project_1