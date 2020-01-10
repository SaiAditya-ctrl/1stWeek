s=input('if you want to enter tem in farenheit press F otherwise press C')
if(s=='c'):
    c1=int(input('enter the temperature in centigrade'))
    print('the farenheit value is', c1*(9/5)+32)
else:
    f1=int(input('enter the temperature in fareheit'))
    print('the farenheit value is', (f1-32)*(5/9))
