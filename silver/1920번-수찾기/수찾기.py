#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2025/05/22 15:41:34 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# """.strip().split()

def search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

n = int(input())
A = list(map(int, input().split()))
A.sort() # 1 2 3 4 5
m = int(input())
targets = list(map(int, input().split())) # 1 3 7 9 5

for t in targets:
    if search(A, t):        
        print(1)
    else:
        print(0)
    

