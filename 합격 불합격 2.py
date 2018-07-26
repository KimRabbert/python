t1 = int(input("토익점수 : "))
a = []
s1 = int(input("과목1 점수 : "))
s2 = int(input("과목2 점수 : "))
s3 = int(input("과목3 점수 : "))
n = 0
s4 = (s1 + s2 + s3) / 3
a1 = ""
a2 = ""
a3 = ""

if s1 < 60 :
    a1 = "nonpass"
if s2 < 60 :
    a2 = "nonpass"
if s3 < 60 :
    a3 = "nonpass"

if s4 >= 70 and t1 >= 800 and s1 > 60 and s2 > 60 and s3 > 60 :
    print("합격하셧습니다!")
else:
    if a1 == "nonpass" :
        print("과목 1 낙제입니다 !")
    if a2 == "nonpass" :
        print("과목 2 낙제입니다 !")
    if a3 == "nonpass" :
        print("과목 3 낙제입니다 !")
    print("불합격하셧습니다!")