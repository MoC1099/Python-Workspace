
is_male = False
is_tall = True

# for and you use "and" symbole, for or your use "or" symbole
if is_male and is_tall:
    print("You are a male")
#else-if
elif is_male and not(is_tall):
    print("you are male but not tall")
elif  is_tall and not(is_male):
    print("you are not male but are tall")
else:
    print("You are not a male")


#-------------------------------------------------------------------------------------
# If statemnets in python using comparisons.

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >+num3:
        return num2
    else:
        return num3

print (max_num(300, 2, 1))



