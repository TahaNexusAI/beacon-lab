# 🛰️ Beacon Lab  

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[![Wireshark](https://img.shields.io/badge/Wireshark-Network_Analysis-1E90FF?logo=wireshark)](https://www.wireshark.org/)
[![License](https://img.shields.io/badge/Licence-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Project-Completed-success)]()

---

## 🎯 Mini-laboratoire éducatif  
**Analyse du trafic HTTP local avec Python et Wireshark**

Ce projet démontre la communication entre un client Python et un petit serveur HTTP local.  
Il permet de visualiser les requêtes dans **Wireshark** pour comprendre le protocole **HTTP** en action.

---

## 🧩 Composants
| Fichier | Description |
|----------|-------------|
| `server_ping.py` | Serveur HTTP local écoutant sur `127.0.0.1:8000` |
| `beacon_http.py` | Client (balise) envoyant des requêtes périodiques au serveur |
| `capture_wifi_test.pcapng` | Exemple de capture Wireshark montrant le trafic généré |

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
## 📸 Capture Wireshark
![Capture Wireshark](wireshark_capture.png)
