n = int(input())

numbers = list(map(int, input().split()))

numbers.reverse()

str_numbers = list(map(str, numbers))

print(" ".join(str_numbers))