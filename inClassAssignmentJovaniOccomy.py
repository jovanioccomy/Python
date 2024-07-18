

# In Class Assignment: Jovani Occomy  

#create (gather) inputs for name of employee, employee ID, hourly wage and number of hours worked
name = input('employee name: ')

idNumber = input('employee id: ')

hourlyWage = input('hourly wage: ')

numHoursWorked = input('number of hours worked: ')

 

#convert the variables to numbers to display number of wages and hours worked

hourlyWage = float(hourlyWage)

numHoursWorked = float(numHoursWorked)

 

#calculate the weekly pay by multiplying the hourly wage by number of hours worked

pay = hourlyWage*numHoursWorked

 

#print out the outputs using command 'print'

print('employee name: %s, with ID: %s' % (name,idNumber))

print('they worked %f hours \n' % numHoursWorked)

print('their weekly pay was: %f \n' % pay)