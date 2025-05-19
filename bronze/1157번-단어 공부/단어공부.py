#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2025/05/19 18:26:16 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# Mississipi
# """.strip().split()

# input_data = """
# zZa
# """.strip().split()

# input_data = """
# baaa
# """.strip().split()

words = input().strip().upper()

words_count = dict()

for i in words:
    words_count[i] = words_count.get(i, 0) + 1

max_count = max(words_count.values())

max_count_word = []

for ch, cnt in words_count.items():
    if cnt == max_count:
        max_count_word.append(ch)

if len(max_count_word) > 1:
    print("?")
else:
    print(max_count_word[0])