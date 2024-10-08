import datetime

def date_to_day(date):
    split_day = date.split("/") ## output = ["14", "07"]
    day = int(split_day[0]) ## output = 14
    month = int(split_day[1]) ## output = 7

    year = datetime.datetime.now().year
    date_obj = datetime.datetime(year, month, day)

    day_of_year = date_obj.timetuple().tm_yday

    return day_of_year


def day_to_star_sign(day):
    if 1 <= day <= 19:
        return "Capricorn"
    elif 20 <= day <= 49:
        return "Aquarius"
    elif 50 <= day <= 79:
        return "Pisces"
    elif 80 <= day <= 109:
        return "Aries"
    elif 110 <= day <= 140:
        return "Taurus"
    elif 141 <= day <= 172:
        return "Gemini"
    elif 173 <= day <= 203:
        return "Cancer"
    elif 204 <= day <= 234:
        return "Leo"
    elif 235 <= day <= 266:
        return "Virgo"
    elif 267 <= day <= 296:
        return "Libra"
    elif 297 <= day <= 326:
        return "Scorpio"
    elif 327 <= day <= 356:
        return "Sagittarius"
    else:
        return "Capricorn"


while 1 == 1:

    try:
        date = input("Enter your birthday in format DD/MM: ")

        day = date_to_day(date)


        star_sign = day_to_star_sign(day)
        print("Your star sign is", star_sign)
        
    except:
        print("Invalid date format")