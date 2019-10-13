
#!/usr/bin/python

# Free Project 7-1: Modify "Stochastic Texts"
#   I have modified the original program so that it tells of a greeting to one subject
#   will have some effect on a greeting or farewell of another subject, and the effect 
#   that it will have on another thing, ending with a final greeting. However, if 'hell'
#   is mentioned at all, the sentence stops and prints the next sentence. Similarly,
#   if the word 'damns' is printed for the verbs, it will reduce the counter. When
#   five "damns" are printed, the function stops.
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

subjects = ['HELL', 'STRANGER', 'DARKNESS', 'LIGHT', 'CHICKEN', 'FIEND', 'TRAVELER', 'FREAK', 'CRIMINALS', 'GENIUS', 
              'SLEEP', 'WORLD', 'AMERICA', 'HUMANITY', 'SIR', 'MAAM', 'FANTASY', 'REALITY', 'LOVE', 'HAPPINESS',
              'MISERY', 'AGONY', 'ECSTASY']
adverbs = ['SLOWLY', 'IMMEDIATELY', 'SURELY', 'INEVITABLY', 'URGENTLY', 'SUDDENLY', 'MESSILY', 'PERFECTLY']
verbs = ['MEANS', 'CAUSES', 'PREDATES', 'BEGETS', 'ENDS', 'PROLONGS', 'PREVENTS', 'NECESSITATES', 'DAMNS']
operators = ['HI', 'GUTEN TAG', 'HOLA', 'BONJOUR', 'KONICHIWA', 'ALOHA', 'GOODBYE', ]
effect = ['CREATING', 'DESTROYING']

def phrase_iterations():
    p = 5
    while(p > 0):
        text = choice(operators) + ' TO ' + choice(subjects)
        if 'HELL' in text:
            text = text + '.'
        else:
            text = text + ' ' + choice(verbs) + ' ' + choice(operators) + ' TO ' + choice(subjects)
            if 'HELL' in text:
                text = text + '.'
            else:
                text = text + ', ' + choice(adverbs) + ' ' + choice(effect) + ' ' + choice(subjects)
                if 'HELL' in text:
                    text = text + '.'
                else:
                    text = text + '. ' + choice(operators) + '!'
        print text
        if 'DAMNS' in text:
            p = p - 1
    return text

phrase_iterations()
#%%

#%%
