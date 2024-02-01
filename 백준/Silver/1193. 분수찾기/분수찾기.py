N = int(input())

k = 1
while k * (k+1) / 2 < N:
    k += 1

# idx -1 이 index 번호가 됨
a = k-1
idx = int(N - a*(a+1)/2)-1

# 분자는 왼쪽에 있을 때 제일 크고 오른쪽으로 가면 갈수록 작아짐
# 분모는 왼쪽에 있을 때 제일 작고 오른쪽으로 가면 갈수록 작아짐
bunza = [i for i in range(1, k+1)]
bunmo = [j for j in range(1, k+1)]

bunsu = []

if k % 2 == 0:
    # 분자 정순 / 분모 역순
    for k in range(k):
        bunsu.append(f'{bunza[k]}/{bunmo[-k-1]}')
elif k % 2 == 1:
    # 분자 역순 / 분모 정순
    for k in range(k):
        bunsu.append(f'{bunza[-k-1]}/{bunmo[k]}')

print(bunsu[idx])