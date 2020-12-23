MAX_VALUE = 100*100000+1            # 최소값 저장을 위한 비교 최대값 ('동전의 최대 개수 * 동전의 최대 가치값' 보다 큰 수)  
n, k = map(int, input().split())    # 동전 개수 n개, 만들어야 하는 가치의 합 k
coin_list = []                      # 동전 종류를 저장하기 위한 리스트
min_cnt = [MAX_VALUE] * (k+1)       # 최소값 (최적해) 저장 리스트
min_cnt[0] = 0                      # 0원 => 0개의 기본값 설정

used_cnt = [[0] * n for _ in range(k+1)] # 사용한 동전 개수 저장 리스트

for _ in range(n):
    coin_list.append(int(input()))

for i in range(1, k+1):                                     # 1부터 k원까지를 만들 수 있는 최소 동전 개수 해를 위한 순회
    for idx, coin in enumerate(coin_list):                  # 동전 순서 idx와 동전 단위 coin
        if i >= coin and min_cnt[i] > 1 + min_cnt[i-coin]:  # 만들어야하는 금액 i원보다 coin이 작거나 같아야만 해당 동전을 사용할 수 있음.
            min_cnt[i] = 1 + min_cnt[i-coin]                #   및 해당 종류의 동전 사용 (1개) + 해당 동전을 제외한 금액(i-coin원)의 최소 동전 개수 중 최소값.
            used_cnt[i] = used_cnt[i-coin][:]               # 해당 동전 제외 금액(i-coin)의 동전 개수 조합을 가져옴.
            used_cnt[i][idx] += 1                           # 사용 동전 개수 반영

if min_cnt[k] == MAX_VALUE: # 초기값이 그대로인 경우, 즉 해당 금액의 가치를 만드는 것이 불가능한 경우일 때.
    print("-1")
else:
    # print(used_cnt[k])
    print(min_cnt[k])