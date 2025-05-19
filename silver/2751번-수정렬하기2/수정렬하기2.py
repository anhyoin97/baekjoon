#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2751                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2751                           #+#        #+#      #+#     #
#    Solved: 2025/05/18 18:02:01 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.stdin = open("./input.txt", "r")

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

nums.sort()

for num in nums:
    print(num)