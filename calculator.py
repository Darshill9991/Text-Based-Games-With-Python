while True:
#   print(" To square, type 2 in the second number.\n For cubing, type 3 in the second number.\n To square root, type 0.5 in the second number,and type exp")
  operation = input("Different Operation we perform?\n Add for addition,\n Sub for subtraction,\n Div for division,\n Mult for multiplication,\n Is_divisible to see if n1 is divisible by n2,\n Exp for exponentiation\n Type stop to stop.\n").lower()


  if operation == 'stop':
      break

  n1 = input("What is number 1? ")
  n1 =  float(n1)
  n2 = input("What is number 2? ")
  n2 = float(n2)

  if( operation == 'add') :
    print("Sum is", n1+n2)
  elif (operation == 'sub'):
    print('Difference is', n1-n2)
  elif (operation == 'div') :
    print('Quotient is', n1/n2)
  elif (operation == 'mult'):
    print('Product is', n1*n2)
  elif (operation == "is_divisible") :
    if (n1%n2) == 0:
      print("The first number is divisible by the second number.")
    else:
      print('The first number is not divisible by the second number.')
  elif (operation == 'exp'):
    print("n1 to the power of n2 is",n1**n2)
  else:
    print('You entered an operation that is not listed.') 
  print('=====================================')
  



 

