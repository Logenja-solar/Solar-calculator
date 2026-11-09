# Solar Quotation Generator - by Logenja-solar
# Mombasa, Kenya

print("☀️ LOGENJA SOLAR - QUOTATION GENERATOR")
print("--------------------------------------")

customer = input("Customer name: ")
location = input("Location (e.g. Nyali, Mombasa): ")
daily_watts = float(input("How many watts do you use per day? "))

# Calculation - using 550W panels
panels_needed = daily_watts / 550
# Round up - you can't buy half a panel
import math
panels_needed = math.ceil(panels_needed)

panel_price = 28000
battery_price = 45000
inverter_price = 35000
labour = 15000

panel_cost = panels_needed * panel_price
battery_needed = 1
if daily_watts > 2000:
    battery_needed = 2

battery_cost = battery_needed * battery_price
total = panel_cost + battery_cost + inverter_price + labour

print("\n========== QUOTATION ==========")
print(f"Customer: {customer}")
print(f"Location: {location}")
print(f"Daily Usage: {daily_watts} Wh")
print(f"Panels Needed: {panels_needed} x 550W @ {panel_price} KES = {panel_cost} KES")
print(f"Battery: {battery_needed} x 12V @ {battery_price} KES = {battery_cost} KES")
print(f"Inverter: 1 x {inverter_price} KES")
print(f"Labour & Installation: {labour} KES")
print("------------------------------")
print(f"TOTAL: {total} KES")
print("==============================")
print("Thank you for choosing Logenja Solar!")
print("Mombasa | Call / WhatsApp: 07XX XXX XXX")
