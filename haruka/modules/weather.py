import pyowm
import requests

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import run_async

from haruka import dispatcher, API_WEATHER, API_ACCUWEATHER
from haruka.modules.disable import DisableAbleCommandHandler


@run_async
def weather(bot, update, args):
    spam = (update.effective_message.text, update.effective_message.from_user.id, update.effective_chat.id, update.effective_message)
    if spam == True:
        return
    location = " ".join(args)
    if location.lower() == bot.first_name.lower():
        update.effective_message.reply_text(update.effective_message, "I will keep watching when I am happy or sad!")
        bot.send_sticker(update.effective_chat.id, BAN_STICKER)
        return

    try:
        owm = pyowm.OWM(API_WEATHER, language='en')
        observation = owm.weather_at_place(location)
        cuacanya = observation.get_weather()
        obs = owm.weather_at_place(location)
        lokasi = obs.get_location()
        lokasinya = lokasi.get_name()
        temperatur = cuacanya.get_temperature(unit='celsius')['temp']

        # Weather symbol
        statusnya = ""
        cuacaskrg = cuacanya.get_weather_code()
        if cuacaskrg < 232:  # Rain storm
            statusnya += "⛈️ "
        elif cuacaskrg < 321:  # Drizzle
            statusnya += "🌧️ "
        elif cuacaskrg < 504:  # It's raining
            statusnya += "🌦️ "
        elif cuacaskrg < 531:  # Cloudy rain
            statusnya += "⛈️ "
        elif cuacaskrg < 622:  # Snow
            statusnya += "🌨️ "
        elif cuacaskrg < 781:  # Atmosphere
            statusnya += "🌪️ "
        elif cuacaskrg < 800:  # Bright
            statusnya += "🌤️ "
        elif cuacaskrg < 801:  # A little cloudy
            statusnya += "⛅️ "
        elif cuacaskrg < 804:  # Cloudy
            statusnya += "☁️ "
        statusnya += cuacanya._detailed_status


        update.message.reply_text(update.effective_message, "{} today is {}, around {}°C.\n").format(lokasinya,
                statusnya, temperatur)

    except pyowm.exceptions.api_call_error.APICallError:
        update.effective_message.reply_text(update.effective_message, "Write the location to check the weather")
    except pyowm.exceptions.api_response_error.NotFoundError:
        update.effective_message.reply_text(update.effective_message, "Sorry, location not found 😞")
    else:
        return

