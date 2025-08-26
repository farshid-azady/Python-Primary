# command=""
# while command != "exit":
#     command = input("Enter a command (type 'exit' to quit): ")
#     print(f"You entered: {command}")


# برنامه محاسبه مجموع اعداد بین دو عدد با while

# گرفتن دو عدد از کاربر
num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))

# پیدا کردن کوچک‌ترین و بزرگ‌ترین عدد
start = min(num1, num2)
end = max(num1, num2)

# محاسبه مجموع
total = 0
current = start

while current <= end:
    total += current
    current += 1

print(f"مجموع اعداد بین {num1} و {num2} برابر است با: {total}")
# =========================================================================
# برنامه محاسبه مجموع اعداد بین دو عدد با while True

while True:
    # گرفتن ورودی از کاربر
    num1 = input("عدد اول را وارد کنید (یا q برای خروج): ")
    if num1.lower() == "q":
        print("خروج از برنامه...")
        break

    num2 = input("عدد دوم را وارد کنید (یا q برای خروج): ")
    if num2.lower() == "q":
        print("خروج از برنامه...")
        break

    # تبدیل به عدد
    num1 = int(num1)
    num2 = int(num2)

    # پیدا کردن کوچک‌ترین و بزرگ‌ترین عدد
    start = min(num1, num2)
    end = max(num1, num2)

    # محاسبه مجموع
    total = 0
    current = start
    while current <= end:
        total += current
        current += 1

    print(f"👉 مجموع اعداد بین {num1} و {num2} برابر است با: {total}")
    print("-" * 40)

# ================================================================
# برنامه محاسبه مجموع اعداد بین دو عدد با while True

while True:
    num1 = int(input("عدد اول را وارد کنید: "))
    num2 = int(input("عدد دوم را وارد کنید: "))

    start = min(num1, num2)
    end = max(num1, num2)

    total = 0
    current = start
    while current <= end:
        total += current
        current += 1

    print(f"👉 مجموع اعداد بین {num1} و {num2} برابر است با: {total}")
    
    # چون فقط یکبار می‌خوایم اجرا بشه
    break
# =============================================================================
# برنامه محاسبه مجموع اعداد وسطی بین دو عدد با while True

while True:
    num1 = int(input("عدد اول را وارد کنید: "))
    num2 = int(input("عدد دوم را وارد کنید: "))

    start = min(num1, num2) + 1   # یکی بعد از عدد کوچکتر
    end = max(num1, num2) - 1     # یکی قبل از عدد بزرگتر

    total = 0
    current = start
    while current <= end:
        total += current
        current += 1

    print(f"👉 مجموع اعداد بین {num1} و {num2} (بدون خودشان) برابر است با: {total}")

    break
# =============================================================================