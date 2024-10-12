bank = input("กรุณาใส่เงินของคุณ : ")  # รับจำนวนเงินที่มีจากผู้ใช้
print("รับเงินมา : ", bank, "บาท")  # แสดงจำนวนเงินที่ได้รับจากผู้ใช้
bank = int(bank)  # แปลงจำนวนเงินที่รับเป็นจำนวนเต็ม

stamp = input("คุณต้องการ Stamp กี่ดวง : ")  # รับจำนวน Stamp ที่ต้องการจากผู้ใช้
print("ซื้อ Stamp : ", stamp, "ดวง")  # แสดงจำนวน Stamp ที่ต้องการซื้อ
stamp = int(stamp)  # แปลงจำนวน Stamp ที่ต้องการเป็นจำนวนเต็ม

result = stamp * 25  # คำนวณราคาของ Stamp
if bank < result:
    print("เงินไม่พอ")  # แสดงข้อความว่าเงินไม่เพียงสำหรับการซื้อ Stamp
else:
    print("รวมเป็นเงิน : ", result, "บาท")  # แสดงราคารวมของ Stamp ที่ต้องจ่าย

ts, fh, h, ft, tt, ten = 0, 0, 0, 0, 0, 0  # กำหนดตัวแปรสำหรับจำนวนธนบัตรแต่ละหน่วยให้เป็น 0 เริ่มต้น
returnmoney = bank - result  # คำนวณจำนวนเงินทอนที่ต้องทอนให้กับผู้ใช้

# คำนวณจำนวนเงินที่ต้องทอน
if (returnmoney // 1000) > 0:
    ts = returnmoney // 1000
    returnmoney = returnmoney - (ts * 1000)
if (returnmoney // 500) > 0:
    fh = returnmoney // 500
    returnmoney = returnmoney - (fh * 500)
if (returnmoney // 100) > 0:
    h = returnmoney // 100
    returnmoney = returnmoney - (h * 100)
if (returnmoney // 50) > 0:
    ft = returnmoney // 50
    returnmoney = returnmoney - (ft * 50)
if (returnmoney // 20) > 0:
    tt = returnmoney // 20
    returnmoney = returnmoney - (tt * 20)
if (returnmoney // 10) > 0:
    ten = returnmoney // 10
    returnmoney = returnmoney - (ten * 10)

cbstp = bank // 25  # คำนวณจำนวน Stamp ที่ซื้อได้จากเงินที่มี

if returnmoney > 0:
    print("ได้รับเงินมาเป็น")  # แสดงข้อความว่าได้รับเงินมาเท่าไหร่
elif returnmoney < 0:
    print("ซื้อได้", cbstp, "ดวง", "เป็นเงิน ", bank, " บาท")  # แสดงจำนวน Stamp ที่ซื้อได้และเงิน
if ts > 0:
    print("ธนบัตรใบละ 1000 X", ts)  # แสดงจำนวนธนบัตรแต่ละหน่วย
if fh > 0:
    print("ธนบัตรใบละ 500 X", fh)
if h > 0:
    print("ธนบัตรใบละ 100 X", h)
if ft > 0:
    print("ธนบัตรใบละ 50 X", ft)
if tt > 0:
    print("ธนบัตรใบละ 20 X", tt)
if ten > 0:
    print("ธนบัตรใบละ 10 X", ten)
if ts == 0 and fh == 0 and h == 0 and ft == 0 and tt == 0 and ten == 0:
    print("ไม่มีเงินทอน")  # แสดงข้อความว่าไม่มีเงินทอน

tip = returnmoney % 10  # คำนวณเงินทริปของพนักงาน

if returnmoney % 10 != 0:
    print("เงินทริปพนักงาน ", tip, " บาท")  # แสดงจำนวนเงินทริป
if returnmoney % 10 == 0:
    print("ไม่มีทริปพนักงาน")  # แสดงข้อความว่าไม่มีเงินทริป
