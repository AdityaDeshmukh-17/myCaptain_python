string = input("Enter string.....")
frequencies={}
  
for char in string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

# Show Output
print ("Per char frequency in {}  is :\n{} ".format(string,str(frequencies)))
 
 