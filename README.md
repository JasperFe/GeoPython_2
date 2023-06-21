# Python voor Geospatiale Analyse

Welkom bij de repository voor de cursus "Python voor Geospatiale Analyse"! Deze cursus is ontworpen binnen het GCCA+ 2 project, om kennis en vaardigheden te bieden voor het effectief gebruiken van Python bij geospatiale analyse. 


## Inhoud van de cursus

1. **Python-introductie in Jupyter Lab**: Maak kennis met de basisprincipes van Python-programmering in het interactieve Jupyter Lab-omgeving.
2. **Pandas**: Leer hoe je geospatiale datasets kunt laden, schoonmaken, analyseren en visualiseren met behulp van de krachtige pandas-bibliotheek.
3. **Geopandas voor vectoranalyse**: Verken geospatiale vectoranalyse en ontdek hoe je geopandas kunt gebruiken voor taken zoals ruimtelijke koppelingen, buffering en ruimtelijk
4. **xarray en rasterio voor rasteranalyse**: Ontdek de mogelijkheden van rasterio voor het werken met rastergegevens, inclusief het lezen, manipuleren en visualiseren van georeferenced rasters.
5. **Raster-vector operaties**: Leer hoe je vector- en rastergegevens kunt combineren en overlayen om geavanceerde geospatiale analyses uit te voeren, zoals zonale statistieken en ruimtelijke aggregatie.
6. **GeoWombat: scaling en machine learning**: Verken machine learning-technieken voor het classificeren van landbedekking op basis van geospatiale gegevens, inclusief remote sensing-beelden.

# Installatie en vereisten
## Binder
Je kunt de cursus ook online volgen, zonder installatie via binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JasperFe/GCCA_GeoPython/HEAD)


## 1. Installeer Anaconda

We maken gebruik van Anaconda als distributeur van python (versie 3.X) en jupyter lab. Dit is een open-source sofware, waardoor de installatie volledig gratis is. Ga naar website van Anaconda: [https://www.anaconda.com/download/](https://www.anaconda.com/download/).

[Meer informatie? Lees hier over de installatie van Anaconda op windows](https://docs.anaconda.com/free/anaconda/install/windows/).


## 2. Maak een nieuw **conda environment** aan
Anaconda werkt met **conda environments**, wat python-omgeving is met alle noodzakelijke pakketten voor een bepaalde toepassing (op die manier kun je meerdere environments hebben, voor verschillende applicaties). We maken een nieuwe **conda environment** aan, die de noodzakelijke paketten bevat voor deze cursus. 

De [environment.yml](https://github.com/JasperFe/GCCA_GeoPython/blob/main/environment.yml) file is nodig voor deze installatie en bevat de informatie omtrent;
  * de naam van de omgeving
  * de channels waaruit python-pakketten gedownload worden
  * een lijst met alle te installeren paketten.

Ga naar de environment.yml file en download deze naar een folder (bijvoorbeeld C:/Users/UserName/Documents/Geopython).

Open daarna de anaconda prompt. 
Typ hierbij volgende code in (lijn per lijn):

```shell
conda config --add channels conda-forge
conda config --set channel_priority strict
cd FOLDER_PATH_TO_ENVIRONMENT_FILE
conda env create -f environment.yml
```  

Vervang FOLDER_PATH_TO_ENVIRONMENT_FILE door het pad naar de map waarin het environment.yml bestand zich bevindt.

De environment en pakketten zullen vervolgens worden geïnstalleerd, dit kan enkele minuten duren. Antwoord met '''y''' indien dit gevraagd wordt.

### 3. Starten van de Jupyter lab

Om jupyter lab te openen en de cursus-*notebooks* te kunnen gebruiken, open de Anaconda prompt opnieuw:

1. Navigeer naar de folder waar je notebooks hebt gedownload:

```shell
cd FOLDER_PAD_NAAR_CURSUSMATERIAAL
```   

Vervang hierbij de FOLDER_PAD_NAAR_CURSUSMATERIAAL door het correct pad.
(bijvoorbeeld: C:/Users/yourusername/Documents/Geopython)

2. Activeer de conda environment:

```shell
conda activate GCCA-Geopython
``` 

3. Start Jupyter Notebook
Jupyter notebook is een interactieve omgeving om code te schrijven en te laten lopen. Een voordeel is dat de code kan worden afgewisseld met extra verduidelijkende tekst. Ideaal dus voor een cursus geopython!

Om jupyter notebook te starten, typ binnen het geactiveerde environment:

```shell
jupyter lab
```  

Een chrome-venster gaat open, waarin de jupyter lab tevoorschijn komt.

## Cursusmateriaal

Het cursusmateriaal is gestructureerd in afzonderlijke modules, elk met hun eigen notebooks en bijbehorende datasets. Je kunt door de mappen navigeren om toegang te krijgen tot de specifieke inhoud van elke module. Naast de 'basiscursus' kan de opgedane kennis aan de hand van extra notebooks worden uitgebreid, via referentiemateriaal.

Het cursusmateriaal wordt tijden de cursus steeds bijgewerkt, dus mogelijks zul je de meest recente versies moeten downloaden

## Aan de slag

Om te beginnen met de cursus, raden we je aan om de notebooks te openen in Jupyter Lab en de instructies te volgen. De notebooks bevatten gedetailleerde uitleg, codevoorbeelden en oefeningen om je te helpen de concepten en technieken te begrijpen en toe te passen.

## Bronnen

Deze cursus is tot stand gekomen dankzij enkele zeer nuttige bronnen:
-
 



