#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10814                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10814                          #+#        #+#      #+#     #
#    Solved: 2025/05/18 18:14:03 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.stdin = open("./input.txt", "r")

n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
