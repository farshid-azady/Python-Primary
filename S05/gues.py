import random

# عدد تصادفی بین 1 و 100
# secret = random.randint(1, 100)
# guess = None


# print("guess")

# while guess != secret:
#     guess = int(input("your guess "))
#     if guess < secret:
#         print("guess greater than")
#     elif guess > secret:
#         print("guess less than")

# print("Good", secret, "yes 🎉")


# ---------------------------------------------
'''نسخه کاملتر'''
import random

# عدد تصادفی بین 1 و 100
secret = random.randint(1, 100)
guess = None
attempts = 0

print("یک عدد بین 1 تا 100 حدس بزن!")

while guess != secret:
    guess = int(input("حدس تو: "))
    attempts += 1  # هر بار که کاربر حدس می‌زند، شمارش اضافه می‌شود
    if guess < secret:
        print("بزرگ‌تر حدس بزن!")
    elif guess > secret:
        print("کوچک‌تر حدس بزن!")

print(f"آفرین! عدد درست {secret} بود 🎉")
print(f"تو با {attempts} تلاش موفق شدی! 👏")

