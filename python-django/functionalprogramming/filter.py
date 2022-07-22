lst=[2,3,4,6,5,8,9]

even=list(filter(lambda n:n%2==0,lst))
print(even)
odd=list(filter(lambda n:n%2!=0,lst))
print(odd)

output=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(output)


