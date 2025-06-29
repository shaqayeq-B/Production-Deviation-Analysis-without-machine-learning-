# تحلیل انحراف قطعات یدکی خودرو

این پروژه با استفاده از پایتون، انحراف بین مقادیر مورد انتظار (Expected) و مقادیر واقعی (Actual) برای قطعات یدکی خودرو را تحلیل می‌کند.

## 📂 فایل‌ها

- `part_deviation_data.csv`: فایل داده‌ها شامل نام قطعه، مقدار مورد انتظار و مقدار واقعی  
- `part_deviation_results.csv`: خروجی تحلیل شامل انحراف و قدر مطلق انحراف برای هر قطعه  
- `analysis.py`: کد اصلی پایتون برای خواندن داده‌ها، محاسبه‌ی انحراف و رسم نمودار  
- `README.md`: همین فایل توضیحاتی

## 🧪 محاسبات انجام‌شده

- **Deviation** = Actual - Expected  
- **Absolute Deviation** = |Deviation|  
- **میانگین انحراف** (Mean Deviation)  
- **انحراف معیار** (Standard Deviation)  
- **میانگین مربعات خطا** (Mean Squared Error - MSE)

## 📊 نمودارها

در پایان اجرای برنامه، دو نمودار نمایش داده می‌شود:

1. **نمودار انحراف** (Deviation): نشان‌دهنده‌ی تفاوت مقدار واقعی و مورد انتظار  
2. **نمودار قدر مطلق انحراف** (Absolute Deviation): شدت انحراف بدون در نظر گرفتن جهت

## 🛠 ابزارها و کتابخانه‌ها

- Python 3.x  
- pandas  
- matplotlib  
- numpy

## ▶️ نحوه اجرا

برای اجرای برنامه کافیست دستور زیر را وارد کنید:

```bash
python analysis.py
