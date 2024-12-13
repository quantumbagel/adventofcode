import os

options = ["Generate day structure for a year", "Enter examples for a given day", "Add user to a given day"]


for ind, option in enumerate(options):
    print(f"{ind+1}.", option)

num = int(input(":"))

if num == 1:
    year = int(input("Enter year:"))
    if not os.path.exists(str(year)):
        os.mkdir(str(year))
    os.chdir(str(year))
    for i in range(25):
        if not os.path.exists("day"+str(i+1)):
            os.mkdir("day"+str(i+1))
        os.chdir("day"+str(i+1))
        if not os.path.exists("inputs"):
            os.mkdir("inputs")
        os.chdir("..")
# TODO