from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()

    if not city:
        city = "Locquirec"

    try:
        weather_data = get_current_weather(city)
        if "cod" not in weather_data or weather_data["cod"] != 200:
            return render_template("city-not-found.html", city=city)

        return render_template(
            "weather.html",
            title=weather_data.get("name", "Unknown City"),
            status=weather_data.get("weather", [{}])[0].get("description", "No data").capitalize(),
            temp=f"{weather_data['main'].get('temp', 'N/A'):.1f}",
            feels_like=f"{weather_data['main'].get('feels_like', 'N/A'):.1f}",
        )
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    print("\n ** Starting the server ** \n")
    serve(app, host="0.0.0.0", port=8000)
