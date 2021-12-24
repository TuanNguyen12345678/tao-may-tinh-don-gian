def cong(num1,num2,num3):
    return num1+num2+num3
def tru(num1,num2,num3):
    return num1-num2-num3
def nhan(num1,num2,num3):
    return num1*num2*num3
def chia(num1,num2,num3):
    return num1/num2/num3
try:
    so1 = int(input("Nhập số thứ nhất từ bàn phím: "))
    so2 = int(input("Nhập só thứ hai từ bàn phím: "))
    so3 = int(input("NHập số thứ ba từ bàn phím: "))
    pheptoan = input("Nhập phép toán +,-,*,/ mà bạn muốn")
    if pheptoan=='+':
        print(so1,"+",so2,"+",so3, "=",cong(so1,so2,so3))
    elif pheptoan=='-':
        print(so1,"-",so2,"-",so3,"=",tru(so1,so2,so3))
    elif pheptoan == '*':
        print(so1,"*",so2,"*",so3,"=",nhan(so1,so2,so3))
    elif pheptoan == '/':
        print(so1,"/",so2,"/",so3,"=",chia(so1,so1,so3))
    else:
        print("Không có kết quả")
except:
    print('Nhập đầu vào chưa đúng')