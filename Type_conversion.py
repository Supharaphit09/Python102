'''
การแปลงข้อมูล
'''
x = 10      #int เลข จน. เต็ม
y = 3.14    #float เลข ทศนิยม
z = "20"    #str ข้อความ

print(type(x))
print(type(y))
print(type(z))

'''
# บวกเลข
result = x + y
print(result)
'''

'''
# string => int
result = x + int(z)
print(result)
'''

'''
# int => string
result = str(x) + z
print(result)
'''

# string => float
print(float(z))

# float => string
print(str(y))

#int => float
print(float(x))

#float => int
print(int(y))

# วิธีแปลงช้อมูลตัวแปรใหม่
z = float(z)
z = z + 50
print(z)