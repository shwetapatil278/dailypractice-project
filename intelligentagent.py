
low, high = 1, 100

print("Think of a number between 1 and 100")

while low <= high:
    guess = (low + high) // 2
    print("Agent guesses:", guess)

    feedback = input("Give feedback: Higher (h), Lower (l), Correct (c): ").lower()

    if feedback == 'c':
        print("Agent guessed the number:", guess)
        break
    elif feedback == 'h':
        low = guess + 1
    elif feedback == 'l':
        high = guess - 1
    else:
        print("Invalid feedback!")
else:
    print("Inconsistent feedback!")