@run_async
def accuweather(bot, update, args):
    chat_id = update.effective_chat.id
    message = update.effective_message
    spam = (update.effective_message.text, update.effective_message.from_user.id, update.effective_chat.id, update.effective_message)
    if spam == True:
        return
    if args == []:
        return update.effective_message.reply_text(update.effective_message, "Enter the name of the location to check the weather!")
    location = " ".join(args)
    if location.lower() == bot.first_name.lower():
        update.effective_message.reply_text(update.effective_message, "I will keep watching when I am happy or sad!")
        bot.send_sticker(update.effective_chat.id, BAN_STICKER)
        return

    if True:
        url = "http://api.accuweather.com/locations/v1/cities/search.json?q={}&apikey={}".format(location, API_ACCUWEATHER)
        headers = {'Content-type': 'application/json'}
        r = requests.get(url, headers=headers)
        try:
            data = r.json()[0]
        except:
            return update.effective_message.reply_text(update.effective_message, "Sorry, location not found 😞")
        locid = data.get('Key')
        urls = "http://api.accuweather.com/currentconditions/v1/{}.json?apikey={}&language={}&details=true&getphotos=true".format(locid, API_ACCUWEATHER)
        rs = requests.get(urls, headers=headers)
        datas = rs.json()[0]

        if datas.get('WeatherIcon') <= 44:
            icweather = "☁"
        elif datas.get('WeatherIcon') <= 42:
            icweather = "⛈"
        elif datas.get('WeatherIcon') <= 40:
            icweather = "🌧"
        elif datas.get('WeatherIcon') <= 38:
            icweather = "☁"
        elif datas.get('WeatherIcon') <= 36:
            icweather = "⛅"
        elif datas.get('WeatherIcon') <= 33:
            icweather = "🌑"
        elif datas.get('WeatherIcon') <= 32:
            icweather = "🌬"
        elif datas.get('WeatherIcon') <= 31:
            icweather = "⛄"
        elif datas.get('WeatherIcon') <= 30:
            icweather = "🌡"
        elif datas.get('WeatherIcon') <= 29:
            icweather = "☃"
        elif datas.get('WeatherIcon') <= 24:
            icweather = "❄"
        elif datas.get('WeatherIcon') <= 23:
            icweather = "🌥"
        elif datas.get('WeatherIcon') <= 19:
            icweather = "☁"
        elif datas.get('WeatherIcon') <= 18:
            icweather = "🌨"
        elif datas.get('WeatherIcon') <= 17:
            icweather = "🌦"
        elif datas.get('WeatherIcon') <= 15:
            icweather = "⛈"
        elif datas.get('WeatherIcon') <= 14:
            icweather = "🌦"
        elif datas.get('WeatherIcon') <= 12:
            icweather = "🌧"
        elif datas.get('WeatherIcon') <= 11:
            icweather = "🌫"
        elif datas.get('WeatherIcon') <= 8:
            icweather = "⛅️"
        elif datas.get('WeatherIcon') <= 5:
            icweather = "☀️"
        else:
            icweather = ""

        cuaca = "*{} {}*\n".format(icweather, datas.get('WeatherText'))
        cuaca += (update.effective_message, "*Temperature:* `{}°C`/`{}°C`\n").format(datas.get('Temperature').get('Metric').get('Value'), datas.get('Temperature').get('Imperial').get('Value'))
        cuaca += (update.effective_message, "*Humidity:* `{}`\n").format(datas.get('RelativeHumidity'))
        direct = "{}".format(datas.get('Wind').get('Direction').get('English'))
        direct = direct.replace("N", "↑").replace("E", "→").replace("S", "↓").replace("W", "←")
        cuaca += (update.effective_message, "*Wind:* `{} {} km/h` | `{} mi/h`\n").format(direct, datas.get('Wind').get('Speed').get('Metric').get('Value'), datas.get('Wind').get('Speed').get('Imperial').get('Value'))
        cuaca += (update.effective_message, "*UV level:* `{}`\n").format(datas.get('UVIndexText'))
        cuaca += (update.effective_message, "*Pressure:* `{}` (`{} mb`)\n").format(datas.get('PressureTendency').get('LocalizedText'), datas.get('Pressure').get('Metric').get('Value'))

        lok = []
        lok.append(data.get('LocalizedName'))
        lok.append(data.get('AdministrativeArea').get('LocalizedName'))
        for x in reversed(range(len(data.get('SupplementalAdminAreas')))):
            lok.append(data.get('SupplementalAdminAreas')[x].get('LocalizedName'))
        lok.append(data.get('Country').get('LocalizedName'))
        teks = (update.effective_message, "*Current weather in {}*\n").format(data.get('LocalizedName'))
        teks += "{}\n".format(cuaca)
        teks += (update.effective_message, "*Location:* `{}`\n\n").format(", ".join(lok))

        # try:
        #     bot.send_photo(chat_id, photo=datas.get('Photos')[0].get('LandscapeLink'), caption=teks, parse_mode="markdown", reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="More info", url=datas.get('Link'))]]))
        # except:
        update.message.reply_text(teks, parse_mode="markdown", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="More info", url=datas.get('Link'))]]))


__help__ = """
 - /weather <location>: get weather info in certain places
 """

__mod_name__ = "Weather"

WEATHER_HANDLER = DisableAbleCommandHandler(["weather"], accuweather, pass_args=True)


dispatcher.add_handler(WEATHER_HANDLER)
