# 🛰️ Beacon Lab

Mini-laboratoire éducatif : **analyse du trafic HTTP local avec Python et Wireshark**.

## 📘 Description

Ce projet démontre la communication entre un client Python et un petit serveur HTTP local.  
Il permet de visualiser les requêtes dans **Wireshark** pour comprendre le protocole HTTP.

### 🧩 Composants :
- **`server_ping.py`** : un serveur local simple (HTTP) qui écoute sur `127.0.0.1:8000`
- **`beacon_http.py`** : un client (balise) qui envoie des requêtes périodiques au serveur
- **`capture_wifi_test.pcapng`** : un exemple de capture Wireshark montrant le trafic

## ⚙️ Installation

1. Installer **Python 3.14+**
2. Cloner ce dépôt :
   ```bash
   git clone https://github.com/TahaNexusAI/beacon-lab.git
