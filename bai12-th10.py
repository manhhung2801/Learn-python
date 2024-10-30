# TH10: Viết chương trình kiểm tra tháng trong năm thuộc quý mấy 
# Gợi ý: 
# 1 năm chia làm 4 quý mỗi quý 3 tháng
# Quý 1: gồm các tháng 1, 2, 3
# Quý 2: 4, 5, 6
# Quý 3: 7, 8, 9
# Quý 4: 10, 11, 12
thang = int(input("Nhap vao thang: "))
if thang in (1, 2, 4):
    print(f"{thang} nam trong quy 1")
elif thang in (4, 5, 6):
    print(f"{thang} nam trong quy 2")
elif thang in (7, 8, 9):
    print(f"{thang} nam trong quy 3")
elif thang in (10, 11, 12):
    print(f"{thang} nam trong quy 4")
else:
    print(f"{thang} sai dinh dang thang trong nam !")