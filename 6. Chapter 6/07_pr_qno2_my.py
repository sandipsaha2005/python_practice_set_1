'''Write a  program to find out wheather a student is pass or fail, if it requirs 40%
and least 33% in each subject to pass.Assume 3 subjects and take marks as an input from
the user..'''



# if(sub1<33 or sub2<33 or sub3<33):
#     print("fail")
# elif(sub1+sub2+sub3)/3 <40:
#     print("fail")

# else:
#    print( "you are pass")

# my

sub1=int(input("enter the number\n"))
sub2=int(input("enter the number\n"))
sub3=int(input("enter the number\n"))
if(sub1>=33):
    print("you have passd  the first exam")
else:
    print("you have failed  in the first exam ")
if(sub2>=33):
    print("you have passd the second exam")
else:
    print("you have failed in the second ")
if(sub3>=33):
    print("you have passd the third exam")
else:
    print("you have failed in the third exam")

total=((sub1+sub2+sub3)/3)   # i think it is the average of the total of exams
print(total)
if(total>=40):
    print("you have quilified the exam")
else:
    print("better luck next time")
















