#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2805                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2805                           #+#        #+#      #+#     #
#    Solved: 2025/05/22 16:11:27 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 4 7
# 20 15 10 17
# """.strip().split()

# input_data = """
# 5 20
# 4 42 40 26 46
# """.strip().split()
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
result = 0 

while left <= right:
    mid = (left + right) // 2 
    total = sum((tree - mid) for tree in trees if tree > mid)
    
    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
    

