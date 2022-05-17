sub1 = int(input("Enter Subject1 marks:\n"))
sub2 = int(input("Enter Subject2 marks:\n"))
sub3 = int(input("Enter Subject3 marks:\n"))

percentage = ((sub1+sub2+sub3)*100)/300

if percentage>=70:
    print("Grade A")
elif percentage>=60 and percentage<70:
    print("Grade B")
elif percentage>=50 and percentage<60:
    print("Grade C")
elif percentage>=40 and percentage<50:
    print("Grade D")
elif percentage<40:
    print("Grade F")
else:
    print("Please type it currect")