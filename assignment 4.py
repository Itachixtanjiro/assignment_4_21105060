#Q 1

print("\n Question 1\n")
n=int(input("Enter the number : "))
def Tower_Of_Hanoi(n, source, to, auxiliry):
    if n == 0:
        return
    Tower_Of_Hanoi(n-1, source, auxiliry, to)
    print(f"Move Disk {n} from {source} to {to}")
    Tower_Of_Hanoi(n-1, auxiliry, to, source)
Tower_Of_Hanoi(n, 'S', 'T', 'Au')
print("")

#Q 2
print("\n Question 2\n")
n = int(input("Enter the number of rows in Pascal's Triangle: "))
print("\n Recursions Method:\n")
def Pascal_Triangle(n, realn=n):
    if n == 0:
        return
    Pascal_Triangle(n-1,realn)
    print('  '*(realn-n), end='')
    entry = 1
    for i in range(1, n+1):
       print(entry, end ='   ')
       entry = entry * (n - i) // i
    print()
Pascal_Triangle(n)
print("\n Loops Method :\n")
for j in range(1, n+1):
    print('  '*(n - j), end='')
    x = 1
    for i in range(1, j+1):
        print(x, end='   ')
    x = x * (j - i) // i
    print()
print("")

#Q 3
print("\n Question 3\n")

a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)
print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Maximum value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

#Q 4
print("\n Question 4 \n")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
        def __del__(self):
            print("Object destroyed")
student1 = Student("Priyanshu", 21105060)
print("Object created")
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")
del student1
print("")


#Q 5
print("\n Question 5 \n")
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __del__(self):
        print(f"Employee {self.name} record deleted")
E1=Employee("Mehak",40000)
E2=Employee("Ashok",50000)
E3=Employee("Viren",60000)
E1.salary=70000
print(f"\n (a) The updated salary of the employee {E1.name} is {E1.salary} \n")
print("\n (b) ", end='')
del(E3) 
print("")

#Q 6
print("\n Question 6 \n")
word=input("Enter the first word: ")
testword=input("\nEnter a new meaningful word to test your friendship: ")
def count_in_dict(word):
    count={}
    list1=list(word)
    n=len(list1)
    for i in range (n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
            return count
if count_in_dict(word) !=count_in_dict(testword):
    print("The letter aren't exact, friendshio is fake!!")
def userinput():
    ans= input("\nDoes the word makes sense?(y or n)\n")
    if ans=='y':
        print("The friends pass the friendship test!!\n\n")
    elif ans=='n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n ")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")        





