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
        .shape {
            position: absolute;
            background-color: black;
            z-index: 0;
            opacity: 0.8; /* زيادة الشفافية */
        }
        .large-square {
            width: 250px;
            height: 250px;
            top: 30%;
            left: 25%;
            animation: rotateLarge 10s infinite linear;
        }
        .small-square {
            width: 150px;
            height: 150px;
            top: 20%;
            left: 70%;
            animation: rotateSmall 6s infinite linear;
        }
        .triangle {
            width: 0; 
            height: 0; 
            border-left: 75px solid transparent; 
            border-right: 75px solid transparent; 
            border-bottom: 130px solid #fff; 
            position: absolute;
            animation: moveTriangle 4s infinite alternate;
        }
        .triangle1 { top: 50%; left: 15%; }
        .triangle2 { top: 20%; left: 55%; }
        .triangle3 { top: 70%; left: 40%; }
        @keyframes rotateLarge {
            from { transform: rotateY(0deg); }
            to { transform: rotateY(360deg); }
        }
        @keyframes rotateSmall {
            from { transform: rotateY(0deg); }
            to { transform: rotateY(-360deg); }
        }
        @keyframes moveTriangle {
            0% { transform: translateY(0) rotate(0deg); }
            100% { transform: translateY(-20px) rotate(180deg); }
        }
        .container {
            text-align: center;
            color: white;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 20px;
            position: relative;
            z-index: 1;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% {
                background-color: rgba(0, 0, 0, 0.5);
            }
            50% {
                background-color: rgba(50, 50, 50, 0.7);
            }
        }
        h1 { 
            color: #ffdd57; 
            margin: 0 0 20px; 
            animation: colorChange 3s infinite alternate;
        }
        @keyframes colorChange {
            0% { color: #ff5733; }
            25% { color: #33ff57; }
            50% { color: #3357ff; }
            75% { color: #f0e68c; }
            100% { color: #ff33a1; }
        }
        a { 
            text-decoration: none; 
            color: #007bff; 
            padding: 10px 15px; 
            border-radius: 5px; 
            transition: background 0.3s;
            display: flex;
            align-items: center;
        }
        a:hover { 
            background: rgba(0, 123, 255, 0.1); 
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        img {
            width: 30px; /* عرض الصورة */
            height: 30px; /* ارتفاع الصورة */
            margin-left: 10px; /* مسافة بين النص والصورة */
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
        <h1>مرحبًا بك في موقعي ثلاثي الأبعاد!</h1>
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
                    تيك توك
                    <img src="https://www.dropbox.com/scl/fi/lypqfmsyx4fbvzrcvs3jo/hirphn.jpg?rlkey=reyfi49dmstt3z8z0tdqnnosm&dl=1" alt="تيك توك">
                </a>
            </li>
            <li>
                <a href="https://telegram.org" target="_blank">
                    تيلجرام
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
    port = int(os.environ.get("PORT", 5098))  # استخدم المنفذ المحدد من قبل البيئة
    app.run(host='0.0.0.0', port=port)  # استمع على كل الواجهات
