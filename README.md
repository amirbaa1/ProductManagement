# پروژه مدیریت انبار و فروشگاهی
* هدف اصلی این پروژه، مدیریت انبار و محصولات در فروشگاه آنلاین است. کاربران می‌توانند موجودی انبار را به روزرسانی کنند، سفارشات مشتریان را پیگیری کنند و مشتریان نیز قادر خواهند بود سفارشات خود را ثبت کرده و وضعیت سفارشات خود را بررسی کنند.
----
## اجرا دمو
[https://amirbaa1.pythonanywhere.com](https://amirbaa1.pythonanywhere.com)

 <table>
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">user</th>
                        <th scope="col">پسورد</th>
                        <th scope="col">شهر</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <th scope="row">1</th>
                        <td>amir_tehran</td>
                        <td>Amir$$1379</td>
                        <td>تهران</td>
                    </tr>
                    </tbody>
                    <tbody>
                        <tr>
                        <th scope="row">2</th>
                        <td>amir_tabriz</td>
                        <td>Amir$$1379</td>
                        <td>تبریز</td>
                    </tr>
                    </tbody>

</table>


----
 ## اجرای سرور سایت 
برای اجرای سرور سایت، دستور زیر را در ترمینال اجرا کنید:
```python
python manage.py runserver
```
و ادرس لینک `http://127.0.0.1:8000/`وصل شوید.

---
## بخش مدیریت (admin) 
با ادرس لینک سایت ادمین `http://127.0.0.1:8000/admin` برای مدیریت انبار وارد شوید .
هم میتونید وارد سایت بشید و لاگین کنید. `http://127.0.0.1:8000/accounts/login`
 <table>
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">user_admin</th>
                        <th scope="col">پسورد</th>
                        <th scope="col">وظیفه</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <th scope="row">1</th>
                        <td>admin</td>
                        <td>123</td>
                        <td>مدیریت کل سایت و انبار</td>
                    </tr>
                    </tbody>
                    <tbody>
                        <tr>
                        <th scope="row">2</th>
                        <td>admin2</td>
                        <td>123</td>
                        <td>اضافه کردن محصولات و تغییر قیمت</td>
                    </tr>
                    </tbody>
                    <tbody>
                        <tr>
                        <th scope="row">3</th>
                        <td>admin3</td>
                        <td>123</td>
                        <td>بررسی و تغییر وضعیت سفارش</td>
                    </tr>
                    </tbody>
</table>


---
## Front-End
قسمت رابط کاربری (Front-End)
این پروژه از زبان‌ها و فریمورک‌های زیر در قسمت رابط کاربری استفاده می‌کند:
* html
* css
* bootstrap


----
## ویژگی های سایت برای مشتری
* اضافه کردن سبد خرید 
* دیدن سفارش که خرید شده در پروفایل
* دیدن وضعیت سفارش 
