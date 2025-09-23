import random
from datetime import datetime, timedelta
import string

def rand_str(n):
    return ''.join(random.choices(string.ascii_uppercase, k=n))

def rand_date_range(start="2023-01-01", end="2025-12-31", with_time=True):
    start_dt = datetime.fromisoformat(start)
    end_dt   = datetime.fromisoformat(end)
    delta    = end_dt - start_dt
    rand_dt  = start_dt + timedelta(seconds=random.randint(0, int(delta.total_seconds())))
    return rand_dt.strftime("%Y-%m-%d %H:%M:%S") if with_time else rand_dt.date()

# Data Pools
countries = [
    'Kazakhstan','USA','Canada','UK','Germany','France','Japan','Brazil',
    'Australia','Italy','Spain','India','UAE','South Korea','Mexico'
]

airline_names = [
    "SkyJet Airways","AeroWorld","Blue Horizon","Global Wings","Air Nova",
    "Pacific Breeze","Aurora Airlines","CloudNine Air","Starline Aviation",
    "Sunset Skies","Falcon Air","Emerald Air","Zenith Airlines","Voyager Air",
    "Summit Air","Polar Jet","Galaxy Air","Liberty Flights","Continental Sky",
    "Sunrise Airways","Orbit Express","Northern Lights Air","Frontier Cloud",
    "AeroQuest","Silver Arrow"
]

first_names = [
    "Aidar","Aigerim","Nursultan","Saule","Bota","Dias","Alina","Yerbol",
    "Arman","Madina","Kanat","Dana","Olzhas","Assel","Timur","Laura",
    "James","Maria","Michael","Sophia","Liam","Olivia","Ethan","Emma"
]

last_names = [
    "Nazarbayev","Akhmetov","Mukhamedzhanov","Kairatov","Dosanova",
    "Zhumagulov","Bekturov","Serikbayeva","Kassymov","Sarsenov",
    "Smith","Johnson","Brown","Garcia","Lee","Anderson","Martin",
    "Kuznetsov","Ivanova","Petrova"
]

city_roots = [
    "Astana","Almaty","Shymkent","Karaganda","Aktau","Pavlodar","Turkistan",
    "New York","London","Paris","Berlin","Tokyo","Toronto","Sydney","Dubai",
    "Madrid","Rome","Seoul","Chicago","Los Angeles","Rio","Delhi","Istanbul"
]
airport_suffixes = [
    "International Airport","National Airport","Regional Airport",
    "Air Hub","Skyport","Aero Center"
]

genders   = ['Male','Female']
status    = ['Confirmed','Pending','Cancelled']
platforms = ['Website','MobileApp','Agent']
check_res = ['Clear','Flagged','Pass','Fail']

sql_lines = []

# Airline (20 rows)
for i in range(1,21):
    sql_lines.append(
        f"INSERT INTO Airline (airline_id, airline_code, airline_name, airline_country, created_at, updated_at) "
        f"VALUES ({i}, 'AL{i:03d}', '{random.choice(airline_names)}', "
        f"'{random.choice(countries)}', '{rand_date_range()}', '{rand_date_range()}');"
    )

# Airport (200 rows) with random city-based names
for i in range(1,201):
    city = random.choice(city_roots)
    airport_name = f"{city} {random.choice(airport_suffixes)}"
    sql_lines.append(
        f"INSERT INTO Airport (airport_id, airport_name, country, state, city, created_at, updated_at) "
        f"VALUES ({i}, '{airport_name}', '{random.choice(countries)}', '{rand_str(2)}', '{city}', "
        f"'{rand_date_range()}', '{rand_date_range()}');"
    )

# Passengers (200 rows)
for i in range(1,201):
    dob = rand_date_range("1950-01-01", "2005-12-31", with_time=False)
    sql_lines.append(
        f"INSERT INTO Passengers (passenger_id, first_name, last_name, date_of_birth, gender, "
        f"country_of_citizenship, country_of_residence, passport_number, created_at, updated_at) "
        f"VALUES ({i}, '{random.choice(first_names)}', '{random.choice(last_names)}', '{dob}', "
        f"'{random.choice(genders)}', '{random.choice(countries)}', '{random.choice(countries)}', "
        f"'P{i:07d}', '{rand_date_range()}', '{rand_date_range()}');"
    )

# Flights (100 rows)
for i in rane(1,101):
    sch_dep = rand_date_range()
    sch_arr = (datetime.fromisoformat(sch_dep) + timedelta(hours=random.randint(2,5))).strftime("%Y-%m-%d %H:%M:%S")
    sql_lines.append(
        f"INSERT INTO Flights (flight_id, sch_departure_time, sch_arrival_time, departing_airport_id, arriving_airport_id, "
        f"departing_gate, arriving_gate, airline_id, act_departure_time, act_arrival_time, created_at, updated_at) "
        f"VALUES ({i}, '{sch_dep}', '{sch_arr}', {random.randint(1,200)}, {random.randint(1,200)}, "
        f"'{rand_str(3)}', '{rand_str(3)}', {random.randint(1,20)}, '{sch_dep}', '{sch_arr}', "
        f"'{rand_date_range()}', '{rand_date_range()}');"
    )

# Booking (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Booking (booking_id, flight_id, passenger_id, booking_platform, created_at, updated_at, status, ticket_price) "
        f"VALUES ({i}, {random.randint(1,100)}, {random.randint(1,200)}, '{random.choice(platforms)}', "
        f"'{rand_date_range()}', '{rand_date_range()}', '{random.choice(status)}', {round(random.uniform(5000,100000),2)});"
    )

# Booking_flight (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Booking_flight (booking_flight_id, booking_id, flight_id, created_at, updated_at) "
        f"VALUES ({i}, {random.randint(1,200)}, {random.randint(1,100)}, '{rand_date_range()}', '{rand_date_range()}');"
    )

# Boarding_pass (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Boarding_pass (boarding_pass_id, booking_id, seat, boarding_time, created_at, updated_at) "
        f"VALUES ({i}, {random.randint(1,200)}, '{rand_str(1)}{random.randint(1,30)}', "
        f"'{rand_date_range()}', '{rand_date_range()}', '{rand_date_range()}');"
    )

# Baggage (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Baggage (baggage_id, weight_in_kg, created_at, updated_at, booking_id) "
        f"VALUES ({i}, {round(random.uniform(1,30),2)}, '{rand_date_range()}', '{rand_date_range()}', {random.randint(1,200)});"
    )

# Baggage_check (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Baggage_check (baggage_check_id, check_result, created_at, updated_at, booking_id, passenger_id) "
        f"VALUES ({i}, '{random.choice(check_res[:2])}', '{rand_date_range()}', '{rand_date_range()}', "
        f"{random.randint(1,200)}, {random.randint(1,200)});"
    )

# Security_check (200 rows)
for i in range(1,201):
    sql_lines.append(
        f"INSERT INTO Security_check (security_check_id, check_result, created_at, updated_at, passenger_id) "
        f"VALUES ({i}, '{random.choice(check_res[2:])}', '{rand_date_range()}', '{rand_date_range()}', {random.randint(1,200)});"
    )

# Save all INSERTs
with open("seed_data.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))

print("Created seed_data.sql with", len(sql_lines), "INSERT statements.")
