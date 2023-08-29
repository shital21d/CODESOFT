import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    api_key = "b4edcb28e1aa0b5c7b0e4dfb42586798"
    location = location_entry.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        result_text.set(f"Weather in {location}:\n\n"
                        f"Description: {weather_description}\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s")
    else:
        messagebox.showerror("Error", "Weather data not available.")

# Create the main window
root = tk.Tk()
root.title("Weather Checker")
root.geometry("500x250")

# Create and place widgets
location_label = tk.Label(root, text="Enter city or zip code:")
location_label.pack(pady=5)

location_entry = tk.Entry(root)
location_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Show Weather Report", command=get_weather)
get_weather_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=10)

root.mainloop()
