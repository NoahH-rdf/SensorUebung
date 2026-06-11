"""
SensorPy – Messdaten analysieren
=================================
Dieses Modul enthält alle Funktionen zur Analyse von Umweltmessdaten.

Aufgabe: Implementiert jede Funktion so, dass sie der Beschreibung
im Docstring entspricht. Die Signatur (Name, Parameter, Rückgabetyp)
darf NICHT verändert werden.

Datenformat (eine Zeile aus messdaten.csv als dict):
    {
        "sensor_id":       "S01",
        "timestamp":       "2024-03-01 08:00",
        "temperatur":      19.2,
        "luftfeuchtigkeit": 52.1,
        "co2":             480.0
    }
"""

import csv


# ──────────────────────────────────────────────────────────────
# PERSON A
# ──────────────────────────────────────────────────────────────

def load_data(filename: str) -> list[dict]:
    """Liest eine CSV-Datei mit Messdaten ein und gibt sie als Liste zurück.

    Jede Zeile der CSV wird in ein dict umgewandelt.
    Numerische Felder (temperatur, luftfeuchtigkeit, co2) werden
    automatisch in float konvertiert.

    Args:
        filename: Pfad zur CSV-Datei (z. B. "data/messdaten.csv")

    Returns:
        Liste von dicts, eines pro Zeile. Leere Liste bei Fehler.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> print(daten[0]["sensor_id"])
        S01
        >>> print(daten[0]["temperatur"])
        19.2
    """
    result: list[dict] = []
    numeric_fields = {"temperatur", "luftfeuchtigkeit", "co2"}

    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                converted = {}
                for key, value in row.items():
                    if key in numeric_fields:
                        try:
                            converted[key] = float(value)
                        except (TypeError, ValueError):
                            converted[key] = float('nan')
                    else:
                        converted[key] = value
                result.append(converted)
    except (OSError, csv.Error):
        return []

    return result


def calculate_average(values: list[float]) -> float:
    """Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Arithmetisches Mittel aller Werte, gerundet auf 2 Dezimalstellen.

    Beispiel:
        >>> calculate_average([10.0, 20.0, 30.0])
        20.0
        >>> calculate_average([19.2, 21.4, 24.7])
        21.77
    """
    return round(sum(values) / len(values), 2)


def find_extremes(values: list[float]) -> tuple[float, float]:
    """Findet den kleinsten und grössten Wert einer Liste.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Tupel (minimum, maximum)

    Beispiel:
        >>> find_extremes([19.2, 21.4, 24.7, 17.5])
        (17.5, 24.7)
    """
    return (min(values), max(values))


def count_above_threshold(values: list[float], threshold: float) -> int:
    """Zählt, wie viele Werte in der Liste den Schwellenwert überschreiten.

    Args:
        values:    Liste mit float-Werten
        threshold: Schwellenwert (Werte > threshold werden gezählt)

    Returns:
        Anzahl der Werte, die strikt grösser als threshold sind.

    Beispiel:
        >>> count_above_threshold([19.2, 27.1, 24.7, 33.2, 21.4], 25.0)
        2
    """
    return sum(1 for value in values if value > threshold)


# ──────────────────────────────────────────────────────────────
# PERSON B
# ──────────────────────────────────────────────────────────────

def classify_value(value: float, limits: dict) -> str:
    """Klassifiziert einen Messwert anhand von Grenzwerten.

    Die limits-dict hat folgende Struktur:
        {
            "niedrig":  <obere Grenze für "niedrig">,
            "normal":   <obere Grenze für "normal">,
            "hoch":     <obere Grenze für "hoch">
            # alles darüber gilt als "kritisch"
        }

    Args:
        value:  Der zu klassifizierende Messwert
        limits: Dict mit den Grenzwerten (siehe oben)

    Returns:
        Einen der folgenden Strings: "niedrig", "normal", "hoch", "kritisch"

    Beispiel (Temperatur-Grenzen: niedrig<18, normal<26, hoch<32):
        >>> grenzen = {"niedrig": 18.0, "normal": 26.0, "hoch": 32.0}
        >>> classify_value(15.0, grenzen)
        'niedrig'
        >>> classify_value(22.0, grenzen)
        'normal'
        >>> classify_value(28.5, grenzen)
        'hoch'
        >>> classify_value(35.0, grenzen)
        'kritisch'
    """
    if value < limits["niedrig"]:
        return "niedrig"
    if value < limits["normal"]:
        return "normal"
    if value < limits["hoch"]:
        return "hoch"
    return "kritisch"


