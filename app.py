from flask import Flask, render_template_string
import os

app = Flask(__name__)

# كتابة HTML مباشرة في الكود
html_content = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقعي ثلاثي الأبعاد</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            overflow: hidden; 
            position: relative;
            background: #111; /* خلفية داكنة */
        }
        .background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: hidden;
        }
        .shape { /* باقي التنسيقات كما هي */
        }
        /* باقي التنسيقات هنا */
        .video-container {
            position: relative;
            z-index: 1;
            margin: 20px 0; /* إضافة مسافة بين الفيديو وباقي المحتوى */
        }
        video {
            width: 100%; /* عرض الفيديو بالكامل */
            max-width: 600px; /* تحديد أقصى عرض */
            border-radius: 10px; /* إضافة زوايا دائرية للفيديو */
        }
    </style>
</head>
<body>
    <div class="background">
        <div class="shape large-square"></div>
        <div class="shape small-square"></div>
        <div class="triangle triangle1"></div>
        <div class="triangle triangle2"></div>
        <div class="triangle triangle3"></div>
    </div>
    <div class="container">
        <h1>Programmer Muhammad Abdullah ايوا يصحبي عامل ايه في موقع</h1>
        <div class="video-container">
            <video controls>
                <source src="https://www.dropbox.com/scl/fi/32u6ud295izcxqdjj64ae/4_5896868210531108401.mp4?rlkey=e9ocelr312f6rjrouf6um3gjb&dl=1" type="video/mp4">
                عذراً، متصفحك لا يدعم تشغيل الفيديو.
            </video>
        </div>
        <p>تفضل بزيارة روابط التواصل الاجتماعي أدناه:</p>
        <ul>
            <li>
                <a href="https://www.facebook.com" target="_blank">
                    Facebook
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="فيسبوك">
                </a>
            </li>
            <li>
                <a href="https://www.instagram.com" target="_blank">
                    Instagram
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="إنستغرام">
                </a>
            </li>
            <li>
                <a href="https://www.tiktok.com" target="_blank">
                    TikTok
                    <img src="https://www.dropbox.com/scl/fi/lypqfmsyx4fbvzrcvs3jo/hirphn.jpg?rlkey=reyfi49dmstt3z8z0tdqnnosm&dl=1" alt="تيك توك">
                </a>
            </li>
            <li>
                <a href="https://telegram.org" target="_blank">
                    Telegram
                    <img src="https://www.dropbox.com/scl/fi/lypqfmsyx4fbvzrcvs3jo/hirphn.jpg?rlkey=reyfi49dmstt3z8z0tdqnnosm&dl=1" alt="تيلجرام">
                </a>
            </li>
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # استخدم المنفذ المحدد من قبل البيئة
    app.run(host='0.0.0.0', port=port)  # استمع على كل الواجهات
