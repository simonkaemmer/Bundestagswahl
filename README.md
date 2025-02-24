# Bundestagswahl
Veranschaulichungen zur Bundestagswahl

## VoteMapPy
Auf der [Website der Bundeswahlleiterin](https://www.bundeswahlleiterin.de/bundeswahlleiter.html) werden Daten zur Bundestagswahl veröffentlicht. Diese Daten werden vom Python-Script etwas gefiltert und dann auf eine Leaflet-Map projeziert. Dabei werden derzeit nur die Zweitstimmen der Wähler für folgende Parteien berücksichtigt:
- CDU `Schwarz`
- CSU `Schwarz`
- SPD `Rot`
- B90/Gruene `Grün`
- FDP `Gelb`
- Linke `Pink/Rosa`

Die Daten stammen direkt aus dem [OpenData-Angebot in CSV-Format](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata.html) [(kerg.csv)](https://bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata/btw25/csv/) der Bundeswahlleiterin.

Das [ShapeFile für GeoPandas](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/wahlkreiseinteilung/downloads.html), welches die Wahlkreise definiert, kommt ebenfalls aus dem Portal der Bundeswahlleiterin.

Sowohl der Ordner für das Shapefile, als auch die Zähldaten müssen im selben Verzeichnis, wie das Python-Script liegen. Es wird bei Ausführung des Python-Scripts eine HTML-Datei generiert, welche die Karte beinhaltet.

<ins>**Vorsicht: Dadurch, dass nur die oben genannten Parteien berücksichtigt werden, können Abweichungen auftreten.**</ins> <br>
Beispiel: Wenn im Wahlkreis Berlin-Mitte eine Partei die nicht oben aufgeführt wurde, gewonnen hat, wird diese nicht berücksichtigt. Es wird also der Sieger der oben genannten angezeigt.
