n = int(input("Moi nhap vao mo so: "));
ktra = n % 2
# ktra == 0 la so chan
# ktra > 0 la so le9
if ktra == 0:
    print(f"{n} la so chan")
else:
    print(f"{n} la so le")