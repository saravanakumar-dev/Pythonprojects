#1+2+3+4+5+..+n
inp_ran=int(input("Enter the range:"))
ans=0
for i in range(1,inp_ran+1):
ans=ans+int(i)
print (ans)

#1 4 9 16 25
inp_ran=int(input("Enter the range:"))
for i in range(1,inp_ran+1):
print(str(i**2),end=" ")

#1 4 27 16 125
inp_ran=int(input("Enter the range:"))
for i in range(1,inp_ran+1): 
if(i%2!=0): 
print (str(i**3),end=" ") 
else: 
print (str(i**2),end=" ")

# 1 2 3 6 9 18 27 54
e=0;
d=0;
n=int(input("enter"))
for i in range(1,n+1):
 if(i==1):
  print(i,end=" ")
  e=i
 elif(i==2):
  print(i,end=" ")
  d=i
 elif(i%2==0 and i!=2):
  d=d*3
  print(d,end=" ")
 else:
  e=e*3
  print(e,end=" ")
  
# 1 2 9 4 25 6 49
n=int(input("enter"))
for i in range(1,n+1):
 if(i%2==0):
  print(i,end=" ")
 else:
  print(i*i,end=" ")

# 1  5  9  6  25  8   49
e=5
c=1
n=int(input("enter"))
for i in range(1,n+1):
 if(i==2):
   print(e,end=" ")
 elif(i%2==0 and i!=2):
    print(e+c,end=" ")
    e=e+c
    c=c+1
 else:
  print(i*i,end=" ")