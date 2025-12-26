
# ⚡ PySubEnum (v1.2)

![Version](https://img.shields.io/badge/version-v1.2-magenta?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Offensive_Security-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**PySubEnum** is an advanced, modular **Subdomain Enumeration & Vulnerability Scanner** designed for Red Teams and Bug Bounty hunters. 

Unlike standard enumeration tools, PySubEnum goes beyond listing domains; it performs **CNAME analysis** to detect potential **Subdomain Takeover** vulnerabilities and offers a multi-threaded architecture for high-speed reconnaissance.

## 🚀 Key Features

* **🕵️‍♂️ Multi-Source Passive Recon:** Aggregates data from **Crt.sh** and **HackerTarget** without touching the target directly.
* **🚨 Subdomain Takeover Detection:** Automatically analyzes CNAME records to identify vulnerable pointers (e.g., pointing to abandoned Heroku, AWS S3, GitHub Pages, etc.).
* **🌐 Advanced DNS Resolution:** Uses `dnspython` for accurate A and CNAME record retrieval.
* **⚓ Port Scanning:** Multi-threaded check for critical open ports (`80`, `443`, `22`, `3306`, etc.) on discovered assets.
* **🎨 Visual & Modular:** Color-coded terminal output for easy reading and a clean, maintainable codebase structure.
* **📂 Smart Reporting:** Exports clean results to a file for further processing.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/bellamy58/PySubEnum.git

# Navigate to the directory
cd PySubEnum

# Install dependencies
pip install -r requirements.txt
