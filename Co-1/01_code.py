farmer_id = "F101"
litres = 10.0
fat = 3.5
snf = 8.5
shift = "Morning"

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE
             + snf_steps * SNF_STEP_VALUE, 2)
amount = round(litres * rate, 2)

if litres >= 0 and 2.0 <= fat <= 7.0 and snf >= 0:
    print("Farmer ID:", farmer_id)
    print("Rate per litre:", rate)
    print("Amount:", amount)
else:
    print("Invalid entry")
