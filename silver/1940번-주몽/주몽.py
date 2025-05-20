#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1940                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1940                           #+#        #+#      #+#     #
#    Solved: 2025/05/20 20:10:44 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 6
# 9
# 2 7 4 1 5 3
# """.strip().split()

# n = int(input_data[0])
# m = int(input_data[1])
# clothes = list(map(int, input_data[2:]))

n = int(input())
m = int(input())
clothes = list(map(int, input().split()))

result = set()
count = 0

for num in clothes:
    target = m - num
    
    if target in result:
        count += 1
    result.add(num)
    
print(count)