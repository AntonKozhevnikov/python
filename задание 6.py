n = int(input("введите целое число: "))
s = 0
while n != 0:
    s += n % 10 
    n = n // 10
print("Сумма цифр: ", s)
    
    
        
