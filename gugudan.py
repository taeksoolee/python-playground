num1 = 0
num2 = 0

print("""
hello. this is gugudan program!
*^ v ^*
""")

while 1:
    try:
        num1 = int(input("please, enter the number1(1~9)"))
    except:
        print('please input only number')
        continue
    if num1>0 and num1<10:
        break
    print("you wrong")

while 1:
    try:
        num2 = int(input("please, enter the number2(1~9)"))
    except:
        print('please input only number')
        continue
    if num2>0 and num2<10:
        break
    print("you wrong")

for i in range(1, num1+1):
    for j in range(1, num2+1):
        print(i," + ",j," = ",i*j)
    print('='*10)

print('bye bye')



