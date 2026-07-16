money = int(input())

banknote_1000 = money // 1000    
remaining_money = money % 1000


banknote_100 = remaining_money // 100   
remaining_money = remaining_money % 100


coin10 = remaining_money // 10
remaining_money = remaining_money % 10

coin1 = remaining_money

print(banknote_1000)
print(banknote_100)
print(coin10)