# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 위 코드의 시간복잡도는 for문의 이중 반복문을 통해 결정된다.
# sum에 i와 j가 순회하면서 곱하고 sum에 합치는 방식이므로 i가 1 부터 시작한다면 j가 1부터 n까지 반복되고
# 그 다음 i가 2로 시작해서 j가 1부터 n까지 반복되는 형식으로
# 시간복잡도는 O(n^2)이 된다.

N = int(input())

print(N**2)
print(2)