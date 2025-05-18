#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2025/05/18 18:43:47 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours
# """.strip().split("\n")

#n = int(input())
n = int(input())

words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

words = list(set(words))
    
words.sort(key=lambda x:(len(x), x))

for word in words:
    print(word)
