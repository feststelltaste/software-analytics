# AG Open Source
Kurzlink zu dieser Seite: https://git.io/vxLQL  

## Einleitung

Herzlich Willkommen auf der Begleitseite zu "Datenanalysen in der Softwareentwicklung mit Software Analytics"!

Hier findet ihr alle notwendigen Informationen, um im Mini-Workshop mitmachen zu können.

Gleich vorab: Wer sofort richtig loslegen möchte, kann sich gerne eine "lokale Umgebung" einrichten auf seinen eigenen Computer einrichten. Wer noch zögerlich ist, kann auch die zur Verfügung stehenden Online-Testumgebungen nutzen (welche aber vermutlich nicht so performant und zuverlässig sein werden).

## Hands-On 1: Git-Log-Analyse

Hier geht es um den Einstieg in die Datenanalyse mit Python und Pandas mittels Daten aus dem Versionskontrollsystem Git. Wir wollen einige einfache Statistiken über das Open-Source-Betriebssystem Linux erheben:

* Wer sind die TOP-10-Committer?
* In welcher Zeitzone leben die meisten Entwickler?
* Zu welchen Uhrzeiten arbeiten die Entwickler?
* Wie verteilen sich die Commits über die Jahre?

Mit dem Ergebnis bekommen wir zahlreiche Einblicke in das Leben eines der berühmtesten Open-Source-Projekte.

### Einrichtung
#### Lokale Umgebung

Zur Offline-Nutzung auf dem eigenen Rechner kann die "Eierlegendewollmilchsau"-Python-Distribution Anaconda 5.0.1+ (Python 3.6) installiert werden:

> https://www.anaconda.com/download/

Alternativ kann auch Docker verwendet werden

> https://hub.docker.com/r/continuumio/anaconda3/


Zum Starten des Jupyter Servers
* unter Windows die Verknüpfung "Jupyter Notebook" anklicken
* unter Linux den Befehl `~/anaconda3/bin/jupyter notebook` ausführen

Hinweis: Um ein bestimmtes Verzeichnis für den Jupyter Server anzugeben, bitte in der Verknüpfung bzw. auf der Shell den entsprechenden Verzeichnisnamen an die jeweiligen Startbefehle (nach einem Leerzeichen) ergänzen.


#### Online-Testumgebung

Alternativ kann das Hands-On auch online mittels [https://mybinder.org/](mybinder.org) durchgeführt werden. Hier ist dann lediglich ein Computer mit Browser und Internetzugang notwendig.

Zum Vorab-Test gibt es hier eine Online-Testumgebung:

> https://mybinder.org/v2/gh/feststelltaste/software-analytics/master?urlpath=tree%2Fcourses%2Fsoftwerkskammer

Für das Treffen selbst wird es noch eine separate Online-Testumgebung geben. Die Links werden beim Treffen bekanntgegeben.


### Dataset

Für beide Varianten ist hier die URL zum notwendigen Dataset (~5 MB):

```
https://github.com/feststelltaste/software-analytics/raw/master/demos/dataset/git_demo_timestamp_linux.gz
```

_Zur Offline-Nutzung empfiehlt sich natürlich ein entsprechender Download vorab._

## Hands-On 2: Analyse wertloser Codeteile

Hier analysieren wir eine Java-Anwendung mit Hilfe des statischen Codeanalysewerkzeugs jQAssistant und der Neo4j Graphdatenbank. Wir wollen in einer Java-Anwendung die von uns identifizierten Probleme für Nicht-Techniker verständlich aufbereiten. 

Dazu werden wir
* Code Smells in der Anwendung identifizieren
* unsere Ergebnisse fachlichen Bereichen (etwa, was ein Entscheider oder Kunde versteht) zuordnen

Mit dem Ergebnis können wir Probleme im bestehenden Softwaresystem nach den Geschäftszielen priorisieren.

### Einrichtung
#### Lokale Umgebung

Voraussetzung ist eine eingerichtete, lokale Umgebung vom 1. Hands-On. Zusätzlich wird noch folgendes benötigt:

##### Python-Neo4j-Adapter `py2neo`
Diese Bibliothek kann z. B über den "Anaconda Prompt" (Windows) oder direkt auf der Kommandozeile mit Hilfe des Python-Paketmanagers `pip` installiert werden:

```
pip install py2neo
```

##### Demo-Applikation "Spring Petclinic"
Dieses Open-Source-Projekt ist eine mit jQAssistant ausgestattete (und von mir bewusst verschlechterte) Java-Web-Applikation. Sie ist unter

> https://github.com/JavaOnAutobahn/spring-petclinic

zu finden. Die dortige Anleitung schildert die Installationsschritte:

> https://github.com/JavaOnAutobahn/spring-petclinic#refuctored-spring-petclinic-sample-application

_Zur Offline-Nutzung empfiehlt es sich, die Anwendung wie in der Anleitung beschrieben komplett zu bauen und alles auszuführen._

#### Online-Testumgebung

Zum Treffen wird eine gesonderte Neo4j-Instanz zur Verfügung stehen. Weitere Details zur Nutzung folgen beim Treffen.


## Schlussbemerkung

Wer an den Themen Gefallen gefunden hat, findet auf meinem Blog https://www.feststelltaste.de noch zahlreiche andere Anwendungsfälle. Über ein Feedback zur Veranstaltung per [Mail](mailto:meetup@markusharrer.de) freue ich mich sehr!  

  
Markus Harrer  
[@feststelltaste](https://www.twitter.com/feststelltaste)  
[markusharrer.de](http://www.markusharrer.de) 
