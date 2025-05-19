#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: hyoin1105 <boj.kr/u/hyoin1105>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2025/05/17 18:39:16 by hyoin1105     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
line = input()

parts = line.split()

n = int(parts[0])
k = int(parts[1])

coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

count = 0
used = 0

for coin in coins:
    if k == 0:
        break 
    
    if k >= coin: 
        used = k // coin 
        count += used 
        k -= coin * used 

print(count)
    


