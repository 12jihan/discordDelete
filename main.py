import pyautogui as pyag
# delete position x=1958, y=440 
# confirm x=2585, y=992
pyag.FAILSAFE = True
print("\n ---- Make sure that your discord app is attached to the right side of your screen\n ---- If things don't work as expected then drag the mouse up to the top left to stop execution of the script")
count = int(input("\n How many times do you want to do this?\n Please enter a number: "))

print(pyag.position())
print(pyag.size())


for i in range(count):
    pyag.PAUSE = 0.4
    pyag.click(1955, 544)
    pyag.click(2585, 992)

print('done!!!!!!!!!!!')