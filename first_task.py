#Initial value
i = 0
print(i)
j = 1
print(j)
k = 0
#Fibonacci number
while k < 100 :
    k = i + j
    print(k)
    i = j
    j = k
