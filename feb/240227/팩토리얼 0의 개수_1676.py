'''
소인수 분해 해서 2와  5가 몇개있는지 파악 후 2와 5중 적은 수만큼 나올듯
근데 애초에 n!이니깐 무조건 5가 더 작겠네 5의 배수 갯수만 찾으면 될듯
아니다 5가 몇개나오는지 찾아야 할듯 25 이런건 5가 2개니깐
'''

n = int(input())

# 5의 배수 나오면 1개씩 추가
total = n // 5

# 25의 배수 나오면 거기서 1개씩 또 추가
total += n // 25

# 125의 배수 나오면 거기서 또 1개씩 추가
total += n // 125

print(total)

'''
아래 처럼 푸는게 더 똑똑하네
'''
# n = int(input())
#
# count = 0
# # 5의 배수들의 개수 세기
# while n >= 5:
#     count += n // 5
#     n //= 5
#
# print(count)
