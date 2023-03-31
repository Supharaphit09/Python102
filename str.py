'''
เจาะลึก string
'''
# การสร้าง str => 'ใช้กับตัวอักษร'  "ใช้กับข้อความยาวๆ"
name = "Supharaphit"

# index => ให้โชว์แค่ตัวอักษรที่ต้องการ เริ่มต้นจากซ้ายไปขวา ตัวซ้ายสุด = 0
print(name[1])
print(name[0:3]) # Sup => เพราะ ตำแหน่งสุดท้ายจะให้เอาตัวก่อนหน้า จึงแสดงแค่ Sup  
# ถ้ามีช่องว่างก็นับเป็น 1 ช่อง
print(name[-2])  # นับจาก ขวามาซ้าย ค่าจะติด -

# len function => เช็คว่ามีกี่ตัวอักษร
print(len(name))

# strip => การลบช่องว่าง
lname = "  Saenthawisuk  "
print(lname)             # ยังไม่ลบ
lname = lname.strip()
print(lname)             # ลบสองด้าน
lname = lname.lstrip()   
print(lname)             # ลบซ้าย
lname = lname.rstrip()
print(lname)             # ลบขวา

# แปลง case ของ string
print(name.upper()) # ทำให้เป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name.lower()) # ทำให้เป็นตัวพิมพ์เล็กทั้งหมด
print(name.capitalize()) # ทำให้ตัวแรกเป็นตัวพิมพ์ใหญ่ทั้งหมด

# การแทนที่
print(name.replace("Sup","Eyes"))
grade = ("ศุภารพิชญ์ เกรด 4 ชั้นปีที่ 4")
print(grade.replace("4","3.5"))
print(grade.replace("4","3.5",1)) # ถ้าเจอเลข 4 ให้เปลี่ยนเป็น 3.5 จำนวน 1 รอบ

# การเช็คข้อความ => True , Flase
list = ("ไปซื้อข้าวและอาหารที่ตลาด")
x = "ข้าว" in list  # True

# การแทนที่ และ การเช็คข้อความ 
if x:
    list = list.replace("ข้าว","ไข่")
print(list)

# การต่อ string (+)
name2 = "Supharaphit"
lname2 = "Saenthawisuk"
age = "18"
salary = 50000.555414

print("ข้อมูลของฉัน : " + "\n" + "ชื่อของฉัน = " + name2 + "\n" + "นามสกุลของฉัน = " + lname2 + "\n" + "อายุของฉัน = " + age + "\n")

# การจัดรูปแบบการแสดงผล {}
print("ข้อมูลของฉัน")
text = "ชื่อจริง : {} \nนามสกุล : {} \nอายุ : {} \nเงินเดือน : {}"
print(text.format(name2,lname2,age,salary))
print("=============================")
print("ข้อมูลของฉัน")
text = "นามสกุล : {1} \nชื่อจริง : {0} \nอายุ : {2} \nเงินเดือน : {3:.2f}" # .2f ใช้สั่งให้เลขปัดเศษขึ้น
print(text.format(name2,lname2,age,salary))

# นับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ ทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
print(fruit.count("ทุเรียน"))

# เช็คคำขึ้นต้น (startswith) เช้คคำลงท้าย (endswith)
test = "นางสาวศุภารพิชญ์ แสนทวีสุข"
if test.startswith("นางสาว"): 
    print("เป็นเพศหญิง")
else:
    print("เป็นเพศชาย")
    
test2 = "0864511895"
if test2.endswith("1895"):
    print("แม่โทรมา")
else:
    print("เบอร์ที่ไม่ทราบ")