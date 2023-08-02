weight = int(input("What is your weight in kg(s): "))
height = float(input("What is your Height in m(s): "))
def bmi_calc(weight, height):
    bmi = weight/height**2
    print("Your BMI is ",bmi,"and")
    if bmi > 25:
        print("You are overweight :(")
    elif bmi < 18.5:
        print("You are underweight :(")
    else:
        print("You have a healthy body weight! :)")
bmi_calc(weight, height)
