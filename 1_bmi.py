weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
conversion_of_height_cm_to_meters = height / 100
bmi = weight / (conversion_of_height_cm_to_meters ** 2)
print('BMI is: {:.2f}'.format(bmi))