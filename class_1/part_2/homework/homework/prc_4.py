
def monthday(balance,annualInterestRate,minimum_money,day = 0):
    balance -= minimum_money
    if(balance<=0 or day>12):
        return day
    else:
        return monthday(balance+balance*(annualInterestRate/12),annualInterestRate,minimum_money,day+1)

def paying_debt(balance,annualInterestRate):
    BOL = True
    t = 1
    while BOL:
        minimum_money = t*10
        s = monthday(balance,annualInterestRate,minimum_money)
        if s<12:
            BOL = False
        t+=1
    print('Lowest payment: '+ str(minimum_money))

def paying_debt_2(balance,annualInterestRate):
    BOL = True
    min = balance/12
    max = balance*((1+annualInterestRate/12)**12)/12
    while BOL:
        s = monthday(balance,annualInterestRate,(min+max)/2)
        if s == 11:
            BOL = False
            minimum_money = (min+max)/2
        elif s>11:
            min = (min+max)/2
        else:
            max = (min+max)/2
    print('Lowest payment: '+ str(round(minimum_money,2)))

paying_debt_2(999999,0.18)
