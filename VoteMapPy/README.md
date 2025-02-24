# VoteMapPy
Auf der [Website der Bundeswahlleiterin](https://www.bundeswahlleiterin.de/bundeswahlleiter.html) werden Daten zur Bundestagswahl veröffentlicht. Diese Daten werden vom Python-Script etwas gefiltert und dann auf eine OpenStreetMap projeziert. Dabei werden derzeit nur die Zweitstimmen der Wähler für folgende Parteien berücksichtigt:
- CDU `Schwarz`
- CSU `Schwarz`
- SPD `Rot`
- B90/Gruene `Grün`
- FDP `Gelb`
- Linke `Pink/Rosa`

Die Daten stammen direkt aus dem [OpenData-Angebot im CSV-Format](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata.html) [(kerg.csv)](https://bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata/btw25/csv/) der Bundeswahlleiterin.
Das [ShapeFile für Folium und GeoPandas](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/wahlkreiseinteilung/downloads.html), welches die Wahlkreise definiert, kommt ebenfalls aus dem Portal der Bundeswahlleiterin.

Als Ergebnis wird eine HTML-Datei erstellt, die im Browser angesehen werden kann.
[➡ Hier geht’s zur Karte!](https://simonkaemmer.github.io/Bundestagswahl/VoteMapPy/BW2025_Wahlkreise.html)


<ins>**Vorsicht: Dadurch, dass nur die oben genannten Parteien berücksichtigt werden, können Abweichungen auftreten. Ebenfalls besteht die Möglichkeit, dass ich Fehler in der Programmierung oder Formatierung der Daten gemacht habe. Falls etwas auffällt, gerne melden!**</ins> <br>
Beispiel: Wenn im Wahlkreis Berlin-Mitte eine Partei die nicht oben aufgeführt wurde, gewonnen hat, wird diese nicht berücksichtigt. Es wird also der Sieger der oben genannten angezeigt.

## Benötigte Python-Pakete  
Dieses Projekt benötigt folgende Bibliotheken:  

- **GeoPandas** (`pip install geopandas`)  
- **Folium** (`pip install folium`)  
- **Pandas** (`pip install pandas`)  
- **MatPlotLib** (`pip install matplotlib`)  

Alternativ kann man alle Pakete mit:
```bash
pip install geopandas folium pandas matplotlib
```
installieren.

