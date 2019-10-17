#%%
import random

#%%
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result
double([2,4,5])

#%%
# exponent will use a for loop to calculate the exponent without the use of the exponent operator (**)
def exponent(number, exponent):
    result = number
    for element in range(1,exponent):
        result = result * number
    return result

exponent(2,3)

#%% Test that it works
for iter in range(5):
    value_1 = random.randint(1,100)
    value_2 = random.randint(2,10)
    result = exponent(value_1,value_2)
    if(result == value_1**value_2):
        print("Success! " + str(value_1) + "^" + str(value_2) + " = " + str(result))

#%%
