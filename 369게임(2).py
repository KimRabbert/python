import SamYugGuPackage
import time
'''

end_number = int(input("몇 번이나 게임을 할까요? : "))
number_of_player = int(input("몇 명이나 게임을 할까요? : "))

for i in range(1, end_number + 1):
    print(i)
'''

end_number = int(input("몇 번이나 게임을 할까요? : "))
number_of_player = int(input("몇 명이나 게임을 할까요? : "))

playerlist = SamYugGuPackage.Make_playerlist(number_of_player)

for i in range(1, end_number + 1):
    player = playerlist[(i - 1) % number_of_player]
    clap_or_number = SamYugGuPackage.Return_Clap_or_Number(i)
    print(player + ' : ' + str(clap_or_number))
    time.sleep(0.3)
