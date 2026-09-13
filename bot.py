from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = "8874094491:AAGkkRWcyEvlz24_fxolIVg8L2sZbbIGhzM"
CHAT_ID = "-1004371910286"


@app.route("/application", methods=["POST"])
def application():
    try:
        data = request.json

        print("========== НОВАЯ ЗАЯВКА ==========")
        print("DATA:", data)

        name = data["name"]
        age = data["age"]
        email = data["email"]
        telegram = data["telegram"]
        direction = data["direction"]
        reason = data["reason"]

        message = f"""
📩 НОВАЯ ЗАЯВКА

👤 Имя: {name}
🎂 Возраст: {age}
📧 Email: {email}
📱 Telegram: {telegram}
💻 Направление: {direction}

📝 О себе:
{reason}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        response = requests.post(
            url,
            json={
                "chat_id": -1004371910286,
                "text": message
            }
        )

        print("TELEGRAM RESPONSE:", response.text)

        if response.ok:
            print("✅ ОТПРАВЛЕНО В TELEGRAM")
            return jsonify({"message": "Заявка отправлена!"})

        print("❌ TELEGRAM ОТКАЗАЛ")
        return jsonify({
            "message": "Telegram error: " + response.text
        }), 500

    except Exception as e:
        print("❌ ОШИБКА:", repr(e))

        return jsonify({
            "message": str(e)
        }), 500


app.run(host="127.0.0.1", port=5000, debug=True)