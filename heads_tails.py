
# Virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random


head_tails = random.randint(0,1)

if head_tails == 0:
    print("Heads")
else:
    print("Tails")