# test case
T = int(input())

for tc in range(1, T+1):
    #사이 거리, A 기차 속력, B 기차 속력, 파리 속력
    D, A, B, F = map(int, input().split())
    print(f"#{tc} {F * D / (A + B)}")