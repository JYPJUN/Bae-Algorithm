for i in range(10):
    n = int(input())
    building_list = list(map(int, input().split()))
    count_number = 0
 
    for j in range(len(building_list)-2):
        a = building_list[j] - building_list[j-2]
        b = building_list[j] - building_list[j-1]
        c = building_list[j] - building_list[j+2]
        d = building_list[j] - building_list[j+1]
 
        if a > 0 and b > 0 and c > 0 and d > 0:
            count_number += min(a, b, c, d)
 
    print(f'#{i+1} {count_number}')