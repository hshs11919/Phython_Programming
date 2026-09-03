#반복문 : for, while

#while 문
#1~10까지 반복 출력
i = 0
while i < 10 :
    i += 1
    print(i)
    if i == 5 :
        break
else : 
    print("End")

nums = [1,3,5,7,9]
target = 2
i = 0
#found  = False

while i <len(nums) :
    if nums[i] == target :
        print(f"{target} Found.")
        found = True
        break
    i +=1
else :
    print(f"{target} Not Found.")

#if found == False :
#    print("Not Found")

# 1~10까지의 합 출력
#sum = 55
i = 1
tot = 0
while i <=10 :
    tot += i
    i +=1
print(f"sum = {tot}")

i = 0
tot = 0
while i <=10 :
    i +=1
    if i % 2== 0:
        tot += i
print(f"sum = {tot}")

i = 0
tot = 0
while i <= 10 :
    i += 1
    if i % 2 == 1:
        continue
    tot += i
    
print(f"sum = {tot}")

