# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = นน.(kg) / สส. ** 2 (m)

# input
weight = int(input("น้ำหนัก (kg) : "))
height = int(input("ส่วนสูง (m) : ")) / 100

# process
bmi = weight / (height ** 2)

if bmi <18.0:
    result = "ผอม/น้ำหนักน้อย"
elif bmi >=18.5 and bmi <= 24.9:
    result = "ปกติ/สุขภาพดี"
elif bmi >=25 and bmi <=29.9:
    result ="ท้วม/อ้วน"
elif bmi >=30 and bmi <=34.9:
    result ="โรคอ้วนระดับ 1"
elif bmi >=35 and bmi <=39.9:
    result ="โรคอ้วนระดับ 2"
else :
    result = "โรคอ้วนระดับ 3"

# output
print("ค่า BMI : " , bmi)
print("ผลที่ได้ : " , result)

'''
<18.5               : ผอม/น้ำหนักน้อย
>=18.5 and <=24.9   : ปกติ/สุขภาพดี
>=25 and <=29.9     : ท้วม/อ้วน
>=30 and <=34.9     : โรคอ้วนระดับ 1
>=35 and <=39.9     : โรคอ้วนระดับ 2
>=40                : โรคอ้วนระดับ 3
'''