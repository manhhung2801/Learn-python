t = int(input("Nha vao so thang: "))
# 1. neu thang 1, 2, 5, 7, 8, 10, 12 thi co 31 ngay
# 2. neu thang 4, 6, 9, 11 thi co 30 ngay
# 3. neu thang 2 thi yeu cau nhap them nam , nam nhuan thang 2 co 29 ngay,
# khon nhuan thi thang 2 co 28 ngay


if t in (1, 3, 5, 7, 8, 10, 12):
    print(f"thang {t} co 31 ngay")
        
elif t in (4, 6, 9, 11):
    print(f"thang {t} co co 30 ngay")
        
elif t == 2:
    n = int(input("Nhap them nam: "))
    if (n%4 == 0 and n%100 != 0) or n%400 == 0:
        print(f"{n} la nam nhuan nen thang 2 co 29 ngay")    
    else:
        print(f"{n} khong phai la nam nhuan nen thang 2 co 28 ngay")    
else:
    print("Ban nhap sai du lieu thang!")
    