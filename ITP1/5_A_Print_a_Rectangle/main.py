while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for n in range(H):
        for m in range(W):
            print('#', end='')
        print()
    print()