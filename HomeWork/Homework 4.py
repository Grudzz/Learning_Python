print("Welcome to the Voltage Divider")



print("What is the vin?")

vin = int(input())

print("What is the value of R1?")

R1 = int(input())

print("What is the value of R2?")

R2 = int(input())

output = vin*R2/(R1+R2)

print(output)

