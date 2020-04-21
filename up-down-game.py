import random

number = int(random.random()*100)
choice = 0
count = 0
chance = 10

while 1:
    try:
        print('chance : ', chance-count)
        choice = int(input('enter number  ::'))
        if choice==number:
            print('you win!~')
            break
        elif choice>number:
            print('down')
        elif choice<number:
            print('up')
        count = count + 1
        if count==chance:
            print('your looser!!')
            print('anser is ', number)
            break
    except:
        print('pleace enter only number')


    
