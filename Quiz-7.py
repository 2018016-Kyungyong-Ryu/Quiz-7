a = int(input("트리의 높이를 입력하세요: "))

for i in range(a+1):
    print(" " * ((a+1)-i) + "*" * (2*i -1))
