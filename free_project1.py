
#!/usr/bin/python

# Free Project 7-1: Modify "Stochastic Texts"
# Austin Wentworth
# DIG 5508
# Murray


# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

#%%
from random import choice

subjects = ['STRANGER', 'DARKNESS', 'LIGHT', 'CHICKEN', 'FIEND', 'TRAVELER', 'FREAK', 'CRIMINAL', 'GENIUS', 
              'SLEEP', 'WORLD', 'AMERICA', 'HUMANITY', 'SIR', 'MAAM', 'FANTASY', 'REALITY', 'LOVE', 'HAPPINESS',
              'MISERY', 'AGONY', 'ECSTASY']
adverbs = ['SLOWLY', 'IMMEDIATELY', 'SURELY', 'INEVITABLY', 'URGENTLY', 'SUDDENLY', 'MESSILY', 'PERFECTLY']
verbs = ['MEANS', 'CAUSES', 'PREDATES', 'BEGETS', 'ENDS', 'PROLONGS', 'PREVENTS', 'NECESSITATES']
operators = ['HI', 'HELLO', 'GUTEN TAG', 'HOLA', 'BONJOUR', 'KONICHIWA', 'ALOHA', 'GOODBYE', ]
effect = ['CREATING', 'DESTROYING']

def phrase():
    text = choice(operators) + ' TO ' + choice(subjects)
    return text


print(phrase() + ' ' + choice(verbs) + ' ' + phrase() + ', ' + choice(adverbs) + ' ' + choice(effect)+ ' '+ choice(subjects) + '. ' + choice(operators) + '!')



#%%

#%%
