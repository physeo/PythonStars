print("1: *")
print("2: **")
print("3: ***")
print("4: ****")
print("5: *****")
print("6: ******")
print("7: *******")
print("8: ********")
print("9: *********")
print("10: **********")

myStars = ''
numberOfLoops = 0
for i in range(numberOfLoops):
    myStars = myStars + '*'
    line = str(i) + ": " + myStars
    print(line)

myStars = ''
numberOfLoops = 0
for i in range(numberOfLoops):
    if i <= numberOfLoops / 3:
        myStars = myStars + '*'
    else:
        myStars = myStars[0:len(myStars) - 1]
    line = str(i) + ": " + myStars
    print(line)

myStars = ''
numberOfLoops = 100
invert = False
for i in range(numberOfLoops):
    if i > 0 and i % 10 == 0:
        invert = not invert

    if invert:
        myStars = myStars[0:len(myStars) - 1]
    else:
        myStars = myStars + '*'

    line = str(i) + ": " + myStars
    print(line)
