#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1546                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1546                           #+#        #+#      #+#     #
#    Solved: 2025/05/18 17:37:31 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.stdin = open("./input.txt", "r")

n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
new_scores = []

for score in scores:
    new_score = (score / max_score * 100)
    new_scores.append(new_score)

average = sum(new_scores) / n
print(average)