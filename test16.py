def full_calculator (a,b,operator):
    if(operator == '+'):
        print('Result:' ,a+b)

    elif(operator == '-'):
        print('Result:' , a-b)

    elif(operator == '*'):
        print('Reslut:', a*b)

    elif(operator == '/'):
        print('Result:', a/b)

    elif(operator == '%'):
        print('Result:', a%b)

    else:
        print('Please enter the parameter properly')

    

full_calculator(7,3,'+')
full_calculator(7,3,'-')
full_calculator(7,3,'*')
full_calculator(7,3,'/')
full_calculator(7,3,'%')