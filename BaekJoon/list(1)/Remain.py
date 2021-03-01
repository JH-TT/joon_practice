# 3052번 : 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

a = [] # 42로 나누었을 때 나머지를 저장시킬 배열선언.
for _ in range(10):
    num = int(input()) # 정수를 입력받을 때 마다.
    num %= 42  # 42로 나누었을 때 나머지를
    if num not in a: # for문을 돌리면서 a배열에 없으면 append로 넣는다.
        a.append(num)
print(len(a)) # 결국 a배열엔 서로 다른 나머지만 있으니 a배열의 길이가 결국 서로 다른 나머지의 개수 이다.

# 다른 방법.
# not in 으로 판단하지 말고, 나머지들을 전부 배열에 넣고 set을 이용해서 길이를 구한다.(set은 중복을 허락하지 않기 떄문.)