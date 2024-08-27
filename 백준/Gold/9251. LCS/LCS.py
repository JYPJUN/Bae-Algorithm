import sys

I = sys.stdin.readline

word1 = I().strip()
word1_len = len(word1)
word2 = I().strip()
word2_len = len(word2)
lcs = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]

for i in range(1, word1_len + 1):
    for j in range(1, word2_len + 1):
        if word1[i - 1] == word2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

result = lcs[word1_len][word2_len]

print(result)
