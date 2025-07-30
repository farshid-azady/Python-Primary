
```diff


!   اولویت عملگر ها


```

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
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```diff
-  اولویت عملگر ها در پایتون
+  اگر سوالی داشتید کامنت کنید.

```


مشکلی پیش اومد که نتونستم فایل رو همین الان ذخیره کنم، ولی نگران نباش، محتوای قالب‌بندی شده رو اینجا کامل برات می‌فرستم تا بتونی راحت کپی و داخل فایل README.md پروژه‌ات بذاری.

---

```markdown
# تمرین‌های if-elif-else در پایتون 🐍

مجموعه‌ای از تمرین‌های ساده تا پیشرفته برای آموزش شرط‌ها در زبان برنامه‌نویسی پایتون، مناسب برای دانشجویان.

---

<div dir="rtl">

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۱: عدد مثبت یا منفی یا صفر</span>

<br><br>
برنامه‌ای بنویسید که یک عدد از کاربر بگیرد و مشخص کند آن عدد <b>مثبت</b>، <b>منفی</b> یا <b>صفر</b> است.

<br><br>
<em style="color:#555;">راهنمایی: برای بررسی مثبت یا منفی بودن عدد، از شرط <code>if num &gt; 0</code> و برای صفر بودن از <code>else</code> استفاده کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۲: تعیین نمره و وضعیت دانشجو</span>

<br><br>
نمره‌ای بین ۰ تا ۲۰ از کاربر دریافت کنید. سپس بر اساس شرط‌های زیر، وضعیت دانشجو را چاپ کنید:<br>
- کمتر از ۱۰ → مردود<br>
- بین ۱۰ تا ۱۵ → قابل قبول<br>
- بین ۱۵ تا ۱۷ → خوب<br>
- بین ۱۷ تا ۲۰ → عالی

<br><br>
<em style="color:#555;">راهنمایی: می‌توانید از زنجیره شرط‌های <code>elif</code> استفاده کنید تا بازه‌ها را بررسی کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۳: ماشین‌حساب ساده</span>

<br><br>
دو عدد و یک عملگر ( + , - , * , / ) از کاربر بگیرید و عملیات را انجام دهید.

<br><br>
<em style="color:#555;">راهنمایی: با استفاده از شرط‌ها، عملگر ورودی را بررسی و عملیات مربوطه را انجام دهید. حتما بررسی کنید که تقسیم بر صفر انجام نشود.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۴: تعیین فصل با شماره ماه</span>

<br><br>
شماره ماه (۱ تا ۱۲) را بگیرید و فصل آن را مشخص کنید. اگر نامعتبر بود پیام خطا چاپ شود.

<br><br>
<em style="color:#555;">راهنمایی: از بازه‌های عددی با شرط‌های <code>and</code> در <code>if</code> و <code>elif</code> استفاده کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۵: بررسی رمز عبور معتبر</span>

<br><br>
رمز عبوری بگیرید و بررسی کنید:<br>
- حداقل ۸ کاراکتر باشد.<br>
- شامل عدد باشد.<br>
- شامل حروف بزرگ باشد.

<br><br>
<em style="color:#555;">راهنمایی: از توابع <code>len()</code>، <code>any()</code> و متدهای <code>isdigit()</code> و <code>isupper()</code> کمک بگیرید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۶: محاسبه کرایه تاکسی</span>

<br><br>
با توجه به فاصله طی‌شده، کرایه محاسبه شود:<br>
- تا ۳ کیلومتر: ۱۰هزار تومان<br>
- از ۳ تا ۱۰: هر کیلومتر ۸هزار<br>
- بیشتر از ۱۰: هر کیلومتر ۶هزار

<br><br>
<em style="color:#555;">راهنمایی: مسئله شامل چند بازه فاصله است. برای هر بازه مبلغ جداگانه محاسبه کنید و جمع کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۷: دسته‌بندی سن افراد</span>

<br><br>
سن فرد را گرفته و در یکی از گروه‌های کودک، نوجوان، جوان، میانسال یا سالمند دسته‌بندی کنید.

<br><br>
<em style="color:#555;">راهنمایی: از شرط‌های ترتیبی استفاده کنید و ابتدا مقدار منفی را چک کنید. سپس هر بازه را با شرط <code>elif</code> مشخص کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۸: تعیین نوع مثلث</span>

<br><br>
سه ضلع بگیرید، اگر مثلث قابل ساخت بود، نوع آن (متساوی‌الاضلاع، متساوی‌الساقین، مختلف‌الاضلاع) را مشخص کنید.

<br><br>
<em style="color:#555;">راهنمایی: برای تشخیص مثلث، شرط تشکیل مثلث (مجموع هر دو ضلع &gt; ضلع سوم) را بررسی کنید. سپس نوع مثلث را با مقایسه اضلاع مشخص کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۹: محاسبه مالیات بر درآمد</span>

<br><br>
درآمد را از کاربر بگیرید و با توجه به بازه درآمد، درصد مناسب مالیات را محاسبه کنید.

<br><br>
<em style="color:#555;">راهنمایی: شرط‌های <code>if</code> برای هر بازه را بررسی کنید و درصد مالیات را متناسب با درآمد محاسبه کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۱۰: تعیین روز هفته با عدد</span>

<br><br>
عددی بین ۱ تا ۷ از کاربر بگیرید و روز هفته معادل آن را چاپ کنید.

<br><br>
<em style="color:#555;">راهنمایی: از زنجیره <code>if-elif</code> برای نگاشت عدد به روز هفته استفاده کنید. عدد خارج از بازه را مدیریت کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:15px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۱۱: اعتبارسنجی کد ملی</span>

<br><br>
بررسی کنید کد ملی ۱۰ رقمی و فقط عددی باشد.

<br><br>
<em style="color:#555;">راهنمایی: از تابع <code>len()</code> برای طول و متد <code>isdigit()</code> برای عدد بودن رشته استفاده کنید.</em>
</div>

---

<div style="background-color:#f0f8ff; border:1px solid #a0c4ff; padding:15px; margin-bottom:30px; border-radius:8px;">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="40" alt="Python Logo" style="vertical-align:middle; margin-left:10px;">
<span style="font-size:1.2em; font-weight:bold;">تمرین ۱۲: ورود دومرحله‌ای (رمز + کد یک‌بار مصرف)</span>

<br><br>
ابتدا رمز و سپس کد یک‌بار مصرف از کاربر بگیرید و اعتبارسنجی کنید.

<br><br>
<em style="color:#555;">راهنمایی: از ساختار شرطی تو در تو استفاده کنید. ابتدا رمز را چک کنید، سپس کد یک‌بار مصرف.</em>
</div>

</div>
```

---


