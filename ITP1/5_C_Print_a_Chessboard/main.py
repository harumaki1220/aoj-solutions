while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for n in range(H):
        for m in range(W):
            if (n + m) % 2 == 0:
                print('#',end='')
            else:
                print('.', end='')
        print()
    print()