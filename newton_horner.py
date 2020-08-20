# PLEASE READ!
# THIS CODE IS STILL IN DEVELOPMENT
# IT CAN'T FIND THE ROOTS IN ONE GO, IT FINDS ONE ROOT AT A TIME
# THE CODE NEEDS TO BE RUN MANUALLY A FEW TIMES
# DEPENDING ON THE POLYNOMIAL

# at the end of the program a root will be shown
# and a new list which will be our new polynomial
# make sure to insert it in the correspoing places
# which are shown around the code
# WARNING: THE CODE DOESN'T DERIVATE THE FUNCTION



# Please insert your function in func
# and your derivate of the function in the dev function

def func(x):
    Fx = x**4 -6*x**3 -84*x**2 + 214*x + 1155
    return Fx
def dev(x):
    Fx = 4*x**3 -18*x**2 -168*x + 214
    return Fx


# A FUNCTION OF THE NEWTON METHOD
def newton(x):
    for i in range(0,15):
        xn = x - (func(x) / dev(x))
        x = xn
    return xn

# HORNER'S METHOD OR SYNTHETICAL DIVISION
# THE REMAINDER WILL TELL US IF THE RESULT WE GOT FROM THE
# NEWTON METHOD IS A ROOT OR NOT
def horner(coeffs, x):
	acc = 0
	for c in coeffs:
		acc = acc * x + c
	return acc # IT IS A ROOT, IF IT RETURNS A 0

# THIS RETURNS A LIST WHICH IS OUR RESULT FROM THE SYNTHETICAL DIVISION
# DUE TO THE SYNTHETICAL DIVISION OUR POLYNOMIAL GOES DOWN ONE GRADE
def horner_list(coeffs,x):
    acc = 0
    lst = []
    for c in coeffs:
        acc = acc * x + c
        lst.append(acc)
    if lst[-1] == 0:
        lst.pop()
        return lst
    else:
        return lst

guess = 0 #Normally if you want to find negative roots set this to 0 and 1000 for positive roots

# THIS IS WHERE YOU INSERT YOUR NEW LIST(my_fun) GIVEN BY THE LAST RUNNING
# OF THE PROGRAM(IGNORE THE 0 AT THE END OF THE GIVEN LIST)
# OR IF IT'S THE FIRST TIME RUNNING THIS CODE JUST INSERT THE VALUES OF
# YOUR FUNCTION
my_fun = [1,-6,-84,214,1155]
for val in range(0,1):
    print(f"Root at: {newton(guess)}")
    print(f"The result of the synthetic division: {horner_list(my_fun,newton(guess))}")
    new_n = horner(my_fun,newton(guess))
    print(f"The residual of the horners method: {new_n}")
    n = new_n
