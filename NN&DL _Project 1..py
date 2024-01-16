#QUE1

input_string= list(input("Enter the word : "))
if len(input_string) >= 2:
    del input_string[:2]
resultant_string = input_string[::-1]
print("Sample output:")
print("".join(resultant_string))

#QUE 1-1

num1= int(input("enter 1st number \n"))
num2= int(input("enter 2st number \n"))
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
pow = num1 ** num2
print ("sum: ", sum)
print ("difference : ",diff)
print ("product : ",prod)
print ("num1 power num2 : ",pow)


# QUE 2

ipstring = str(input("enter a sentence\n"))
opstring = ipstring.replace("i love playing with python","i love playing with pythons")
print(opstring)

#QUE3

classScore = int(input("enter class score\n"))
if((classScore >=90) and (classScore <100)):
    print("GRADE A")
elif((classScore >=80) and (classScore <89)) :
    print("GRADE B")
elif((classScore >=70) and (classScore <79)) :
    print("GRADE C")
elif((classScore >=60) and (classScore <69)) :
    print("GRADE D")
elif((classScore >=0) and (classScore <60)) :
    print("Grade F")
else:
    print("INVALID INPUT")
