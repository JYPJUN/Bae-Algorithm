# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }
# 해당 코드의 시간복잡도는 n을 입력받고 i를 n까지 1씩 증가시키는 반복문을 통해
# sum에다가 추가하므로 n이 증가할 때 마다 수행 횟수는 1씩 증가하게 된다.
# 따라서, 상기 코드의 시간 복잡도는 O(n)이 된다.


N = int(input())

print(N)
print(1)