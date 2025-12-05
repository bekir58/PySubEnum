
# ⚡ PySubEnum v3.0

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Maintained-orange?style=for-the-badge)

**PySubEnum** is a robust, multi-threaded **Subdomain Enumeration & Reconnaissance Tool**. It combines passive source gathering with active resolution and port scanning capabilities to provide a comprehensive view of the target's attack surface.

## 🚀 Features

* **🔍 Multi-Source Passive Recon:** Aggregates data from **Crt.sh**, **HackerTarget**, and **AlienVault OTX**.
* **🌐 Active DNS Resolution:** Filters dead subdomains by resolving IP addresses (A Records).
* **⚓ Port Scanning:** Optionally scans top critical ports (21, 22, 80, 443, 3306, etc.) on discovered assets.
* **⚡ High Performance:** Uses `ThreadPoolExecutor` for concurrent scanning.
* **📂 Smart Reporting:** Exports results (Domain, IP, Ports) to a file.

## 📦 Installation

```bash
git clone [https://github.com/bekir58/PySubEnum.git](https://github.com/bekir58/PySubEnum.git)
cd PySubEnum
pip install -r requirements.txt
