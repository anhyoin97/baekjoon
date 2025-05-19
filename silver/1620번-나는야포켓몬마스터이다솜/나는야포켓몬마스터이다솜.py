#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1620                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1620                           #+#        #+#      #+#     #
#    Solved: 2025/05/18 19:22:58 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# input_data = """
# 26 5
# Bulbasaur
# Ivysaur
# Venusaur
# Charmander
# Charmeleon
# Charizard
# Squirtle
# Wartortle
# Blastoise
# Caterpie
# Metapod
# Butterfree
# Weedle
# Kakuna
# Beedrill
# Pidgey
# Pidgeotto
# Pidgeot
# Rattata
# Raticate
# Spearow
# Fearow
# Ekans
# Arbok
# Pikachu
# Raichu
# 25
# Raichu
# 3
# Pidgey
# Kakuna
# """.strip().split('\n')

n, m = map(int, input().split())

name_to_num = dict() # 이름 -> 번호
num_to_name = dict() # 번호 -> 이름

# 포켓몬 이름 저장
for i in range(1, n+1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

# 처리
for i in range(n + 1, n + 1 + m):
    query = input().strip()
    if query.isdigit(): # 입력이 숫자일때 이름
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])


# n, m = map(int, input_data[0].split())

# 포켓몬 이름 저장
# for i in range(1, n + 1):
#     name = input_data[i].strip()
#     name_to_num[name] = i
#     num_to_name[i] = name

# 처리
# for i in range(n + 1, n + 1 + m):
#     query = input_data[i].strip()
#     print(query)
#     if query.isdigit(): # 숫자일때 이름 출력
#         print(num_to_name[int(query)])
#     else:
#         print(name_to_num[query])
#     print("=================")