def filter_by_sensor(data: list[dict], sensor_id: str) -> list[dict]:
    """Filtert die Messdaten nach einer bestimmten Sensor-ID.

    Args:
        data:      Liste von Messdaten-dicts (Ausgabe von load_data)
        sensor_id: Sensor-ID, nach der gefiltert werden soll (z. B. "S01")

    Returns:
        Neue Liste, die nur Einträge mit der angegebenen sensor_id enthält.
        Leere Liste, wenn kein passender Eintrag gefunden wird.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> s01 = filter_by_sensor(daten, "S01")
        >>> all(d["sensor_id"] == "S01" for d in s01)
        True
    """
    return [entry for entry in data if entry.get("sensor_id") == sensor_id]


def generate_report(data: list[dict]) -> str:
    """Erstellt einen Textbericht aus den Messdaten.

    Der Bericht enthält:
    - Gesamtanzahl der Messungen
    - Durchschnitt, Min und Max für Temperatur, Luftfeuchtigkeit und CO2
    - Anzahl der kritischen Temperaturmessungen (> 30 °C)
    - Liste aller vorhandenen Sensor-IDs

    Args:
        data: Liste von Messdaten-dicts (Ausgabe von load_data)

    Returns:
        Formatierter mehrzeiliger String.

    Beispiel-Output (gekürzt):
        ========== SensorPy Bericht ==========
        Messungen total:       36
        Sensoren:              S01, S02

        -- Temperatur (°C) --
        Durchschnitt:          22.48
        Min / Max:             15.9 / 33.2
        Kritische Werte (>30): 2

        -- Luftfeuchtigkeit (%) --
        ...
        ======================================
    """
    from statistics import mean

    if not data:
        return "Keine Messdaten verfügbar."

    sensors = sorted({entry["sensor_id"] for entry in data})
    temp = [entry["temperatur"] for entry in data]
    humidity = [entry["luftfeuchtigkeit"] for entry in data]
    co2 = [entry["co2"] for entry in data]

    def avg(values):
        return round(mean(values), 2)

    def minmax(values):
        return min(values), max(values)

    temp_avg = avg(temp)
    temp_min, temp_max = minmax(temp)
    hum_avg = avg(humidity)
    hum_min, hum_max = minmax(humidity)
    co2_avg = avg(co2)
    co2_min, co2_max = minmax(co2)
    critical_temp = sum(1 for value in temp if value > 30)

    return (
        "========== SensorPy Bericht =========="
        f"\nMessungen total:       {len(data)}"
        f"\nSensoren:              {', '.join(sensors)}"
        "\n\n-- Temperatur (°C) --"
        f"\nDurchschnitt:          {temp_avg:.2f}"
        f"\nMin / Max:             {temp_min:.1f} / {temp_max:.1f}"
        f"\nKritische Werte (>30): {critical_temp}"
        "\n\n-- Luftfeuchtigkeit (%) --"
        f"\nDurchschnitt:          {hum_avg:.2f}"
        f"\nMin / Max:             {hum_min:.1f} / {hum_max:.1f}"
        "\n\n-- CO2 (ppm) --"
        f"\nDurchschnitt:          {co2_avg:.2f}"
        f"\nMin / Max:             {co2_min:.1f} / {co2_max:.1f}"
        "\n======================================"
    )

