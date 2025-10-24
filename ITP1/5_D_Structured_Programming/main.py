n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        print(f" {i}", end='')
    else:
        x = i
        found_3 = False
    
        while x > 0:
            if x % 10 == 3:
                found_3 = True
                break
            
            x //= 10 
        if found_3:
           print(f" {i}", end='')
print()
