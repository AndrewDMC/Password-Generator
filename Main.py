from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random as rnd
import tkinter as tk

Checks = {
    'UpperCase': [None, ascii_uppercase],
    'LowerCase': [None, ascii_lowercase],
    'Symbol': [None, punctuation],
    'Number': [None, digits]
}

PASSWORDLENGTH = 69
NUMPASSWORDS = 3

def getChecks(checks):
    checks2 = Checks.copy()
    for c,key in enumerate(checks2):
        checks2[key][0] = checks[c]
    return checks2

def PasswordGenerator(checks):
    checks = getChecks(checks)
    pws = []

    AllChoice = ""

    for i in checks:
        if checks[i][0] == True:
            AllChoice += checks[i][1]

    for i in range(NUMPASSWORDS):
        pws.append("".join(rnd.choice(AllChoice) for _ in range(PASSWORDLENGTH)))

    return pws

# Example
if __name__ == "__main__":

    MINGENERATE = 1
    MAXGENERATE = 5

    rndMax = rnd.randrange(
        MINGENERATE,
        MAXGENERATE + 1,
    )

    for idx in range(rndMax):
        checks = [
            rnd.getrandbits(1) for _ in range(4)
        ]

        if not any(checks): # Checks if all checks are false, then a random one is set to true
            checks[rnd.randrange(4)] = True

        pws = PasswordGenerator(checks)
        for c,pw in enumerate(pws):
            print(f'({ idx+1 }/{ rndMax }) Password n.{ c+1 }: { pw }')

        if idx < rndMax - 1:
            print()
