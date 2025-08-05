
# تمرین ۱: عدد مثبت یا منفی یا صفر
num = float(input("یک عدد وارد کنید: "))

if num > 0:
    print("عدد مثبت است.")
elif num < 0:
    print("عدد منفی است.")
else:
    print("عدد صفر است.")

# --------------------------------------------------

# تمرین ۲: تعیین نمره و وضعیت دانشجو
score = float(input("نمره‌ی خود را وارد کنید (۰ تا ۲۰): "))

if score < 0 or score > 20:
    print("نمره وارد شده معتبر نیست.")
elif score < 10:
    print("مردود")
elif score < 15:
    print("قابل قبول")
elif score < 17:
    print("خوب")
else:
    print("عالی")

# --------------------------------------------------

# تمرین ۳: ماشین‌حساب ساده
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))
op = input("عملگر را وارد کنید (+ - * /): ")

if op == "+":
    print("نتیجه:", num1 + num2)
elif op == "-":
    print("نتیجه:", num1 - num2)
elif op == "*":
    print("نتیجه:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("نتیجه:", num1 / num2)
    else:
        print("تقسیم بر صفر مجاز نیست!")
else:
    print("عملگر نامعتبر است.")

# --------------------------------------------------

# تمرین ۴: تعیین فصل سال
month = int(input("شماره ماه را وارد کنید (۱ تا ۱۲): "))

if month >= 1 and month <= 3:
    print("فصل: بهار")
elif month >= 4 and month <= 6:
    print("فصل: تابستان")
elif month >= 7 and month <= 9:
    print("فصل: پاییز")
elif month >= 10 and month <= 12:
    print("فصل: زمستان")
else:
    print("ماه وارد شده معتبر نیست.")

# --------------------------------------------------

# تمرین ۵: اعتبار رمز عبور
password = input("رمز عبور را وارد کنید: ")

if len(password) < 8:
    print("رمز خیلی کوتاه است.")
elif not any(char.isdigit() for char in password):
    print("رمز باید شامل عدد باشد.")
elif not any(char.isupper() for char in password):
    print("رمز باید حروف بزرگ داشته باشد.")
else:
    print("رمز معتبر است.")

# --------------------------------------------------

# تمرین ۶: محاسبه کرایه تاکسی
distance = float(input("فاصله طی‌شده را وارد کنید (کیلومتر): "))

fare = 0

if distance <= 3:
    fare = distance * 10000
elif distance <= 10:
    fare = 3 * 10000 + (distance - 3) * 8000
else:
    fare = 3 * 10000 + 7 * 8000 + (distance - 10) * 6000

print("مبلغ کرایه:", int(fare), "تومان")
