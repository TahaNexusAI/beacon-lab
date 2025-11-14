# 🧠 Laboratoire Beacon

Mini-laboratoire éducatif : **simulation de beaconing HTTP et analyse réseau avec Python et Wireshark**.

Ce projet montre comment un script Python (client) envoie périodiquement des requêtes HTTP vers un serveur local.  
Le trafic généré est ensuite **capturé et analysé dans Wireshark**, comme le ferait un analyste SOC ou un pentester.

---

## 📚 Table des matières
- [Description](#description)
- [Architecture](#architecture)
- [Composants](#composants)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Analyse Wireshark](#analyse-wireshark)
- [Objectifs pédagogiques](#objectifs-pédagogiques)
- [Licence](#licence)

---

## 📘 Description

Ce laboratoire simule un comportement de **beaconing**, c’est-à-dire l’envoi régulier de requêtes HTTP par un client vers un serveur.  
Ce type de trafic est très courant dans :

- les outils de supervision,
- les applications distribuées,
- les agents réseau,
- les communications **Command-and-Control (C2)** en cybersécurité.

Grâce à Wireshark, on peut observer :
- les requêtes GET,
- les réponses HTTP 200,
- les timestamps réguliers,
- l’établissement de la connexion TCP (SYN, SYN/ACK, ACK).

---

## 🧩 Architecture

[ Client Beacon ] beacon_http.py
│
│ HTTP GET /ping (périodique)
▼
[ Serveur HTTP ] server_ping.py
│
│ HTTP 200 OK
▼
[ Wireshark ]
Capture et analyse du trafic réseau


---

## 🧩 Composants
| Fichier                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `server_ping.py`          | Serveur HTTP local écoutant sur `127.0.0.1:8000`, répondant à `/ping`       |
| `beacon_http.py`          | Client envoyant des requêtes GET régulières (beaconing) au serveur         |
| `capture_wifi_test.pcapng` | Exemple de capture Wireshark montrant le trafic émis par le client         |
| `wireshark_screenshot.png` | Capture d’écran du trafic analysé dans Wireshark                           |

---

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/TahaNexusAI/beacon-lab.git
cd beacon-lab

# Lancer le serveur HTTP
python server_ping.py

# Dans un autre terminal, lancer le client
python beacon_http.py
 

▶️ Utilisation

1.Démarrer le serveur

2.Démarrer le client (envoi d’une requête toutes les X secondes)

3.Ouvrir Wireshark

4.Sélectionner l’interface loopback

5.Appliquer un filtre :

http || tcp.port == 8000


6.Observer :

.GET /ping

.réponses 200 OK

.timestamps réguliers → beaconing

.handshake TCP

🔍 Analyse Wireshark

Le fichier PCAP fourni montre :

les requêtes envoyées par le client (SYN → GET)

les réponses du serveur

la répétition cyclique (intervalle fixe)

les champs HTTP utilisés

la taille et le contenu des paquets

Ce comportement est typique :

des malwares C2 beacons,

des agents d’inventaire automatique,

des sondes réseau.

🎯 Objectifs pédagogiques

Ce laboratoire permet de :

comprendre le modèle client–serveur

analyser un trafic HTTP réel

identifier des communications régulières (beaconing)

utiliser correctement les filtres Wireshark

reconnaître les étapes du handshake TCP

comprendre comment un SOC détecte ce type de trafic

poser les bases pour des projets plus avancés (C2, détection, automatisation)

📝 Licence

Projet éducatif créé par Taha Remadna — Montréal, Canada.



