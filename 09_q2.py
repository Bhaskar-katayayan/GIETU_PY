c=("choose which u currency u have")
c1=("1. euro")
c2=("2. bp")
c3=("3. ad")
c4=("4. cd")
choose=int(input("1/2/3/4"))
urc=int(input("input urc"))
if choose==1:
    print(0.01417*urc)
elif choose==2:
    print(0.0100*urc)
elif choose==3:
    print(0.02140*urc)
elif choose==4:
    print(0.02027*urc)

#2
# def currencycal(amountinr, curr):
#     if curr=="euro":
#         print(amountinr*0.01417)
#     elif curr=="bP":
#         print(amountinr*0.)
#     elif curr==""