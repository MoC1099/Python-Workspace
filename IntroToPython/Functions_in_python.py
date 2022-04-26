# we wanna create a funtion that says hi to the user
# def is a key word that tells python that ok the user needs to use the function

def say_hi():
    print("hello user!!")

#now lets call the function
print("Top")
say_hi()
print("Bottom")

# this is the new function that takes parameter
def greetings(name, age):
    print("Hello " + name, "you are", age)
   # print("Hello " + name, "you are", str(age)) same thing here age was given as a int and we convert it into an int

greetings("saad", 12)
greetings("mike", 12)


