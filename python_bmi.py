"""This python calculator calculates your BMI"""

#set variables weight and height and collect user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

#perform BMI calculation
conversion_of_height_cm_to_meters = height / 100
bmi = weight / (conversion_of_height_cm_to_meters ** 2)

#print formatting method may not work in older versions python
print('BMI is: {:.2f}'.format(bmi))
