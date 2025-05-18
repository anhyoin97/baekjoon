#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7785                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7785                           #+#        #+#      #+#     #
#    Solved: 2025/05/18 19:01:42 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
input_data = """
4
Baha enter
Askar enter
Baha leave
Artem enter
""".strip().split('\n')

#n = input_data[0]
n = int(input())
office = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        office.add(name)
    else:
        office.remove(name)

for name in sorted(office, reverse=True):
    print(name)


    


