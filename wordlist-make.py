from itertools import combinations

MIN = 2
MAX = 4
WORDS = ""

while 1:
    try:
        line = input()
        WORDS += line + "\n"
    except EOFError:
        break

splitted = WORDS.split( '\n' )

for i in range( MIN, MAX + 1 ):
    combs = combinations(splitted, i)
    ress = [''.join(comb) for comb in combs]
    for res in ress:
        print(res)

