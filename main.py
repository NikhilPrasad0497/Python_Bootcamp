# Tricky Counter

mylist = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in mylist:
  sum +=i
print(sum)


for i in range(10,0,-3):
  print(i**2)

for i,char in enumerate('Hello'):
  print({i,char})


for i,char in enumerate(list(range(100))):
  if char ==50:
    print(f'index of 50 is: {i}')
  else:
    continue
