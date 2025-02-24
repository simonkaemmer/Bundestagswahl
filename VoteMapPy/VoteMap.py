import geopandas as gpd
import folium
import pandas as pd
import matplotlib.pyplot as plt

# Farben für die Parteien
party_colors = {
    "SPD": "red",
    "CDU": "black",
    "CSU": "black",
    "Grüne": "green",
    "FDP": "yellow",
    "AFD": "blue",
    "Linke": "#ff00ff",
    "None": "#ffffff"
}

# CSV-Datei einlesen und bereinigen
csv_data = "kerg.csv"
data = pd.read_csv(csv_data, sep=";", skiprows=7)
# Folgend sind erst eine Spalte (Zahl), dann der Bezeichner dieser Spalte aufgelistet, damit data.iloc(...) etwas klarer wird.
# Das dient dazu, nur relevate Spalten (Wahlkreisname und Zweitstimme der jeweiligen Partei) zu filtern.
# 22 SPD steht also dafür, dass in Spalte 22 (Zähler beginnt bei 0), in der CSV-Datei, die hierfür relevanten Zweitstimmen der SPD zu finden sind.
# 1 Wahlkreis, 22 SPD, 26 CDU, 31 Grüne, 35 FDP, 38 AFD, 42 CSU, 46 Linke
data = data.iloc[:, [1, 22, 26, 30, 34, 38, 42, 46]]
data = data.fillna(0)

winner_data = {} # Speichert nur den Wahlkreis und dessen Gewinner
all_data = {} # Speichert alle Wahlkreise und deren Daten

for index, row in data.iterrows():

    wahlkreis = row.iloc[0]

    vote_dict = {
        "SPD": row.iloc[1],
        "CDU": row.iloc[2],
        "Grüne": row.iloc[3],
        "FDP": row.iloc[4],
        "AFD": row.iloc[5],
        "CSU": row.iloc[6],
        "Linke": row.iloc[7]
    }
    vote_dict = {key: int(value) for key, value in vote_dict.items()} # Konvertiert die Werte in Integer

    if all(vote in (0, None) for vote in vote_dict.values()):
        winner_data[wahlkreis] = "None"
    else:
        winner_data[wahlkreis] = max(vote_dict, key=vote_dict.get)

    all_data[wahlkreis] = vote_dict


# Map und Shapefile
shapefile_path = "Shapefile/btw25_geometrie_wahlkreise_shp.shp"
wahlkreise = gpd.read_file(shapefile_path)
wahlkreise = wahlkreise.to_crs(epsg=4326)  # WGS84 Projektion

map_center = [wahlkreise.geometry.centroid.y.mean(), wahlkreise.geometry.centroid.x.mean()]

m = folium.Map(location=map_center, zoom_start=6)

for _, row in wahlkreise.iterrows():

    if row["WKR_NAME"] in winner_data:
        color = party_colors[winner_data[row["WKR_NAME"]]]
    else:
        color = "#ffffff"
    
    tooltip_text = f"<b>{row['WKR_NAME']}</b><br>" + "<br>".join([f"{k}: {v}" for k, v in all_data[row["WKR_NAME"]].items()])

    folium.GeoJson(
        row["geometry"],
        tooltip= tooltip_text,
        style_function=lambda feature, color=color: {
            "fillColor": color,
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.5,
        }
    ).add_to(m)
m.save("BW2025_Wahlkreise.html")

# Charts und weitere Visualisierungen

#chart_data = all_data["Bundesgebiet"]
#labels = list(chart_data.keys())
#values = list(chart_data.values())
#colors = [party_colors[label] for label in labels]

#plt.figure(figsize=(8,8))
#plt.pie(values, labels=labels, colors=colors, autopct="%1.1f%%")

#plt.title("Zweitstimmenverteilung, BW 2025")
#plt.show()
