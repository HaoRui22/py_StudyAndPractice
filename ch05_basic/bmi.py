print("请输入体重(kg):")
weight = float(input())
print("请输入身高(cm):")
height = float(input())
height = height/100
#weight = 85.0
#height = 1.90
#height = float(input())
bmi = weight / (height * height)
print("您的BMI指数是: %.2f" % bmi)
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24:
    print("体重正常")
elif 24 <= bmi < 28:
    print("体重过重")
else:
    print("肥胖")

