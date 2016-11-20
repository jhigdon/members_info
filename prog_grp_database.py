"""
started by Albert Sun, 11/20/2016
this is a simple program to obtain and store data about members of the Wilkes Barre Programming Group
using Python 3.5

currently writing list as a JSON txt file.  would like to implement as SQL or use Pandas to analyze
- future implementation?
"""
import json

try:
    with open("member_dat.txt", 'r') as f:
        templist = json.load(f)
except:
    templist = []

print("Database so far: \n")
for x in templist:
    print(x)

loop1 = True

while loop1:
    not_done = True
    while not_done:
        var_dict = {"name":None, "skills":None, "interests":None}
        tempvar = input("Enter your name (type stop or {Enter} to end): ")
        if tempvar == "":
            loop1 = False
            break
        else:
            var_dict["name"] = tempvar
        var_dict["skills"] = input("Enter your skills: ")
        var_dict["interests"] = input("Enter your interests: ")

        if input("{} is this correct? [Enter = Y]: ".format(var_dict)) == "":
            not_done = False
            templist.append(var_dict)
        else:
            print("O.K. Let's try that again.")

print("list so far", templist)

with open("member_dat.txt", 'w') as f:
    json.dump(templist, f)
