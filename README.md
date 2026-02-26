# 🛰️ AstroData Engine v1.0
### Real-Time Global Orbital Tracking System

**AstroData Engine** is a professional-grade Data Engineering pipeline designed to track the **International Space Station (ISS)** in real-time. It demonstrates a complete **ETL (Extract, Transform, Load)** workflow, integrating live API data into a structured local data warehouse.


## 🚀 Key Features
* **Real-Time Extraction:** Continuously fetches orbital telemetry and crew information from NASA-linked APIs.
* **Automated Transformation:** Processes raw JSON responses into clean, structured data frames.
* **SQL Persistence:** Automatically logs every coordinate into a local SQLite data warehouse (`orbital_missions.db`).
* **Live Dashboard:** Features a high-fidelity Terminal UI with color-coded status updates and formatted data tables.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Libraries:** * `Requests`: For robust API communication.
    * `Pandas`: For advanced data structuring.
        * `SQLite3`: For relational data storage.
            * `Tabulate & Colorama`: For professional Terminal UI rendering.

            ## 📊 Data Pipeline Architecture
            1.  **EXTRACT:** Fetches ISS current position (Latitude/Longitude) and the current number of humans in space.
            2.  **TRANSFORM:** Normalizes timestamps and converts raw strings into floating-point telemetry.
            3.  **LOAD:** Appends the cleaned record to the SQL database and refreshes the live dashboard.


            ## 🔧 Installation & Setup
            1. Clone this repository to your local environment.
            2. Install the required dependencies:
               ```bash
                  pip install requests pandas colorama tabulate