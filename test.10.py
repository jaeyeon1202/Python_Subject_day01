# 3.14 -10.01 0.1
print(3.14, -10.01, 0.1)                      #쉼표
print("%.2f %.2f %.1f" % (3.14, -10.01, 0.1)) #형식지정자
print("{} {} {}".format(3.14, -10.01, 0.1))   #포맷함수

a=3.14
b=-10.01
c=0.1
print(a,b,c)
print("%.2f %.2f %.1f" % (a,b,c))
print("{} {} {}".format(a,b,c))

#포맷함수를 이용해서 출력: format
print("{} {} {}".format(3.14, -10.01, 0.1))
print("{} {} {}".format(a,b,c))