specie = "dog"
age = 6
if specie == "cat":
    if age < 2:
        print("kitten food")
    elif age < 5:
        print("senior cat food")
    else:
        print("Old cat Food")
if specie == "dog":
    if age < 2:
        print("puppy food")
    elif age < 5:
        print("senior dog food")
    else:
        print("Old Dog Food")