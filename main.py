"""
SensorPy – Hauptprogramm
=========================
Dieses Skript ruft alle Funktionen aus sensors.py auf und zeigt
die Ergebnisse an. Ihr könnt es jederzeit ausführen, um zu testen,
ob eure Implementierungen korrekt funktionieren.

Ausführen:
    python main.py
"""

from sensor import (
    load_data,
    calculate_average,
    find_extremes,
    count_above_threshold,
    classify_value,
    filter_by_sensor,
    generate_report,
)

# ── Daten laden ───────────────────────────────────────────────
print("Lade Messdaten...")
daten = load_data("data/messdaten.csv")
print(f"  {len(daten)} Messungen geladen.\n")

# ── Sensor S01 filtern ────────────────────────────────────────
s01 = filter_by_sensor(daten, "S01")
s02 = filter_by_sensor(daten, "S02")
print(f"Sensor S01: {len(s01)} Messungen")
print(f"Sensor S02: {len(s02)} Messungen\n")

# ── Temperatur-Analyse ────────────────────────────────────────
temps_alle = [d["temperatur"] for d in daten]
temps_s01  = [d["temperatur"] for d in s01]

print("Temperatur (alle Sensoren):")
print(f"  Durchschnitt : {calculate_average(temps_alle)} °C")
min_t, max_t = find_extremes(temps_alle)
print(f"  Min / Max    : {min_t} / {max_t} °C")
print(f"  Werte > 28°C : {count_above_threshold(temps_alle, 28.0)}\n")

print("Temperatur (nur S01):")
print(f"  Durchschnitt : {calculate_average(temps_s01)} °C\n")

# ── Klassifizierung ───────────────────────────────────────────
temp_grenzen = {"niedrig": 18.0, "normal": 26.0, "hoch": 32.0}

print("Klassifizierung einzelner Temperaturwerte:")
test_werte = [15.0, 22.0, 28.5, 33.2]
for wert in test_werte:
    klasse = classify_value(wert, temp_grenzen)
    print(f"  {wert:5.1f} °C  →  {klasse}")
print()

# ── CO2-Analyse ───────────────────────────────────────────────
co2_werte = [d["co2"] for d in daten]
co2_grenzen = {"niedrig": 600.0, "normal": 1000.0, "hoch": 1500.0}

print("CO2-Werte:")
print(f"  Durchschnitt        : {calculate_average(co2_werte)} ppm")
min_c, max_c = find_extremes(co2_werte)
print(f"  Min / Max           : {min_c} / {max_c} ppm")
print(f"  Kritische Werte (>1000 ppm): {count_above_threshold(co2_werte, 1000.0)}\n")

# ── Gesamtbericht ─────────────────────────────────────────────
print(generate_report(daten))
