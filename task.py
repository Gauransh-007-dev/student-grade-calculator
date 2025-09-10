print("==============================Student Grade Calculator=========================================")

sub1=int(input("enter marks of subject 1:"))
sub2=int(input("enter marks of subject 2:"))
sub3=int(input("enter marks of subject 3:"))
sub4=int(input("enter marks of subject 4:"))
sub5=int(input("enter marks of subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("The total marks of 5 subjects are",total)
print("The average marks of 5 subjects are",avg)
if avg>=90 :
    print("You have secured grade A")
if avg>=75 :
    print("You have secured grade B")
if avg>=50 :
    print("You have secured grade C")
if avg<50 :
    print("You have secured grade F")
