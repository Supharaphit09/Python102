'''
ตัวดำเนินการ Operator และ ตัวถูกดำเนินการ Operand
'''
# A , B => Operand
# + - * / => Operator

# +
#x = 10
#y = 5
#print("Plus = " ,x + y)
#print("Nagative = " ,x - y)
#print("Multiply = " ,x * y)
#print("Divide = " ,x / y)

# หารปัดเศษ
#print("Divide = " ,x // y)

# หารเอาเศษ ได้ตัวเศษออกมา
#print("Divide = " ,x % y)

# ยกกำลัง
#print("Square = " ,x ** y)

'''
ตัวดำเนินการเปรียบเทียบ T,F
'''

# ชนิดข้อมูลเหมือนกัน
# คำตอบ 2 คำตอบ => จริง/เท็จ

#x = 20
#y = 10
#z = 50
#print(" x มากกว่า y ? : " , x > y)
#print(" x น้อยกว่า y ? : " , x < y)
#print(" x เท่ากับ y ? : " , x == y)
#print(" x ไม่เท่ากับ y ? : " , x != y)

# หรือ => ถ้ามี T หนึ่งตัวจะเป็น T เสมอ ต้อง F ทั้งหมด จึงเป็น F
#print(" x มากกว่า หรือ เท่ากับ y ? : " , x >= y)
#print(" x น้อยกว่า หรือ เท่ากับ y ? : " , x <= y)

# เปรียบเทียบมากกว่า 2 ตัว
# และ => ถ้ามี F หนึ่งตัวจะเป็น F เสมอ ต้อง T ทั้งหมด จึงเป็น T
#print(" x มากกว่า y และ y มากกว่า z ? : " , x > y > z)
#print(" x น้อยกว่า y และ y น้อยกว่า z ? : " , x < y < z)

'''
ตัวดำเนินการทางตรรกศาสตร์
'''
# And => และ F หมด = F, T หมด = T, มี F 1 ตัว = F 
# Not => หรือ F = T, T = F
# Or => ไม่ F หมด = F, T หมด = T, มี T 1 ตัว = T 

#x = (5 > 10)
#y = (10 == 5)

# z = (5>10) and (10==5)
#z = x and y

#print(z)
#print(not z) # ใส่ not เพื่อให้เป็นคำตอบตรงข้าม

'''
ตัวดำเนินการที่ใช้ในการอัพเดต แก้ไข ค่าตัวแปล
'''

#x = 10
#print("ก่อนเพิ่มค่า : " , x)

#x += 5 #x = x + 5
#x -= 5 #x = x - 5
#x *= 5 #x = x * 5
#x /= 5 #x = x / 5
#x //= 5 #x = x // 5
#x **= 5 #x = x ** 5
#x %= 5 #x = x % 5
#print("หลังเพิ่มค่า : " , x)

'''
ลำดับความสำคัญของตัวดำเนินการทางคณิตศาสตร์
'''

'''
1. ()                            จาก ซ้าย ไป ขวา
2. - ,+ ,-- ,++, sizeof, (type)  จาก ขวา ไป ซ้าย
3. * ,/ ,%                       จาก ซ้ายไป ขวา
4. + , -                         จาก ซ้ายไป ขวา
5. =                             จาก ขวา ไป ซ้าย
'''

x = 5 + 2 * 10
print(x) # 5 + 25 = 25

x = (5 + 2) * 10
print(x) # 7 * 10 = 70

x = (5 + 2) * 10 / 2
print(int(x)) # 7 * 10 /2 = 70 / 2 = 35

x = (5 + 2) / 10 * 2
print(x) # 7/10 *2 = 0.7 * 2 = 1.4

x = (5 + 2) / (10 * 2) 
print(x) # 7/20 = 0.35

x = 5 + 2 / 10 * 2 - 5 
print(x) # 5 + 0.2 * 2 -5 = 5 + 0.4 -5 = 0.4