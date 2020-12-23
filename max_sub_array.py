def maxSubArray(nums):
    max_values = [0] * (len(nums)+1) # 해당 원소들로 끝나는 연속된 부분 수열들의 최대합 저장 리스트
    # max_result = 0

    idx = 0
    for num in nums:
        idx += 1
        max_values[idx] = num # 자기 자신 원소 하나를 부분 수열로 가지는 케이스

        if max_values[idx] < max_values[idx-1] + num: # 위의 케이스와 나머지 해당 원소로 끝나는 연속 부분 수열 경우의 수들 중 최대합과의 비교
            max_values[idx] = max_values[idx-1] + num # 두 케이스 중 최대값을 산출 및 저장.

        # if idx == 1 or max_result < max_values[idx]:
        #     max_result = max_values[idx]

    return max(max_values[1:]) # 각 원소로 끝나는 연속된 부분 수열의 최대합 중 최대값. 즉 가능한 모든 경우의 부분수열 중 최대값을 구한다.

print(maxSubArray([-1, 4, -2, 6, -10]))