

#%%
source = open('1342-0.txt')
pride = source.read()
source2 = open('1322-0.txt')
leaves = source2.read()

import re

pride_exclamation = re.findall(r'[A-Za-z0-9]+!', pride)
leaves_exclamation = re.findall(r'[A-Za-z]+!', leaves)
sum = 0
for each in pride_exclamation:
    sum = sum + len(each)
print((float)(sum - len(pride_exclamation))/ len(pride_exclamation))

sum2 = 0
for each in leaves_exclamation:
    sum2 = sum2 + len(each)
print((float)(sum2 - len(leaves_exclamation)) / len(leaves_exclamation))

#%%

import re
def words_exclaimed(x):
    source = open(x)
    origin = source.read()

    string_exclamation = re.findall(r'[A-Za-z0-9]+!', origin)
    sum = 0
    for each in string_exclamation:
        sum = sum + len(each)
    print("The average length of exclaimed words is: ")
    return ((float)(sum - len(string_exclamation)) / len(string_exclamation))

words_exclaimed('219-0.txt')


#%%
