#AVERAGE AND GRADE CALCULATOR

print("enter scores of 5 subjects:")
total=float(0)
score = []
grade = [] 
for i in range (5):
    x=int(input("enter no. \n")) 
    score.insert(i,x)
    i+=1
    total=total+x
    if x>=90:
        grade.insert(i,'A')
    elif x<90 and x>=80:
        grade.insert(i,'B')
    elif x<80 and x>=70:
        grade.insert(i,'C')
    elif x<70 and x>=60:
        grade.insert(i,'D')
    else:
        grade.insert(i,'F')

avg=total/5
print("the average score is: ",avg)

if avg>=90:
    gradeFinal='A'
elif avg<90 and avg>=80:
    gradeFinal='B'
elif avg<80 and avg>=70:
    gradeFinal='C'
elif avg<70 and avg>=60:
    gradeFinal='D'
else:
    gradeFinal='F'


print("the average score is: ",avg,"the final grade is: ",gradeFinal);        
