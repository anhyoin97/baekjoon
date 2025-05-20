#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3273                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3273                           #+#        #+#      #+#     #
#    Solved: 2025/05/20 19:45:33 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 7
# 5 12 7 10 9 1 2 
# 11
# """.strip().split()

#n = int(input_data[0])
#m = list(map(int, input_data[1:1+n]))
#x = int(input_data[1+n])

n = int(input())
m = list(map(int, input().split()))
x = int(input())

integer = set()
count = 0

for num in m:
    target = x - num 
    
    if target in integer: 
        count += 1
        
    integer.add(num)

print(count)
    