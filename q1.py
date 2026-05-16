while 'true':
    chooies=int(input('enter the chooies'))
    match chooies:
        case 1:
            design=['*'],['**'],['***'],['****']
            for i in design:
                for b in i:
                    print(b)
        case 2:
            print(f"enter the start of the range:10")
            print(f"enter the end of the renge:15")
            for a in range(10,16):
             if a%2==0:
                print(f'number is {a} even')
             elif a%2==1:
                 print(f'number is {a} odd')
                 
            
        case 3:
            print('exiting the program.Goodby!')
            break
            
        
            
            
            




