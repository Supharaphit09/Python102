'''
โครงสร้างควบคุม (control structure)
1. แบบลำดับ : ทำงานเป็นลำดับจากบนมาล่าง  เช่น BMI
2. แบบเลือก : เลือกได้ว่าต้องการให้เป็นอะไร
3. แบบทำซ้ำ
'''

# แบบเลือก
'''
โครงสร้าง if => if expression :
                    statement
if = ต้องเป็น จริง ถึงจะทำงานต่อ ไม่งั้นจะจบโปรแกรมเลย
- จะเช็คทุกเครสที่เราใส่เข้าไป ควรระวัง**
'''
##age = int(input("อายุ : "))

#if age >= 15 :
#    print("นางสาว")

'''
โครงสร้าง if - else => 
if จริง :
    ทำอะไร
else :
    ทำอะไร
if-else = if ใช้กับคำสั่งที่เป็นจริง  else ใช้กับคำสั่งที่เป็นเท็จ 
'''

#if age <= 12:
#    print("วัยเด็ก")
#elif age <= 25: # elif ถ้าเจอ 1 เงื่อนไขที่เป็นจริง จะจบการทำงานเลย
#    print("วัยรุ่น")
#elif age <= 60:
#    print("วัยทำงาน")
#else :
#    print("วัยชรา")

# ใช้ if-else กับ and or not ได้ แต่ต้องดูเรื่องตัวเชื่อมดีๆ ระวัง**

# Ternary Operator : การลดรูปคำสั่ง if-else ให้คำสั่งสั้นลง
'''
โครงสร้าง
"เงื่อนไขเป็นจริง" if expression else "เงื่อนไขอื่นๆ"
'''
#print("วัยเด็ก") if age <= 12 else print("วัยรุ่น")

# if ซ้อน if
#if age <= 15:
#    if age == 15:
#        print("ม.3")
#    elif age == 14:
#        print("ม.2")
#    elif age == 13:
#        pass # คำสั่ง pass มีไว้เพื่อวางโครงสร้างของตัวโค้ดที่เราวางไว้ แต่ยังคิดไม่ออกว่าให้ทำอะไร ก็ให้ผ่านไปก่อน เพราะถ้าว่างไว้จะ error
#    else :
#        print("ประถมศึกษา")
#else :
#    print("จบการศึกษาแล้ว")






# แบบทำซ้ำ
'''
while expression :
        statement
จะทำงานก็ต่อเมื่อ เงื่อนไขเป็นจริง ทำไปเรื่อยๆจนกว่าจะเป็นเท็จ
'''

#i = 1              # ตัวนับจำนวนรอบ
#summation = 0      #เก็บผลการบวกเลขตามจำนวนรอบ
#average = 0        #ผลรวม / จำนวนรอบ

#count = int(input("ระบุจำนวนรอบ : "))

#while i <= count :
#    summation += i # เก็บผลรวมของ i แต่ละรอบ
#    print("รอบ = " , i , "ค่า sum = " , summation)
#    i += 1

#average = summation / count
#print("ผลรวมการบวกเลข = " , summation)
#print("ค่าเฉลี่ย = " , average)

'''
for i in range(start , stop , step): # กำหนดรอบ 
loop for รู้จำนวนรอบที่ชัด สามารถระบุได้ชัดเจนว่าต้องการเริ่มเท่าไหร่ จบเท่าไหร่
'''

#for i in range(3): # เริ่มจาก 0
#    print("รอบที่ = " , i , "Hello World")

#for i in range(1 , 6 , 2): # start stop step(1 + 2 =3 ,3 + 2 =5)
#    print("รอบที่ = " , i , "Hello World")

#summation = 0
#for i in range(1,6):
#    summation += 1
#    print("รอบที่ =" , i , "sum = ",summation)
#    
#print("ผลรวม = " , summation)
#print("เฉลี่ย = ", summation/10)

#for i in range (-10,6):
#    print("รอบที่ = " , i)

# Loop ซ้อน Loop
#i = 1
#while i <= 2:
#    j = 1
#    while j <= 5:
#        print("รอบที่ = " , i ,"ตำแหน่งที่ : " , j)
#        j += 1
#    i += 1

#print("====================")

#for i in range(1,3):
#    print("รอบที่ = ", i)
#    for j in range(1,6):
#        print("ตำแหน่งที่ = " , j)