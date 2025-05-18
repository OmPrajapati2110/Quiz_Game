# String concatenation (aka how to put strings together)
#  Suppose we want to create a string that says "subscribe to __________"
youtuber = "Om" # Some string variable

# A few ways to do this
'''
print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}") 

'''

# For Madlibs we will be using the third way because it is the cleanest way for concatenation

adj = input("Adjective: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")

famous_person = input("famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \nI love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)