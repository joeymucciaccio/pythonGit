#Joseph Mucciaccio
#This is the input gained from the user
rate_per_hour = float(input("Enter how much you make an hour: "))
hours_worked = float(input("Eneter how many hours you worked this week: "))
yes_no = input("Did you recieve a bonus? (y/n): ")

bonus = 0
overtime_salary = 0
non_overtime_salary = 0

#Getting the users bonus
if yes_no == 'y':
    bonus = float(input("Eneter your bonus: "))

#overtime calculation
if hours_worked > 40:
    overtime_salary += 1.5 * (hours_worked - 40) * rate_per_hour

if hours_worked > 40:
     non_overtime_salary = 40 * rate_per_hour 
else:
     non_overtime_salary = hours_worked * rate_per_hour 

total_salary = overtime_salary + bonus + non_overtime_salary


print("Your bonus is ", bonus)
print("Your Overtime is ", overtime_salary)
print("Your total salary is ", total_salary)