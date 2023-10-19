def face (n):
   if(n==1):
      return 1
    else:
      return n*face(n-1)
n=int(input/"Enter the n value ")
print (face(n))