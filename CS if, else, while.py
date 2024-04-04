#Morgan Williams
#GPA qualifier
#Determine if you will make the deans lis or honor roll                                   

#Ask student last name
lname = input("Enter the students last name(Enter 'ZZZ' to quit)")

if lname == 'ZZZ':
    print("quit processing student records")

#ask student first name
fname = input("What is your first name.")

#get the gpa
GPA = float(input("What is ypur GPA."))             

if (GPA >= 3.5):
    print("Student has made the Dean's List")

elif(GPA >= 3.25):
    print("Student has made the honor roll.")

else:
    print("You are a good student")