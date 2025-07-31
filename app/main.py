from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

def get_city_times():
    cities = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Dubai": "Asia/Dubai",
        "Mumbai": "Asia/Kolkata",
        "Tokyo": "Asia/Tokyo",
        "Singapore": "Asia/Singapore",
        "Bangkok": "Asia/Bangkok",
        "Riyadh": "Asia/Riyadh",
        "Toronto": "America/Toronto"
    }

    time_data = []

    for city, tz in cities.items():
        tz_obj = pytz.timezone(tz)
        city_time = datetime.now(tz_obj)

        is_daytime = 6 <= city_time.hour < 18

        time_data.append({
            "city": city,
            "time": city_time.strftime("%I:%M:%S %p"),
            "date": city_time.strftime("%A, %d %B %Y"),
            "icon": "🌞" if is_daytime else "🌙"
        })

    return time_data

@app.route("/")
def home():
    times = get_city_times()
    return render_template("index.html", times=times)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")