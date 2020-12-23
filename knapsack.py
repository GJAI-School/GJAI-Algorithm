n, k = map(int, input().split())                    # 물건 개수 n개, 배낭 무게 제한 k 
item_info = []                                      # 물건 정보 [무게, 가치]
max_value_list = [[0] * (k+1) for _ in range(n+1)]  # 최대 가치 (최적해) 저장 리스트

for _ in range(n):
    item_info.append(list(map(int, input().split())))

idx = 0
for (weight, value) in item_info:                           # 해당 순회 물건 (weight, value) 까지 고려하는 순회.  
    idx += 1
    for i in range(1, k+1):                                 # 무게 1부터 k까지 안에서 만들 수 있는 최대 가치값 해를 위한 순회
        max_value_list[idx][i] = max_value_list[idx-1][i]   # 직전 idx의 해당 무게에서 최대 가치값, 즉 자기 자신(현재 물건)을 담지 않는 기준에서의 최대 가치값.
        if i >= weight and max_value_list[idx][i] < value + max_value_list[idx-1][i-weight]: # 배낭 무게보다 무거운 물건은 담을 수 없으며, 자기 자신(현재 물건)의 가치와 자기 자신을 제외한 조건에서 차감된 무게 기준의 최대 가치값과의 합을 구하고, 위 줄에서 구한 값과의 대소 비교
            max_value_list[idx][i] = value + max_value_list[idx-1][i-weight] # 이를 통해 최대 가치값을, 현재 무게 안에서 현재 물건까지 고려해 담은 최대 가치값으로 산출 및 저장한다.

print(max_value_list[n][k])