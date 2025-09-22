valasz = 0
valasz = valasz+1
kutyak = {
    'neve' : '' ,
    'fajta' :'' 
    ,'kora' : ''
    ,'oltas': ''
}

if valasz != 0:
    kutya = input("add meg a kutya nevét:")
    if valasz !='':
        kutyak['neve']= kutya
        print('kutya neve',kutyak['neve'])

if valasz!=0:
    kutya2 = int(input("add meg a kutya korát:"))
    if valasz !='':
        kutyak['kora'] = kutya2
        print('kutya kora',kutya2)

if valasz !=0:
    kutya3 = input("add meg a kutya fajtajat:")
    if valasz !='':
        kutyak['fajta'] = kutya3
        print('kutya fajtaja',kutya3)

if valasz !=0:
    kutya4 = input("add meg hogy a kutya rendelkezik e oltással:")
    if valasz !='Igen':
        kutyak['oltas'] = kutya4
        print('bevan oltva',kutya4)
    else:
        print("nem rendelkezik")
        
print(kutyak)


