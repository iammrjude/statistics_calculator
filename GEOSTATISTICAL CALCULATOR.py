
from math import *
import numpy
from scipy import stats

print("           WELCOME")
print(" What do you want to calculate ?")
print(" Type 1: to calculate MEAN")
print(" Type 2: to calculate MEDIAN")
print(" Type 3: to calculate VARIANCE")
print(" Type 4: to calculate Standard Deviation")
print(" Type 5: to calculate COVARIANCE")
print(" Type 6: to calculate DETERMINANT OF A MATRIX")
print(" Type 7: to calculate PEARSON'S CORRELATION COEFFICIENT")
print()
choice=int(input("  What is your choice ? : "))
print()

#MEAN
if choice==1:
	list=[]
	print(" This Program Will Calculate the Mean of a Distribution")
	print()
	n=int(input(" How many numbers are in the distribution: "))
	print()
	for i in range(n):
		num=float(input(" Enter first number (or the next number): "))
		list.append(num)
	mean=numpy.mean(list)
	print()
	print(" MEAN = ",mean)

#MEDIAN
if choice==2:
	list=[]
	print(" This Program Will Calculate the Median of a Distribution")
	print()
	print(" The program will arrange the numbers in ascending order and then calculate the MEDIAN")
	print()
	n=int(input(" How many numbers are in the distribution: "))
	print()
	for i in range(n):
		num=float(input(" Enter first number (or the next number): "))
		list.append(num)
	median=numpy.median(list)
	print()
	print(" MEDIAN = ",median)

#VARIANCE
if choice==3:
	list=[]
	print(" This Program Will Calculate the Variance of a Distribution")
	print()
	n=int(input(" How many numbers are in the distribution: "))
	print()
	for i in range(n):
		num=float(input(" Enter first number (or the next number): "))
		list.append(num)
	mean=numpy.mean(list)
	print()
	print(" MEAN =",mean)
	print()
	list2=[]
	for x in list:
		dev_mean=x-mean
		list2.append(dev_mean)
	print(" Deviation from the mean(x-xbar) =",list2)
	print()
	list3=[]
	for i in list2:
		dev_mean_sqrd=i*i
		list3.append(dev_mean_sqrd)
	print(" (x-xbar)^2 =",list3)
	print()
	sum_list3=numpy.sum(list3)
	print(" SUM(x-xbar)^2 =",sum_list3)
	print()
	variance=(sum_list3)/(n-1)
	print(" VARIANCE =",variance)

#SD
if choice==4:
	list=[]
	print(" This Program Will Calculate the Standard Deviation (SD) of a Distribution")
	print()
	n=int(input(" How many numbers are in the distribution: "))
	print()
	for i in range(n):
		num=float(input(" Enter first number (or the next number): "))
		list.append(num)
	mean=numpy.mean(list)
	print()
	print("  Mean =",mean)
	print()
	list2=[]
	for x in list:
		dev_mean=x-mean
		list2.append(dev_mean)
	print("  Deviation from the mean(x-xbar) =",list2)
	print()
	list3=[]
	for i in list2:
		dev_mean_sqrd=i*i
		list3.append(dev_mean_sqrd)
	print("  (x-xbar)^2 =",list3)
	print()
	sum_list3=numpy.sum(list3)
	print("  SUM(x-xbar)^2 =",sum_list3)
	print()
	variance=(sum_list3)/(n-1)
	print("  Variance =",variance)
	SD=sqrt(variance)
	print()
	print("  STANDARD DEVIATION =",SD)

#COVARIANCE
if choice==5:
	list1=[]
	list2=[]
	list3=[]
	a=" This Program Will Calculate the CoVariance of xy"
	b=a.upper()
	print(b)
	print()
	n1=int(input(" How many numbers are in the table for x: "))
	print()
	n2=int(input(" How many numbers are in the table for y: "))
	print()
	if n1!=n2:
		print("Error!! You must have Equal amount of numbers in both tables!! \n\nThe program has ended you have to restart the program")
	elif n1==n2:
		print()
		for i in range(n1):
			num1=float(input(" Enter first number in the table for X (or the next number): "))
			num2=float(input(" Enter first number in the table for Y (or the next number): "))
			num3=num1*num2
			list1.append(num1)
			list2.append(num2)
			list3.append(num3)
		sum_x=numpy.sum(list1)
		sum_y=numpy.sum(list2)
		sum_xy=numpy.sum(list3)
		sum_x_mul_sum_y=sum_x*sum_y
		n_sum_xy=n1*sum_xy
		SS_xy=(n_sum_xy-sum_x_mul_sum_y)/n1
		COV_xy=SS_xy/(n1-1)
		print()
		print("      COVARIANCE =",COV_xy)

