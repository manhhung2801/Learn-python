from math import sqrt

# TH9: Viết chương trình giải phương trình bậc 2: ax^2 + bx + c = 0

# Giải phương trình bậc 2
# Bước 1: Tính Δ = b^2 - 4ac

# Bước 2: So sánh Δ với 0:
# - Nếu Δ < 0, phương trình vô nghiệm.
# - Nếu Δ = 0, phương trình có nghiệm kép x1 = x2 = -b / (2a).
# - Nếu Δ > 0, phương trình có 2 nghiệm phân biệt x1 = (-b + sqrt(Δ)) / (2a) và x2 = (-b - sqrt(Δ)) / (2a).

print("Chương trình giải phương trình bậc 2")
a = float(input("Nhập vào giá trị của a trong biểu thức ax^2 + bx + c = 0: "))
b = float(input("Nhập vào giá trị của b trong biểu thức ax^2 + bx + c = 0: "))
c = float(input("Nhập vào giá trị của c trong biểu thức ax^2 + bx + c = 0: "))

# Kiểm tra nếu a = 0 thì không phải là phương trình bậc 2
if a == 0:
    print("Giá trị a phải khác 0 để là phương trình bậc 2.")
else:
    # Tính Δ
    delta = (b ** 2) - (4 * a * c)
    
    # So sánh Δ với 0 và đưa ra kết quả tương ứng
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép x1 = x2 = {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

#https://quantrimang.com/cong-nghe/cach-giai-phuong-trinh-bac-2-176425