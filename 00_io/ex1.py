# 1. 입출력

a = int(input())
print(a, end="")
print(type(a))
print(a, type(a), sep = " ")

a = int(a) # 정수형 변환 # 함수 호출하는 것과 비슷하다(인자를 넘기는 느낌)
print(a, type(a))

a = int(input())
print(a, type(a))

b = float(input()) # 실수형
print(b, type(b))

# 정수 2개 입력
#100
#200
a = int(input())
b = int(input())
print(a,b)

#100 200
a = input().split()
print(a, type(a))

#map 함수
#map(함수, List객체)
a,b,c = map(int,input().split())
print(a, b, c)

#리스트 변환
a = list(map(int,input().split()))
print(a, type(a))