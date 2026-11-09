# Solar Calculator - by Logenja-solar
# Calculates panels, battery and cost for a home in Mombasa

import math

print("=== LOGENJA-SOLAR CALCULATOR ===")
print("Calculate solar for your home\n")

daily_watts = int(input("How many watts do you use per day? Example 2000: "))
sun_hours = 5.5
panel_watts = 550
price_per_panel = 18000
battery_price_per_kwh = 25000

panels_needed = math.ceil(daily_watts / (panel_watts * sun_hours))
if panels_needed == 0:
    panels_needed = 1

battery_wh = daily_watts * 1.5
battery_kwh = battery_wh / 1000

panel_cost = panels_needed * price_per_panel
battery_cost = battery_kwh * battery_price_per_kwh
total_cost = panel_cost + battery_cost

print("\n--- RESULTS ---")
print(f"Panels needed: {panels_needed} x 550W")
print(f"Battery needed: {battery_wh:.0f} Wh ({battery_kwh:.1f} kWh)")
print(f"Panels cost: {panel_cost:,} KES")
print(f"Battery cost: {battery_cost:,.0f} KES")
print(f"TOTAL ESTIMATE: {total_cost:,.0f} KES")
print("\nBuilt by Logenja-solar | Mombasa, Kenya")
