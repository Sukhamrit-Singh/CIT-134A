# Sukhamrit Singh
# Recursive Program

# recursive function to calculate the power
def calculate(x, p, v):
    
    # end recursion
    if (p == 0):
    	return v
    
    # recursive call
    return calculate(x, p-1, v * x)
    

# asking user for floating point number
n = input("Please type a floating point number: ")
n = float(n)

# asking user for power
power = input("Please Power: ")
power = int(power)

# calculate the power and print the value
value = calculate(n, power, 1)
print(value)