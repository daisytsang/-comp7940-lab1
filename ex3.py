# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
for i in l:
    for j in range(i+1):
        if i % (j+1) == 0:
            print(j)