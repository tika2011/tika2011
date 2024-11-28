#day 20
#2)შემქმენით სია და გადაუარეთ for loop ით, (ინდექსით გამოძახებისას რიგის ნიმრის მაგივრად საიტერეაციო 
# ცვლადი ჩაწერეთ - i) და ეკრანზე გამოიტანეთ ყველა სიის ელემენტი
#3) .append ფუნქციის გამოყენებით დაამატეთ 2 ლემენტი სიას და გამოიტანეთ, კომენტარებით ახსენით როგორ მუშაობს ეს ფუნქცია
#4)შექმენით სია და for loop ით გადაუარეთ და ყოველი საიტერაციო ცვლადის მნიშვნელობა ჩაამატეთ სიას. ( მაგ. ls.append(i) )


#homework1
Corners_of_Georgia= ["Batumi","Qutaisi", "afxazeTi","Svaneti","racha","samegrelo","kaxeti","Qartli","Xevsureti","Samcxe- javaxeti","guria"]
print(len(Corners_of_Georgia))
print(Corners_of_Georgia[0])
print(Corners_of_Georgia[1])
print(Corners_of_Georgia[2])
print(Corners_of_Georgia[3])
print(Corners_of_Georgia[4])
print(Corners_of_Georgia[5])
print(Corners_of_Georgia[6])
print(Corners_of_Georgia[7])
print(Corners_of_Georgia[8])
print(Corners_of_Georgia[9])
print(Corners_of_Georgia[10])

#homework2
ls1=["blue","pink","black","red","green"]
print(ls1[4])
#homework3
ls1=[]
ls1.append("animal")
ls1.append("flower")
print(ls1)
#homework4
Corners_of_Georgia= ["Batumi","Qutaisi", "afxazeTi","Svaneti","racha","samegrelo","kaxeti","Qartli","Xevsureti","Samcxe- javaxeti","guria"]
ls1=[]
for i in Corners_of_Georgia:
    ls1.append(i)
print(ls1)



