import random
isaac = ["cool", "not cool", "sort of cool"]
for i in range(6):
    print("soldship is the best lol")
    cool_factor = random.choice(isaac)

    if cool_factor == "cool":
        print("Isaac is cool")
    elif cool_factor == "uncool":
        print("isaac isn't cool.")
    else:
        print("Isaac is sort of cool.")