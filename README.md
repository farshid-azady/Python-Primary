


 # 
 - پایتون از قانون PEMDAS پیروی می کنه . حال این چیه:

 - حرف P اول نشون دهنده Parentheses که می شه پرانتز. یعنی اولیت اول با پرانتزه

 - حرف E نشون دهنده Exponents که میشه توان. یعنی اولیت بعدی با توان هست

 - حرف M نشون دهنده Multiplication که میشه ضرب

 - حرف D نشون دهنده Division که میشه تقسیم

 - حرف A نشوند دهنده Addition که میشه جمع

 - حرف S نشون دهنده Subtraction که میشه تفریق

 - ضرب و تقسیم هم اولویت هستن همچنین جمع و تفریق هم اولویتن. مثال زیر رو ببینید:

>>> a, b, c, d = 2, 3, 5, 7
>>> a ** (b + c) # parentheses
256

>>> a * b ** c # exponent: same as `a * (b ** c)`
7776

>>> a + b * c / d # multiplication / division: same as `a + (b * c / d)`
4.142857142857142
>>> a, b, c, d = 2, 3, 5, 7
>>> a ** (b + c) # parentheses
256

>>> a * b ** c # exponent: same as `a * (b ** c)`
7776

>>> a + b * c / d # multiplication / division: same as `a + (b * c / d)`
4.142857142857142
--------------------------
[![Project Euler](https://img.shields.io/badge/Project_Euler-About-ff69b4?logo=project-euler&logoColor=white&style=for-the-badge)](https://projecteuler.net/about)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ✨ Project Euler — About

<a href="https://projecteuler.net/about" target="_blank" rel="noopener noreferrer">
  <img src="blink.gif" width="20" height="20" alt="blink" />
  <strong>Click here: Project Euler – About</strong>
</a>

---

📋 Or copy the link manually:

```
https://projecteuler.net/about
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
> 💡 گزینه ۱:
قبل از کمک گرفتن از دیگران (یا حتی ChatGPT!)، با دقت فکر کن. تمرین‌ها طوری طراحی شدن که ذهن تو رو به چالش بکشن. پس اول خودت امتحان کن!

> 🧠 گزینه ۲:
این تمرین‌ها فرصتی برای تقویت قدرت حل مسئله هستن. اگر بلافاصله دنبال جواب بری، فرصت فکر کردن رو از خودت گرفتی! پس اول خودت تلاش کن، بعد سراغ کمک بیا.

> ⚠️ گزینه ۳:
نکته مهم: این تمرین‌ها طراحی شدن تا شما رو به چالش بکشن. لطفاً قبل از استفاده از هرگونه راه‌حل یا ابزار هوش مصنوعی، ابتدا خودتان فکر کنید، بنویسید، و تحلیل کنید.
>
> 
# تمرین‌های if-elif-else در پایتون 🐍

مجموعه‌ای از تمرین‌های ساده تا پیشرفته برای آموزش شرط‌ها در زبان برنامه‌نویسی پایتون، مناسب برای دانشجویان.

---

## ✅ تمرین ۱: عدد مثبت، منفی یا صفر
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

برنامه‌ای بنویسید که یک عدد از کاربر بگیرد و مشخص کند آن عدد **مثبت**، **منفی** یا **صفر** است.

> 💡 راهنما: از شرط‌های `if num > 0`, `elif`, و `else` استفاده کنید.

---

## ✅ تمرین ۲: تعیین نمره و وضعیت دانشجو
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

نمره‌ای بین ۰ تا ۲۰ از کاربر دریافت کنید. سپس بر اساس شرط‌های زیر، وضعیت دانشجو را چاپ کنید:
- کمتر از ۱۰ → مردود
- ۱۰ تا ۱۵ → قابل قبول
- ۱۵ تا ۱۷ → خوب
- ۱۷ تا ۲۰ → عالی

> 💡 راهنما: بازه‌ها را با `if` و `elif` به درستی تنظیم کنید.

---

## ✅ تمرین ۳: ماشین‌حساب ساده
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

دو عدد و یک عملگر ریاضی از کاربر بگیرید و نتیجه را محاسبه کنید.

> 💡 راهنما: از شرط‌های `if operator == '+'` و موارد مشابه استفاده کنید.

---

## ✅ تمرین ۴: تعیین فصل با شماره ماه
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

شماره ماه (۱ تا ۱۲) را بگیرید و فصل آن را مشخص کنید.

> 💡 راهنما: شرط‌های تو در تو برای بررسی گروهی از اعداد کاربرد دارد.

---

## ✅ تمرین ۵: بررسی رمز عبور معتبر
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

رمز عبوری بگیرید و بررسی کنید:
- حداقل ۸ کاراکتر باشد
- شامل عدد باشد
- شامل حرف بزرگ باشد

> 💡 راهنما: از توابع `len`, `isdigit`, `isupper` و حلقه استفاده کنید.

---

## ✅ تمرین ۶: محاسبه کرایه تاکسی
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

بر اساس مسافت طی‌شده:
- تا ۳ کیلومتر: ۱۰هزار تومان
- ۳ تا ۱۰: هر کیلومتر ۸هزار
- بیشتر از ۱۰: هر کیلومتر ۶هزار

> 💡 راهنما: محاسبه تفاضل مسافت‌ها در شرط‌ها مهم است.

---

## ✅ تمرین ۷: دسته‌بندی سن افراد
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

سن را گرفته و دسته‌بندی کنید:
- ۰ تا ۱۲: کودک
- ۱۳ تا ۱۹: نوجوان
- ۲۰ تا ۳۵: جوان
- ۳۶ تا ۵۹: میانسال
- ۶۰ به بالا: سالمند

> 💡 راهنما: دقت به ترتیب شرط‌ها و پوشش تمام بازه‌ها مهم است.

---

## ✅ تمرین ۸: تعیین نوع مثلث
سه ضلع گرفته و اگر مثلث قابل ساخت بود، مشخص کنید:
- متساوی‌الاضلاع
- متساوی‌الساقین
- مختلف‌الاضلاع

> 💡 راهنما: از قانون مجموع دو ضلع برای مثلث و سپس مقایسه استفاده کنید.
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

---

## ✅ تمرین ۹: محاسبه مالیات
درآمد را گرفته و با توجه به بازه، درصد مالیات را محاسبه کنید.

> 💡 راهنما: شرط‌های ترتیبی برای تعیین درصد مناسب استفاده شود.
> | درآمد ماهیانه (تومان) | درصد مالیات |

- | تا ۵ میلیون           | ۰٪          |
- 
- | ۵ تا ۱۰ میلیون        | ۱۰٪         |
- 
- | ۱۰ تا ۲۰ میلیون       | ۱۵٪         |
- 
-  | بیشتر از ۲۰ میلیون    | ۲۰٪         |


---

## ✅ تمرین ۱۰: تعیین روز هفته
عدد ۱ تا ۷ گرفته و روز هفته معادل آن را چاپ کنید.
> | عدد | روز      |
> 

> | 1   | شنبه     |
> 
> | 2   | یک‌شنبه  |
> 
| 3   | دوشنبه   |

> 💡 راهنما: برای نگاشت عدد به متن، از `if-elif` یا `dict` استفاده کنید.
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

---

## ✅ تمرین ۱۱: اعتبارسنجی کد ملی
> بررسی کنید کد ملی:
> دقیقاً ۱۰ رقم باشد

> فقط عدد باشد
>  طول کد ملی غیر از ۱۰ باشد → خطا چاپ شود.

>  اگر فقط شامل عدد نباشد → خطا چاپ شود.

> در غیر این صورت → "کد ملی معتبر است." چاپ شود.



> 💡 راهنما: از `len` و متد `isdigit()` استفاده کنید.
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

---

## ✅ تمرین ۱۲: ورود دو مرحله‌ای
> ابتدا رمز، سپس کد یک‌بار مصرف از کاربر گرفته شود و صحت آن بررسی گردد.
> سطح: ترکیبی و تو در تو (nested if)
> برنامه‌ای بنویسید که ابتدا رمز عبور را دریافت کند. اگر صحیح بود، سراغ مرحله دوم (کد یک‌بار مصرف) برود.
> اگر هرکدام اشتباه بود، پیام مناسبی نمایش داده شود.

مثال:


### رمز درست = python2024
### کد یک‌بار مصرف = 4321

> 💡 راهنما: ترکیب شرط‌های تو در تو با ورودی‌های متوالی کاربرد دارد.
<img src="https://www.python.org/static/community_logos/python-logo.png" width="100">

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
> ### ⚠️لطفا اکر در حل پروژه های بالا به مشکل برخوردید.در بالا همین صفحه در کنار دکمه CODE▶️ یه دکمه دیگر هست بنام Issues▶️ روش کلیک کن حالا وارد یه صفحه جدید میشی که اونجا هم یه دکمه 🟢رنگ هست بنام:New issue🟢روش کلیک کن.من اونجا واست یه صفحه مخصوص خودت طراحی کردم اسمش هست:**🔴گزارش باگ**. اون انتخاب کن.من طوری برات طراحیش کردم که مشکلات بصورت بخش بندی باش تا یاد بگبری چطوری به من گزارش بدی.حتی میتونی عکس گزارش خطا را از قسمتی که برایت توضیح دادم برای راهنمایی بیشتر واسم آپلود کنی.حالا دیگه با خیال راحت من در کنارت هستم.تا راحتتر بتونی این مسیر به همراه من طی کنی.موفق باشی./فرشید آزادی-مدرس دوره پایتون .
-  مشکلات پروژه را با من در میان بگذاری 👇 👇
- **❗ گزارش باگ:** **✅ آماده استفاده:**[👈clicke](https://github.com/farshid-azady/Python-Primary/issues) 🖱️ کنید.


---------------------------------------------------------------------------------------
> [!NOTE]
> ## 💬 سلام بچه‌ها لطفا توجه کنید:
 --------------------------------------------------------------------------------------
> [!IMPORTANT]
> ## 🖥️ تمرین برنامه‌نویسی:
> از شما خواسته می‌شود برنامه‌ای بنویسید که بر اساس عددی که کاربر وارد می‌کند، این مقدار را به **ترابایت، گیگابایت، مگابایت، کیلوبایت یا بایت** تبدیل کند.
>
> 🔹 نکته:  
> اگر عدد ورودی به صورت `1426` باشد، برنامه باید **به صورت هوشمند** از تعداد رقم‌ها بفهمد که این مقدار بر حسب کیلوبایت است.
>
> 🛠 روش حل:  
> - می‌توانید از `if-elif` یا `loop` استفاده کنید.  
> - برای موفقیت، مسئله را به بخش‌های کوچک تقسیم کنید.  
> - هرگز سعی نکنید کل مسئله را یکجا حل کنید، چون در نهایت **خیارشور ماشین** می‌شود 😄
>
> ❗ در بخش `else`، پیامی مناسب برای ورودی نامعتبر نمایش دهید.
----------------------------------------------------------------------------------------
> [!TIP]
> ## 1️⃣ تحلیل مسئله
> کاربر یک عدد وارد می‌کند.  
> 
> - اگر طول عدد خیلی زیاد باشد → احتمالاً **ترابایت** است.  
> - اگر کم باشد → احتمالاً **بایت** یا **کیلوبایت** است.  
> - ما بر اساس **تعداد رقم‌ها** تشخیص می‌دهیم که واحد چیست.  
>
> #### 📏 فرض تبدیل‌ها:
> - `1 KB = 1024 Bytes`  
> - `1 MB = 1024 KB`  
> - `1 GB = 1024 MB`  
> - `1 TB = 1024 GB`  
>
> ## 2️⃣ منطق تصمیم‌گیری
> - **1 تا 3 رقم** → Bytes  
> - **4 تا 6 رقم** → KB  
> - **7 تا 9 رقم** → MB  
> - **10 تا 12 رقم** → GB  
> - **بیشتر از 12 رقم** → TB
 
<h1 align="center">🚀 استراتژی حرفه‌ای حل مسائل</h1>

<p align="center">
📚 <b>راهنمای بهینه‌سازی مهارت برنامه‌نویسی و حل مسئله</b>
</p>

---

<details>
<summary><b>⏱️ ۱. قانون یک دقیقه</b></summary>

💡 اگر الگوریتم درست طراحی شده باشه، حتی برای مسائل سخت، جواب باید در کمتر از **۶۰ ثانیه** بیاد.  
⏳ اگر اینطور نیست، یعنی وقت **بهینه‌سازی** رسیده!

</details>

---

<details>
<summary><b>🔄 ۲. وقتی بیشتر طول می‌کشد</b></summary>

⚡ اگر اجرای کد بیشتر از یک دقیقه طول کشید، الگوریتمت رو دوباره بررسی کن.  
💬 از ایده‌های دیگران الهام بگیر ولی **کپی نکن**.

</details>

---

<details>
<summary><b>🌐 ۳. استفاده از اینترنت و هوش مصنوعی</b></summary>

🌍 تحقیق کردن فوق‌العاده است.  
🚫 اما استفاده مستقیم از جواب آماده یعنی **یادگیری صفر**.  
🤖 از AI به‌عنوان **راهنما** استفاده کن، نه جایگزین فکر کردن.

</details>

---

<details>
<summary><b>🎯 ۴. وقتی جواب قبول نمی‌شود</b></summary>

📌 در مسائل تازه احتمال خطا هست.  
📊 اما اگر خیلی‌ها درست جواب دادند، مشکل از **کد تو**ست.

</details>

---

<details>
<summary><b>🏆 ۵. نکات طلایی موفقیت</b></summary>

✅ مسئله را چند بار بخوان.  
📝 از مثال‌ها یادداشت‌برداری کن.  
🔍 ایده را با ورودی‌های کوچک تست کن.  
📚 پیش‌زمینه لازم را یاد بگیر.  
📏 خروجی را با مثال‌ها تطبیق بده.  
⏱️ اگر بیش از یک دقیقه طول می‌کشد، **استراتژی را عوض کن**.

</details>

---

<h3 align="center">💬 نکته پایانی</h3>

<p align="center">
👨‍💻 برنامه‌نویس واقعی کسیه که <b>کد می‌زنه</b>، نه فقط نگاه می‌کنه. 💻🔥
</p>

-----------------------------------------------------------------------                  **بخش مسابقه کدنویسی** -----------------------------------------------------------
# 🏆 Code Challenge

## 🟩 سوال ساده
> [!NOTE]
> ### 🔢 مجموع مضرب‌های 3 یا 5
> اگر تمام اعداد طبیعی زیر 10 که مضرب‌های 3 یا 5 هستند را فهرست کنیم، به اعداد 3، 5، 6 و 9 می‌رسیم.  
> مجموع این مضرب‌ها 23 است.
> 
> 🏆 **هدف**:  
> مجموع تمام مضرب‌های 3 یا 5 زیر 1000 را بیابید.

---

## 🟨 سوال متوسط
> [!IMPORTANT]
> ### 🔁 چالش پالیندروم
> یک **عدد پالیندرومیک** در هر دو جهت یکسان خوانده می‌شود.  
> مثال: `9009 = 91 × 99`
> 
> 🏆 **هدف**:  
> بزرگترین پالیندروم ساخته شده از حاصل‌ضرب اعداد دو رقمی را پیدا کنید.

---

## 🟥 سوال سخت
> [!WARNING]
> ### 🤖 چالش ویژه
> این بخش برای سوالات سنگین‌تر و پروژه‌های کوچک برنامه‌نویسی رزرو شده است.
> (به‌زودی سوال اضافه می‌شود...)
-------------------------------------------------------------------------------------------------
# 🎮 Beginner Python Loop Games

Welcome to **Beginner Python Loop Games**! 🚀
This project includes **5 simple and fun Python games** designed for **absolute beginners** to practice **loops (`for`, `while`) and conditions**.

Each game is small, interactive, and easy to understand — perfect for students just starting their coding journey. 💻✨

---

## 📌 Table of Contents

* [Game 1: Number Guessing](#-game-1-number-guessing)
* [Game 2: Multiplication Table](#-game-2-multiplication-table)
* [Game 3: Countdown](#-game-3-countdown)
* [Game 4: Secret Word Guessing](#-game-4-secret-word-guessing)
* [Game 5: Star Pyramid](#-game-5-star-pyramid)
* [Purpose](#-purpose)
* [How to Run](#-how-to-run)

---

## 🎲 Game 1: Number Guessing

🔹 The computer selects a **random number** between 1 and 10.
🔹 The player guesses until they find the correct number.
🔹 The program shows how many attempts were made.

**Concepts:** `while loop`, `if-else`, `random`, user input.

---

## 🎲 Game 2: Multiplication Table

🔹 The player enters a number.
🔹 The program prints the multiplication table (1 → 10).

**Concepts:** `for loop`, user input, string formatting.

---

## 🎲 Game 3: Countdown

🔹 The player enters a number.
🔹 The program counts down to 0.
🔹 Prints **Boom!** at the end.

**Concepts:** `for loop` with negative step.

---

## 🎲 Game 4: Secret Word Guessing

🔹 The computer has a **secret word** (default: `python`).
🔹 The player keeps guessing until correct.

**Concepts:** `while loop`, string comparison.

---

## 🎲 Game 5: Star Pyramid

🔹 The player enters a number.
🔹 The program prints a pyramid of stars `*`.

Example (4 rows):

```text
*
**
***
****
```

**Concepts:** `for loop`, string multiplication.

---

## 🎯 Purpose

These games are made for **students who just learned loops and conditions**.
The aim is to practice programming in a **fun and engaging way**. 🌟

---

## ⚡ How to Run

1. Install [Python 3](https://www.python.org/downloads/).
2. Save the file as `beginner_games.py`.
3. Run it in the terminal:

   ```bash
   python beginner_games.py
   ```

---

## ✨ Practice More (Project Euler)
[![Project Euler](https://img.shields.io/badge/Project_Euler-About-ff69b4?logo=project-euler&logoColor=white&style=for-the-badge)](https://projecteuler.net/about)


> Challenge your students with math+coding puzzles.

<a href="https://projecteuler.net/about" target="_blank" rel="noopener noreferrer">
  <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" width="20" height="20" alt="blink" />
  <strong>Project Euler – About</strong>
</a>

> If the animation doesn't show on your platform, the link still works: `https://projecteuler.net/about`

---

## 📷 Screenshots (Optional)

🎨

---

## 💡 Author

👨‍💻 Made by **Farshid** for his awesome students. ✨

👨‍💻 Made by **Farshid** for his awesome students. ✨

---------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------


![بازدیدکننده‌ها](https://visitor-badge.laobi.icu/badge?page_id=farshid-azady.Python-Primary)




