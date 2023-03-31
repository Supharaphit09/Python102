# โปรแกรมหาตัวเลข มาก / น้อย / เท่ากับ
'''
a = int(input("ป้อนหมายเลขที่ 1 : "))
b = int(input("ป้อนหมายเลขที่ 2 : "))

if a>b :
    print(a,"มากกว่า",b)
elif a==b :
    print(a,"เท่ากับ",b)
else :
    print(a,"น้อยกว่า",b)
'''

# โปรแกรมหาเลข คู่/คี่
'''
number = int(input("ป้อนหมายเลข : "))

if number % 2 == 0:
    print("เป็นเลขคู่")
else :
    print("เป็นเลขคี่")
'''

# โปรแกรมแลกเงินและหาจำนวนแบงค์
'''
number = int(input("จำนวนเงิน : "))

if number >= 1000:
    print("1000 บาท", number//1000, "ใบ")
    number %= 1000
if number >= 500:
    print("500 บาท", number//500, "ใบ")
    number %= 500
if number >= 100:
    print("100 บาท", number//100, "ใบ")
    number %= 100
if number >= 50:
    print("50 บาท", number//50, "ใบ")
    number %= 50
if number >= 20:
    print("20 บาท", number//20, "ใบ")
    number %= 20
'''

# แปลง ค.ศ เป็น พ.ศ (+ 543) และ แปลง พ.ศ. เป็น ค.ศ (-543)
'''
number = int(input("ป้อน พ.ศ. :"))
number += 543
print("เป็น ค.ศ. = ",number)

number = int(input("ป้อน ค.ศ. :"))
number -= 543
print("เป็น พ.ศ. = ",number)
'''

# โปรแกรมแปลงอุณหภูมิ จาก celsius to fahrenhrit and fahrenhrit to celsius
'''
temp = input("ป้อนอุณหภูมิ : ")

degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == "C" :
    result = (9*degree/5) + 32
    unit_result = "Fahrenhrit"
if unit == "F" :
    result = (degree - 32)* 5 / 9
    unit_result = "Celsius"

print("แปลงตัวเลข = ", temp , "เป็น" , unit_result , " =  ",result )
'''

# แม่สูตรคูณ
'''
start = int(input("ป้อนแม่สูตรคูณเริ่มต้น = "))
stop = int(input("ป้อนแม่สูตรคูณสุดท้าย = "))

for i in range(start,stop +1):
    print("แม่สูตรคูณ = ", i)
    for y in range(1,13):
        print ( i , "x" , y ," = " ,(i*y))
'''

# ป้อนตัวเลข และ หาผลรวมตัวเลข (แบบระบุชัดเจน)
'''
# ป้อนตัวเลข และ หาผลรวมตัวเลข
start , stop = 1 , 5
sum , avg = 0 , 0
while (start <= stop):
    number = int(input("ป้อนตัวเลข : "))
    sum += number # บวกเลขที่ป้อนแต่ละรอบ
    start += 1

avg = sum/stop
print("ผลรวม = " , sum)
print("ค่าเฉลี่ย = " , avg )
'''

# ป้อนตัวเลข และ หาผลรวมตัวเลข (แบบไม่ระบุ start stop)
'''
sum  = 0 
while sum != 100 : # ถ้าผลรวม = 100 จะจบโปรแกรม
    number = int(input("ป้อนตัวเลข : "))
    sum += number # บวกเลขที่ป้อนแต่ละรอบ
    print("ผลรวม = " , sum)
'''

'''
sum  = 0 
while sum < 100 : # ถ้าผลรวมเกิน 100 จะจบโปรแกรม
    number = int(input("ป้อนตัวเลข : "))
    sum += number # บวกเลขที่ป้อนแต่ละรอบ
    print("ผลรวม = " , sum)
'''

'''
sum  = 0 
while True :
    number = int(input("ป้อนตัวเลข : "))
    sum += number # บวกเลขที่ป้อนแต่ละรอบ
    if sum >= 100: # ถ้าผลรวมเกิน 100 จะจบโปรแกรม
        break
    print("ผลรวม = " , sum)
'''

# โปรแกรมค้นหาตัวเลขมากสุด / น้อยสุด
'''
max , min = 0 , 9999

while True:
    number = int(input("ป้อนตัวเลข : "))
    if number < 0 :     # ถ้าป้อนเลขที่ < 0 จะหยุดโปรแกรม
        break
    if number > max :
        max = number
    if number < min :
        min = number

print("ค่าสุงสุด" , max)
print("ค่าต่ำสุด" , min)
'''

# ตัวเลขขั้นบันได
'''
number = int(input("ป้อนตัวเลข = "))

for row in range (1,number+1):
    for column in range (1,row+1):
        print(column,end = '')
    print(" ") #ขึ้นบรรทัดใหม่
'''
'''
อธิบาย

input = 3

row = 1 , 3
column = 1 , 2
=> 1

row = 2
column = 1 , 3
=> 12

row = 3
column = 1 , 4
=> 123
'''

# สร้างภาพวาด 4 เหลี่ยมจตุรัส
# while ใช้เมื่อไม่รุ้ขนาดที่ชัดเจน  for ใช้เมื่อรู้ขนาดที่ชัดเจน
'''
number = int(input("ป้อนขนาด : "))

for row in range(number):
    for column in range(number):
        print("x" , end=" ")
    print(" ") #ขึ้นบรรทัดใหม่
'''

# สร้างตารางหมากฮอต
'''
number = int(input("ป้อนขนาด : "))

for row in range(number):
    for column in range(number):
        if (row + column) %2 == 0:
            print("x" , end = "")
        else:
            print("o" , end = "")
    print(" ")
'''
'''
อธิบาย
3 x 3
row = 0 + culumn = 0 หารลง : x
row = 0 + culumn = 1
row = 0 + culumn = 2 หารลง : x

row = 1 + culumn = 0
row = 1 + culumn = 1 หารลง : x
row = 1 + culumn = 2

row = 2 + culumn = 0 หารลง : x
row = 2 + culumn = 1
row = 2 + culumn = 2 หารลง : x

xox
oxo
xox
'''

# สร้างขอบตาราง
'''
number = int(input("ป้อนขนาด : "))

for row in range(number):
    for column in range(number):
        if row == 0 or row == number - 1 or column == 0 or column == number - 1 :
            print("x" , end=" ")
        else:
            print(" ", end =" ")
    print(" ") #ขึ้นบรรทัดใหม่
'''

# เกมทายเลขลูกเต๋า
import random

my_random = random.randrange(1,20)
k = 1
correct = False

while True:
    number = int(input("ป้อนคำตอบของคุณ : "))
    correct = (number == my_random)

    if not correct:
        if(number > my_random):
            print("น้อยกว่านี้")
        if(number < my_random):
            print("มากกว่านี้")


    if correct:
        print("รับไปเลย 1 ล้านบาท")
        break
    else:
        print("เสียใจด้วย คุณไม่ถูกรางวัล")

    if number <0 or k == 5:
        break
    k += 1

if not correct :
    print("เสียใจด้วยนะ")
    print("เฉลย = " , my_random)