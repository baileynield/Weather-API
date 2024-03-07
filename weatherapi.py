import requests

class Day():
    def __init__(self):
        pass

    def get_data_for_coordinates(latitude: float, longitude: float):

        url = f"https://api.weather.gov/points/{latitude},{longitude}"

        response = requests.get(url=url)
        weather_data = response.json()

        forecast_url = weather_data["properties"]["forecastHourly"]
        response = requests.get(url=forecast_url)
        forecast = response.json()
        print()
class CurrentConditions(Day):
        
    def period():
        periods = Day.get_data_for_coordinates.forecast["properties"]["periods"]
        current_period = periods[0]
    def temp():
        current_temperature = CurrentConditions.current_period["temperature"]
    def wind_speed():
        current_wind_speed = CurrentConditions.current_period["windSpeed"]
    def weather():
        weather_condition = CurrentConditions.current_period["shortForecast"]



def main():
    latitude = 19.705520
    longitude = -155.085918
    Day.get_data_for_coordinates(latitude, longitude)
    print()
    print(f"The current temperature is {CurrentConditions.temp}")
    print(f"The current wind speed is {CurrentConditions.wind_speed}")


if __name__ == "__main__":
    main()