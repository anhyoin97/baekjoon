#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10871                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10871                          #+#        #+#      #+#     #
#    Solved: 2025/05/18 17:57:25 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.stdin = open("./input.txt", "r")

n, x = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
    if num < x:
        print(num, end=' ')
    