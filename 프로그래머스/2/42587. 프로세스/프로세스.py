
def solution(priorities, location):
    from collections import deque
    prior = [[priorities[i], i] for i in range(len(priorities))]
    prior.append([0, 0])
    que = deque(prior)
    answer = 0
    while True:
        k = que.popleft()
        if k[0] >= max(que)[0]:
            answer += 1
            if k[1] == location:
                break
        else:
            que.append(k)
    
    return answer