from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de Mexico: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

lima_timezone = pytz.timezone("America/Lima")
lima_date = datetime.now(lima_timezone)
print("Lima: ", lima_date.strftime("%d/%m/%Y, %H:%M:%S"))
