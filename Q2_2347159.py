"""
1. LIST
Write a PYTHON script with List comprehension for the following
• Is the given list divisible by 3 or NOT?
• Square of even numbers in a list
• Sum of digits of all EVEN numbers in a list
• Remove duplicate numbers in a list

"""
Age_Of_employee = [x for x in range(27,51)]


for x in Age_Of_employee:
    if x%3 != 0:
        print("THE LIST IS NOT DIVISIBLE BY 3")
        break

print("Sqaure of even numbers")
for x in Age_Of_employee:
    if x%2 ==0:
        print( f"square of {x} = {x**2}")

 
sum = 0

for x in Age_Of_employee:

    if x%2 ==0:
        sum += x
print(f"Sum of even numbers = {sum}")

Age_Of_employee = [22,33,44,44,56,65,51,59,59]

unique_elements = []

for x in Age_Of_employee:
    if x not in unique_elements:
        unique_elements.append(x)

print(unique_elements)



"""

Create a dictionary to store the details of your company employees (name as key and
birthdate as value).
{ ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
Write a function birthDate() that takes the full name of your employees(as a string) and
displays the given employee’s birthdate.
>>>birthDate(‘Rohit Sharma’)
‘30 April 1987’

"""


Employee_in_a_educationDept = {'Ravi':'5 October 1995',
                            'Vishnu' : '2 December 2001',
                            'Karthik' : '4 March 2000',
                            'Divya': '5 June 1995',
                            'Bhanu' : '7 September 2001'}


def birthDate(full_name):
    print(Employee_in_a_educationDept[full_name])

birthDate('Ravi')
birthDate('Divya')