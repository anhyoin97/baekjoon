#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1253                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1253                           #+#        #+#      #+#     #
#    Solved: 2025/05/20 22:08:58 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# input_data = """
# 3
# 3 1 2
# """.strip().split()

# n = int(input_data[0])
# A = list(map(int, input_data[1:]))
n = int(input())
A = list(map(int, input().split()))
A.sort() 

count = 0

for i in range(n):
    target = A[i]
    left = 0
    right = n - 1 
    
    while left < right:
        if left == i:
            left += 1
            continue
        
        if right == i:
            right -= 1
            continue
        
        total = A[left] + A[right] 
        
        if total == target:
            count += 1
            break
        
        elif total < target:
            left += 1
        
        else:
            right -= 1
        
print(count)
    
    
        

