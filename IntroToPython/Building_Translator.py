# In this example we will be translating/ converting all the vowels into letter "g"
vowels = "AEIOUaeiou"
def translator(str):
    # use for loop and interate through teh string
    new_string = ""
    for i in str:
        if i.lower() in vowels:
            if i.isupper():
                new_string = new_string + "G"
            else:
                new_string = new_string + "g"
        else:
            new_string = new_string + i
    return new_string

print(translator(input("Enter a word: ")))