#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11650                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11650                          #+#        #+#      #+#     #
#    Solved: 2025/05/18 18:25:43 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
# """.strip().split("\n")

#n = int(input_data[0])
n = int(input())
points = []

# for line in input_data[1:]:
#     x, y = map(int, line.split())
#     points.append((x, y))

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    

points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(x, y)

