a = input().split("-") # -부호를 제외한 나머지를 저장.
res = 0  # 결과값
s = "" # 문자열로 된 숫자 저장
for i in range(len(a)):
    b = 0 # -끼리 나눈 나머지 숫자들은 각각 더해줘야함. 각 구간마다의 합들
    for j in a[i]:
        if j == "+": # +연산자 만나면
            b += int(s) # 그동안 저장한 s의 int형을 b에 더해줌 (lstrip("0")도 있지만 그냥 int로 하는게 더 나음)
            s = "" # s 는 다시 초기화
        else:
            s += j # +만나기전 까진 문자하나하나 저장.
    b += int(s) # 마지막숫자는 더해줌(+를 안만나기 때문에 두번째for문의 if문을 안거침.)
    s = "" # 다시s초기화
    a[i] = b # a[i]를 숫자의 합으로 저장.
    b = 0 # b초기화
res = a[0] # 첫 숫자의 합들
for j in a[1:]: # 나머지 숫자들의 합들은 빼준다.
    res -= j
print(res)