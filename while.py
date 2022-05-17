# Write a programe which will break if user enter a number greater then 100
while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats yor have entered a number greater then 100\n")
        break
    else:
        print("Try Again!")
        continue