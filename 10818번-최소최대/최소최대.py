#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10818                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10818                          #+#        #+#      #+#     #
#    Solved: 2025/05/18 17:52:22 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.stdin = open("./input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))