a = str(input("숫자를 넣으세요 : "))
b = int(a)
n = 0
c = b
d = 0
x = 0
i = []
j = []

while c >= 10 :
    c = c // 10
    d = d + 1

while n < b :
    n = n + 1
    m = str(n)
    i.append(m)
    j.append(n)
n = 0

while n < b :
    n = n + 1
    m = str(n % 10)
    l = str(n)
    j[n - 1] = j[n - 1] // 10
    if "3" in l or "6" in l or "9" in l :
        i[n - 1] = ("")
    if "3" in m or "6" in m or "9" in m :
        i[n - 1] = ("짝")
n = 0

if b >= 10 :
    while x < d :
        x = x + 1
        while n < b :
            n = n + 1
            m = str(j[n - 1])
            if "3" in m or "6" in m or "9" in m :
                i[n - 1] = i[n - 1] + ("짝")
            j[n - 1] = j[n - 1] // 10
        n = 0
print(i)