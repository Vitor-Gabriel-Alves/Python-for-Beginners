'''Os comentários estão todos em inglês por motivos óbvios! Traduza caso queira entender melhor o código.'''

''' Create variables to store entered values'''

quest = input("Enter the type of currency you want to convert: ").strip().lower() 

#strip() remove spacing, lower() Leave it lowercase so the code doesn't break.

'''Let's create a condition for the value entered, if the answer is USD, 
we will convert 
dollars to reais, otherwise reais to dollars'''

if quest == "usd":
  value_usd = float(input("Enter the value in USD: "))
  new_value_usd = value_usd / 0.17482517482 #BRL quotation, 2024.
  new_value_usd = round(new_value_usd,2)
  print(f"{value_usd} in BRL {new_value_usd}")#"f" is used to format the string. 
#In this situation the variables must be between {}

elif quest == "brl":
  value_brl = float(input("Enter the value in BRL: "))
  new_value_brl = value_brl / 5.72 #USD quotation 2024
  new_value_brl = round(new_value_brl, 2)#round is used to round values.
  print(f"{value_brl} in USD {new_value_brl}")

else:
  print("only BRL or USD is allowed!")

'''using another IF will result in consuming more memory, as the machine tests them all 
simultaneously. Therefore, in this situation, the use of Elif is recommended.'''
