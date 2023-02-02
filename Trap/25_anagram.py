from collections import Counter 

def anagramoftwonumber(p1,p2): 

   bno1 = bin(p1)[2:] 
   bno2 = bin(p2)[2:] 
  
   # append zeros in shorter string 
   zeros = abs(len(bno1)-len(bno2)) 
   if (len(bno1)>len(bno2)): 
      bno2 = zeros * '0' + bno2 
   else: 
      bno1 = zeros * '0' + bno1 
  
   # convert binary representations  
   # into dictionary 
   dict1 = Counter(bno1) 
   dict2 = Counter(bno2) 
  
   # compare both dictionaries 
   if dict1 == dict2: 
      print(p1, p2 ,"are two anagram number") 
   else: 
      print(p1 , p2 ,"are not anagram number") 
  
# Driver program 
if __name__ == "__main__": 
   n1 = int(input("Enter First number ::>"))
   n2 = int(input("Enter Second number ::>"))
   anagramoftwonumber(n1,n2) 