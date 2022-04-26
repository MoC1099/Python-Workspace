# exponents in python
print(2**3) #2^3


# writing a function that will do raise to power for us

def raise_to_power(num1, num2):
    x = (num1**num2)
    print (x)

raise_to_power(3, 4)


def resieto_power(base_num, expo_num):
    result = 1
    for i in range(expo_num):
        result = result * base_num
    return result

print(raise_to_power(2, 2))
