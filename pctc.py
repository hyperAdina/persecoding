#round 1 demo 1: 
string1 = input()
string2 = input()
print(string1+" "+string2)

#round 1 demo 2
n = int(input())
x = int(input())
if n>x:
    print(n-x)
elif x>n:
    print(x-n)
    
#round 1 demo 3
string = input()
n=int(30/len(string))+1
string2=string*n
print(string2)

#round 1 demo 4
numberChoice = int(input())
if numberChoice>50:
     print("yes dream big")
else:
     print("on the small side")
   
#round 1 demo 5
n = int(input())
k = input()
x = int(input())
if (k=="*"):
    print(n*x)
elif (k=="+"):
    print(n+x)
  
#round 1 demo 6
names = []
for i in range(5):
    names.append(input())
position = names.index("Ellie") + 1
if position == 1:
    print("1st")
elif position == 2:
    print("2nd")
elif position == 3:
    print("3rd")
elif position == 4:
    print("4th")
else:
    print("5th")
    
