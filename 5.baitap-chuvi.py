import math 
r = float(input("moi nhap vao ban kinh cua duong tron: "));
chuvi = 2 * r * math.pi
dientich = math.pi * (r**2) 

print("chu vi hinh tron la: ",chuvi)


print("dien tich hinh tron la: ",dientich)
# cach 2 in thong bao ra man hinh
# print(f"chu vi hinh tron la {chuvi}")

# cach 3 in thong bao ra man hinh
# print("chu vi hinh tron la: ", chuvi, "dien tich la: ", dientich)
# print(f"chu vi hinh tron la: {chuvi} dien tich la: {dientich}")
print("chu vi hinh tron la: {} dien tich la: {}", format(chuvi,dientich))
