import random

s = ['python', 'java', 'kotlin', 'javascript']
w = (random.choice(s))
# print(w)
ans = (len(w) * "-")
print("H A N G M A N\n")
i = 8
while i >= 0:
    print(ans)
    o = input("Input a letter:  ")
    if o in w:
        for j in range(len(w)):
            if o == w[j]:
                ans = ans[:j]+w[j]+ans[j+1:]
    else:
        print("That letter doesn't appear in the word")
    i -= 1
    print()

    if i == 0:
        print()
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")
        break
