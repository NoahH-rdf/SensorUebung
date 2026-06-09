# SensorPy – Messdaten analysieren

Python-Gesamtübung | 2 Doppelstunden | Teams à 2 Personen

## Aufgabe

Eine Umweltmessstation liefert Daten zu **Temperatur**, **Luftfeuchtigkeit** und **CO₂-Gehalt**.  
Ihr implementiert gemeinsam ein Analyse-Tool, das diese Daten einliest, auswertet und einen Bericht erstellt.

## Repo-Struktur

```
sensorpy/
├── sensors.py          ← Hier implementiert ihr die Funktionen
├── main.py             ← Testprogramm (nicht verändern)
└── data/
    └── messdaten.csv   ← Beispieldaten (nicht verändern)
```

## Einstieg

```bash
# 1. Repo forken (auf GitHub)
# 2. Lokal klonen
git clone https://github.com/EUER-TEAM/sensorpy.git
cd sensorpy

# 3. Eigenen Branch erstellen
git checkout -b feature/person-a    # oder feature/person-b

# 4. Funktionen in sensors.py implementieren
# 5. Testen
python main.py
```

## Aufteilung

| Person A | Person B |
|----------|----------|
| `load_data()` | `classify_value()` |
| `calculate_average()` | `filter_by_sensor()` |
| `find_extremes()` | `generate_report()` |
| `count_above_threshold()` | `main.py` – alles verbinden |

## GitHub-Workflow

```
main  ←── Pull Request ←── feature/person-a
      ←── Pull Request ←── feature/person-b
```

1. Jede Person arbeitet auf ihrem eigenen Branch
2. Commits regelmässig pushen (`git add`, `git commit`, `git push`)
3. Wenn fertig: Pull Request erstellen
4. Den Code der anderen Person reviewen, dann mergen

## Tipps

- Lest die **Docstrings** in `sensors.py` – sie beschreiben genau, was jede Funktion tun soll
- Testet mit `python main.py` nach jeder implementierten Funktion
- Ihr dürft KI-Tools (GitHub Copilot) verwenden – versteht aber, was der Code tut
- Schreibt mindestens **3 eigene Commits** pro Person

## Bewertungskriterien

- [ ] GitHub Repo zugänglich mit min. 2 Branches und 1 Pull Request
- [ ] Alle Funktionen implementiert
- [ ] `main.py` läuft fehlerfrei durch
- [ ] Beide Personen haben mind. 3 eigene Commits


Hallo Noah
Hallo Julian 