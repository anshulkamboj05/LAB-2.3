#CODE WITH ERRORS#
# some_number = 0
# i = 1
# while i < 11:
# 	some_number += 1
#     for
# print(some_number)

#ANSWERS#
#(a) ERRORS IN ABOVE CODE#

# 1. "While" loop should be lowercase as "while".
#
# 2. A colon(:)is missing at the end of while statement.
#
# 3. The += operator is  used to add the value of i to "Some_number", not to add 1 to it.
#
# 4. The "Print" statement should be lowercase "print" in Python.
#
# 5. There is no incrimation of variable "i" without this loop will not work.



#(b) CODE WITHOUT ERRORS#

some_number = 0
i = 1
while i < 11:
    some_number += i
    i+= 1
print(some_number)
