n = int(input("팩토리얼 할 값을 넣으세요:\n"))
a = 0
b = 0

if n < 0 :
    print ("불가능합니다")
else :
    while b < n :
        b = b + 1
        a = a + b
    print (a)