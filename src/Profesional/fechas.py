from datetime import datetime

my_datetime = datetime().now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%y')
print(f'formato LATAM:{my_str}')

my_str = my_datetime.strftime('%d/%m/%y')
print(f'formato USA:{my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'formanato Random: Estamos en el año 2020')

#* %Y (Year)
#* %m (Month)
#* %Y (Day)
#* %Y (Hour)
#* %Y (Minute)
#* %Y (Second)