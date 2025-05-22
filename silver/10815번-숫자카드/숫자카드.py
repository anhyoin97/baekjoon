#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10815                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10815                          #+#        #+#      #+#     #
#    Solved: 2025/05/22 16:01:44 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# input_data = """
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
# """.strip().split()


def binary_search(array, target):
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
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))

results = []

for t in targets:
    if binary_search(cards, t):
        results.append('1')
    else:
        results.append('0')
        
print(' '.join(results))
