#Level 18
#1. ლუწი ან კენტი-დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს და ამოწმებს
#  ლუწია თუ კენტი პირობითი განცხადებების გამოყენებით.
#2. ხმის მიცემის მარტივი უფლება-
#შექმენით პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და ეუბნება, აქვს თუ არა ხმის მიცემის უფლება (18 წლის ან უფროსი).
#3. ტემპერატურის შემოწმება
#დაწერეთ პროგრამა, რომელიც გაზომავს ტემპერატურას ცელსიუს გრადუსებში და ბეჭდავს არის თუ არა ის „ცივი“ (15°C-ზე ქვემოთ), 
# „თბილი“ (15°C-დან 25°C-მდე) თუ „ცხელი“ (25°C-ზე მეტი).
#4. პაროლი
#შექმენით პროგრამა, რომელიც მომხმარებელს პაროლს სთხოვს. თუ პაროლი არის წინასწარ განსაზღვრული (მაგ. "python123"),
#  დაუპრინტეთ "Access Granted", წინააღმდეგ შემთხვევაში  "Access Denied".

# clasework1
usernum = int(input("enter your num: "))
if usernum % 2==1:
    print("odd")
else :
    print("even")
# clasework 2
userage = int(input("enter your age"))
if userage <=18:
    print(" you are too small to vote")
else:
    uservote = input(" enter your choice: pink or blue: ")
    print("your voit is error")

 # homework3
 temperature= 25