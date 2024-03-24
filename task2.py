codes = [14,15,16,17,18,19,20]
myCode =[]
for n in myCode:
 myCode.append(n)

print(codes)


[n for n in myCode]
print(codes)


addSum = []
num = 0
for c in codes:
  num = num + c

print("The total number of codes: ", num)
addSum.append(num)

oddNums = []

for od in codes:
  if od%2 !=0:
    oddNums.append(od)

print(oddNums)

setCodes = {14,15,16,17,18,19,20}
print(setCodes)

