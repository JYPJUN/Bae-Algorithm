N = int(input())
words = input()
numbers = 0

for i in range(len(words)):
    numbers += ((ord(words[i])-96) * (31**i))

print(numbers % 1234567891)