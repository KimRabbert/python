# nubmer가 박수를 쳐야하는 숫자인지, 그냥 숫자로 말해야하는 숫자인지 판단하는 함수입니다.
# 판단해서 박수를 쳐야하는 숫자이면 박수를 쳐야하는 횟수만큼 "짝"을 return 해주고, 아니라면 number를 그대로 return 해줍니다.
def Return_Clap_or_Number(number):
    count_369 = 0
    for i in str(number):
        if int(i)%3 == 0 and i != '0':
            count_369 = count_369 + 1
    
    if count_369 != 0:
        return "짝"*count_369
    else:
        return number

# player 수를 argument로 받아서 player 수만큼 player들의 이름을 입력받아 list로 만들어주는 함수
def Make_playerlist(player_number):
    playerlist = []
    for i in range(1, player_number + 1):
        playerlist.append(input(str(i) + ' 번째 player의 이름을 입력해주세요 : '))
    
    return playerlist

