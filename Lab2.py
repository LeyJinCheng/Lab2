def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)

    if(bmi<18.5):
        print("You are Under Weight")
    if(18.5<=bmi<=25.0):
        print("Normal Weight")
    if(bmi>25.0):
        print("You are Over Weight")


    print("The BMI is=" + str(bmi))
calculate_bmi(weight=57, height=1.73)


