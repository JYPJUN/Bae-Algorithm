import sys

def solution(s, lst):
    if s == len(arr):
        if len(lst) == 6:
            print(*lst)
        return

    solution(s+1, lst+[arr[s]])
    solution(s+1, lst)


while True:
    k, *arr = map(int, sys.stdin.readline().split())
    if k == 0:
        break

    solution(0, [])
    print()