dtb = float(input("Nhap vao dien trung binh: "))
if dtb >= 9.0:
    print(f"Ban dat loai gioi, diem trung binh cua ban la: {dtb}")
elif dtb > 7.0 and dtb < 9.0:
    print(f"Ban dat loai kha, diem trung binh cua ban la: {dtb}")
elif dtb > 5.0 and dtb < 7.0:
    print(f"Ban dat loai TB, diem trung binh cua ban la: {dtb}")
else: 
    print(f"Ban dat loai yeu, diem trung binh cua ban la: {dtb}")
    