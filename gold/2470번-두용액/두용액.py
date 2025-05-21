#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2470                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2470                           #+#        #+#      #+#     #
#    Solved: 2025/05/21 18:41:35 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 5
# -2 4 -99 -1 98
# """.strip().split()

n = int(input())
A = list(map(int, input().split()))
A.sort()

left = 0
right = n - 1
min_total = float('inf')
result = (0, 0)

while left < right:
    total = A[left] + A[right]
    
    if abs(total) < abs(min_total):
        min_total = total
        result = (A[left], A[right])
    
    if total < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])


