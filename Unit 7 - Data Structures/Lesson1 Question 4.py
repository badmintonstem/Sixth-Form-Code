from random import randint
outletSales = [[randint(0,25) for i in range(4)] for j in range(50)]
total = [0 for i in range(4)]
#print(outletSales)
for quarter in range (4):
    for outlet in range(len(outletSales)):
        total[quarter] = total[quarter] + outletSales[outlet][quarter]
    print(f'Total sales for quarter {quarter+1}: £{total[quarter]}')
