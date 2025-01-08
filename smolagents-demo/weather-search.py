from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional
import requests
import json
import os
from google.colab import userdata

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

model = LiteLLMModel(model_id="gpt-4o-mini")

# 设置API key，从此处获取API key：https://home.openweathermap.org/api_keys
OPENWEATHER_API_KEY = userdata.get('OPENWEATHER_API_KEY')


@tool
def get_weather(location: str, celsius: Optional[bool] = True) -> str:
    """
    获取指定位置的实时天气信息

    Args:
        location: 位置名称(城市名)
        celsius: 是否使用摄氏度(默认True)
    """
    try:
        # 1. 先通过地理编码API获取位置的经纬度
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPENWEATHER_API_KEY}"
        geo_response = requests.get(geocoding_url)
        geo_data = geo_response.json()

        if not geo_data:
            return f"无法找到位置: {location}"

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # 2. 调用天气API获取天气数据
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
        response = requests.get(weather_url)
        data = response.json()

        # 3. 温度转换(开氏度转换为摄氏度或华氏度)
        temp_k = data['main']['temp']
        if celsius:
            temp = temp_k - 273.15
            temp_unit = "°C"
        else:
            temp = (temp_k - 273.15) * 9 / 5 + 32
            temp_unit = "°F"

        # 4. 格式化天气信息
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_info = (
            f"当前{location}的天气情况:\n"
            f"- 天气状况: {weather_desc}\n"
            f"- 温度: {temp:.1f}{temp_unit}\n"
            f"- 湿度: {humidity}%\n"
            f"- 风速: {wind_speed}m/s"
        )

        return weather_info

    except Exception as e:
        return f"获取天气信息时发生错误: {str(e)}"


agent = ToolCallingAgent(tools=[get_weather], model=model)

# 测试
print(agent.run("What's the weather like in Paris?"))
print(agent.run("What's the weather like in New York? Use Fahrenheit."))

