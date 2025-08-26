# data=input("مقدار خود را وارد کنید: ")
# data=int(data)
# if data>=1000000000000:
#     data/=1000000000000
#     print(data,'TB')
    
# elif data>=1000000000:
#     data/=1000000000
#     print(data,'GB')
# elif data >= 1000000:
#     data/=1000000
#     print(data,'MB')
# elif data>=1000:
#     data/=1000
#     print(data,'KB')
# else:
#     print(data,'Byte')

# ------------------------------------

'''
۱. شمارش تا ۱۰
یک برنامه بنویس که با استفاده از while اعداد ۱ تا ۱۰ را چاپ کند.
مثال خروجی:

python-repl
Copy
Edit
1
2
3
...
10
۲. مجموع اعداد مثبت تا صفر
برنامه‌ای بنویس که از کاربر اعداد بگیرد و مجموع آن‌ها را حساب کند، تا زمانی که کاربر عدد صفر وارد کند.

۳. حدس عدد
یک عدد مخفی (مثلاً ۷) انتخاب کن. برنامه باید از کاربر بخواهد عددی وارد کند تا زمانی که عدد درست حدس زده شود. اگر عدد بزرگ‌تر یا کوچک‌تر بود، به کاربر بگو.

۴. چاپ مثلث ستاره‌ای
برنامه‌ای بنویس که با استفاده از while یک مثلث ستاره‌ای به شکل زیر چاپ کند (تعداد سطرها از کاربر گرفته شود):

markdown
Copy
Edit
*
**
***
****
۵. عدد معکوس
یک برنامه بنویس که یک عدد صحیح از کاربر بگیرد و رقم‌های آن را به صورت معکوس چاپ کند.
مثلاً اگر ورودی 1234 باشد خروجی 4321 شود.
'''
i = 1
while i <= 10:
    print(i)
    i += 1


total = 0
num = int(input("عدد وارد کن (صفر برای پایان): "))

while num != 0:
    total += num
    num = int(input("عدد وارد کن (صفر برای پایان): "))

print("مجموع اعداد =", total)

# -------------------------------------


secret = 7
guess = None

while guess != secret:
    guess = int(input("حدس بزن: "))
    if guess < secret:
        print("بزرگ‌تر حدس بزن!")
    elif guess > secret:
        print("کوچک‌تر حدس بزن!")

print("آفرین! درست حدس زدی 🎉")
# -------------------------------------
import random

# عدد تصادفی بین 1 و 100
secret = random.randint(1, 100)
guess = None

print("یک عدد بین 1 تا 100 حدس بزن!")

while guess != secret:
    guess = int(input("حدس تو: "))
    if guess < secret:
        print("بزرگ‌تر حدس بزن!")
    elif guess > secret:
        print("کوچک‌تر حدس بزن!")

print("آفرین! عدد درست", secret, "بود 🎉")

# -------------------------------------


rows = int(input("تعداد سطرها: "))
i = 1

while i <= rows:
    print("*" * i)
    i += 1

# -----------------------------

num = int(input("عدد وارد کن: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("عدد معکوس =", reverse)

    


