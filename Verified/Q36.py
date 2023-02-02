def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

f = open("input.txt",'r')
l1=f.readline()
print(string_both_ends(l1))
