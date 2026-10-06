# 사용자 정의 모듈
print("start2",__name__)
PI = 3.141592653689793238462633832795

def add(a,b) : 
    return a + b

if __name__== "__main__":
    print(PI)
    print(add(10,20))