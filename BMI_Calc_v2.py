a = float(input("Введите Ваш рост в метрах (например - 1.86): "))
b = float(input("Введите Ваш вес в килограммах (например - 67): "))
sex = str(input("Введите Ваш пол (М или Ж):"))
age = int(input("Введите Ваш возраст:"))

s = [20]+["="]*15+[50] # 20 - minimal BMI, 50 - maximal BMI, one "=" - 2 points
bmi = round(b/(a**2), 2)
i = int(round((bmi-20)/2)) # position "|" in list, where 20 - minimal BMI

print ("Ваш индекс массы тела: ", bmi)

if bmi<20 and sex == "М" and age <30:
    print ("Наращивай массу и занимайся спортом, шкет!")
if bmi<20 and sex == "М" and age >30:
    print ("Работа на вас плохо влияет, надо кушать, сэр!")   
if bmi<20 and sex == "Ж" and age <30:
    print ("Хватит быть анорексичкой, кушай здоровую еду!")
if bmi<20 and sex == "Ж" and age >30:
    print ("Перестаньте стрессовать и кушайте полезную пищу! Слишком маленький BMI!")    
if bmi>50 and sex == "М" and age <30:
    print ("Пора худеть! Бабушкины пирожки до добра не доведут!")
if bmi>50 and sex == "М" and age >30:
    print ("У вас такой вес, что сердечко может не выдержать. Займитесь собой!")   
if bmi>50 and sex == "Ж" and age <30:
    print ("Так вас мальчики не полюбят, пора худеть!")
if bmi>50 and sex == "Ж" and age >30:
    print ("Вы слишком упитанны, надо заняться собой!")
else:
    if 20>bmi>30:
        print ("Вы в отличной форме!")
    elif 30<bmi<50 and sex == "Ж" and age <30:
        print ("Вам надо заняться своим телом, заплыв жиром уже недалеко!")
    elif 30<bmi<50 and sex == "М" and age <30:
        print ("Мужик, сходи в зал, пока не поздно")    
    elif 30<bmi<50 and sex == "Ж" and age >30:
        print ("По вам плачет лечебная гимнастика, хотя бы в перерывах на работе")
    elif 30<bmi<50 and sex == "М" and age >30:
        print ("Пузо - это, конечно, хорошо, но скоро могут начаться проблемки")    
    
 
    s[i] = "|"
    print (*s, sep="")        
        

