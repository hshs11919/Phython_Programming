#비트 연산자
a=5 #0000 0101
b=3 #0000 0011
print(a&b) # 0000 0001
print(a|b) # 0000 0111
print(a^b) # 0000 0110
print(a<<b) # 5 -> 10 -> 20 -> 40
print(40 >> b) # 40 -> 20 -> 10 -> 5
print(~a) # 1111 1010 -> 0000 0110

#멤버십 연산자
print("a" in "apple")
print(3 in [1,2,3])

#삼항 연산자
# int max = a>b ?a:b; # C 언어 방식

max = a if a > b else b

print("짝수" if a % 2 == 0 else "홀수")
score = 85
#90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 60점 미만이면 F출력
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F")