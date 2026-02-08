from collections import Counter

n = int(input())
sizes = list(map(int , (input().split())))
stock = Counter(sizes)

m = int(input())
total_money = 0

for _ in range(m):
    size,price = map(int,input().split())
    
    if stock[size]>0:
        total_money+=price
        stock[size] -=1
        
print(total_money)
