#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10816                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10816                          #+#        #+#      #+#     #
#    Solved: 2025/05/19 17:45:53 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
# """.strip().split()

# 첫째줄 : 상근이가 가지고 있는 숫자 카드의 개수 N
# 둘째줄 : 숫자 카드에 적혀있는 정수
# 셋째줄 : M ????
# 넷째줄 : 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수, 공백으로 구분

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbercards = list(map(int, input().split()))

card_count = dict()

for num in cards:
    card_count[num] = card_count.get(num, 0) + 1

result = []
for number in numbercards:
    result.append(str(card_count.get(number, 0)))    

print(' '.join(result))