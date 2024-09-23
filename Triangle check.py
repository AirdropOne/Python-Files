num1 = float (input ("First Triangle Side Length"))
num2 = float (input ("Second Triangle Side Length"))
num3 = float (input ("Third Triangle Side Length"))

if num1==num2 and num2==num3 :
    print ("Equalateral")
elif num1==num2 or num2==num3 or num1==num3 :
    print ("Isosceles")
else :
    print ("Scalene")