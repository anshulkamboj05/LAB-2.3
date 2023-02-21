# Average of integers
maximum_number = int(input("Enter integer greather then 1): /n "))
total = 0
for i in range(1, maximum_number+1):
    total += i
average = total / maximum_number
print("The average is:", average)
