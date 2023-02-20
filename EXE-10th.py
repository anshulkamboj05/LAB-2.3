print("Average of integers")
N = int(input("enter integer (N>1)= "))
total = 0
for i in range(1, N+1):
    total += i
    print(i,"  ""total: ", total,)
average = total / N
print("The average is:", average)



