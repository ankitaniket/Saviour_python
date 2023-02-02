def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ng'

  return str1
try:
  f = open("input.txt",'r')
  l1=f.readline()
  print(add_string(l1))
except:
  print("File not Found")
