user_age=int(input("enter your age:"))
if user_age<2:
    print("the person is a baby")
elif 2<=user_age<4:
    print("the person is a toddler")
elif 4<=user_age<13:
    print("the person is a kid")
elif 13<=user_age<20:
    print("the person is a teenager")
elif 20<=user_age<65:
    print("the person is an adult")
elif user_age>=65:
    print("the person is an elder")
    
year= int(input("Enter a year:"))
if ( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("the entered number is a Leap Year")
else:
    print("the entered year is not a leap year")
    
cost_price = float(input("enter the cost price:"))
sell_price = float(input("enter the selling price:"))

if (cost_price > sell_price):
    loss= cost_price - sell_price
    print("the seller has made a loss, Amount of loss is: ", loss )
    
elif(sell_price > cost_price):
    profit= sell_price - cost_price
    print("the seller has made profit, Amount of profit is: ", profit)
    
else:
    print("the seller has neither made profit or loss")

if profit <= 50:
    tax= profit*0.02
elif (profit>51 and profit < 100):
    tax= profit*0.04
elif (profit>=100 and  profit<500):
    tax= profit*0.05
else:
    tax= profit*0.07
    
final_amount= profit - tax
print("the amount left after deduction of taxes is: ", final_amount)

    

    