# Function to calculate a 2*2 Matrix
def mat_2_2():
	print("FOR A 2*2 MATRIX ; ")
	print()
	if row==2 and column==2:
		R1C1=int(input("Enter the number contained in column 1 of row 1: "))
		R1C2=int(input("Enter the number contained in column 2 of row 1: "))
		R2C1=int(input("Enter the number contained in column 1 of row 2: "))
		R2C2=int(input("Enter the number contained in column 2 of row 2: "))
		Det=str(((R1C1*R2C2)-(R1C2*R2C1)))
		print()
		print("The Determinant is: "+Det)

# Function to calculate a 3*3 matrix
def mat_3_3():
	print()
	print("FOR a 3*3 Matrix ; ")
	print()
	if row==3 and column==3:
		R1C1=int(input("Enter the number contained in column 1 of row 1: "))
		R1C2=int(input("Enter the number contained in column 2 of row 1: "))
		R1C3=int(input("Enter the number contained in column 3 of row 1: "))
		R2C1=int(input("Enter the number contained in column 1 of row 2: "))
		R2C2=int(input("Enter the number contained in column 2 of row 2: "))
		R2C3=int(input("Enter the number contained in column 3 of row 2: "))
		R3C1=int(input("Enter the number contained in column 1 of row 3: "))
		R3C2=int(input("Enter the number contained in column 2 of row 3: "))
		R3C3=int(input("Enter the number contained in column 3 of row 3: "))
		a=int((R2C2*R3C3)-(R2C3*R3C2))
		b=int((R2C1*R3C3)-(R2C3*R3C1))
		c=int((R2C1*R3C2)-(R2C2*R3C1))
		d=int(R1C1*a)
		e=int(R1C2*b)
		f=int(R1C3*c)
		print()
		Det1=str((d-e+f))
		print("The Determinant is: "+Det1)

# Function to start the program		
def start():
	global row
	global column
	print(" This Program will calculate the Determinant of a 2*2 matrix or a 3*3 matrix")
	print()
	row=int(input(" How many rows ? : "))
	print()
	column=int(input(" How many columns ? : "))
	print()
	
# Function that Decides which matrix to calculate		
def condition():
	if row==2 and column==2:
		mat_2_2()
	elif row==3 and column==3:
		mat_3_3()
	else:
		print("This program can only calculate the determinant for a 2*2 matrix or a 3*3 matrix" )
		print("")
		start()
						
#DETERMINANT OF A MATRIX
if choice==6:
	start()
	condition()

#CORRELATION COEFFICINT
if choice==7:
	print(" THIS PROGRAM WILL CALCULATE THE PEARSON'S CORRELATION COEFFICIENT")
	print()
	n1=int(input(" How many numbers are in table X : "))
	print()
	n2=int(input(" How many numbers are in table Y : "))
	if n1!=n2:
		print("Error!! Both Tables Must contain Equal amount of numbers.\n\n The program has Ended. You have to restart the program. ")
	elif n1==n2:
		list1=[]
		list2=[]
		list3=[]
		list4=[]
		list5=[]
		for i in range(n1):
			numX=float(input(" Enter first number in table X (or next number) : "))
			numY=float(input(" Enter first number in table Y (or next number) : "))
			list1.append(numX)
			list2.append(numY)
			numXY=numX*numY
			xx=numX*numX
			yy=numY*numY
			list4.append(xx)
			list5.append(yy)
			list3.append(numXY)
		sumX=numpy.sum(list1)
		sumY=numpy.sum(list2)
		sumx_sumy=sumX*sumY
		sumXY=numpy.sum(list3)
		SS_xy=sumXY-(sumx_sumy/n1)
		sumx_x=numpy.sum(list4)
		sumxsumx=sumX*sumX
		SS_x=sumx_x-(sumxsumx/n1)
		sumy_y=numpy.sum(list5)
		sumy_sumy=sumY*sumY
		SS_y=sumy_y-(sumy_sumy/n1)
		sqr_t=sqrt((SS_x*SS_y))
		CorCo=SS_xy/sqr_t
		print()
		print(" CORRELATION COEFFICIENT (r) = ",CorCo)