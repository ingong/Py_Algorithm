print(any(range(3)))
cur = 3 
temp = [1, 3, 6, 2]
if any(cur < num for num in temp):
  print('there is bigger number than cur in temp list')