import requests
import pandas as pd
import sqlite3
import time
import os
from datetime import datetime
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize professional UI
init(autoreset=True)

class OrbitalDataPipeline:
    def __init__(self):
        self.database = "orbital_missions.db"
        self.iss_api = "http://api.open-notify.org/iss-now.json"
        self.crew_api = "http://api.open-notify.org/astros.json"
        self._initialize_warehouse()

    def _initialize_warehouse(self):
        """Creates the SQL schema with matching column names."""
        with sqlite3.connect(self.database) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS telemetry_logs 
                (Timestamp TEXT, Latitude REAL, Longitude REAL, Crew_Count INTEGER)''')

    def extract_telemetry(self):
        """Extracts real-time data from NASA/Open-Notify APIs."""
        try:
            position_data = requests.get(self.iss_api, timeout=10).json()
            astronaut_data = requests.get(self.crew_api, timeout=10).json()
            return {
                "Timestamp": datetime.now().strftime("%H:%M:%S"),
                "Latitude": float(position_data['iss_position']['latitude']),
                "Longitude": float(position_data['iss_position']['longitude']),
                "Crew_Count": int(astronaut_data['number'])
            }
        except Exception as e:
            return None

    def run_pipeline(self):
        """Orchestrates the ETL process and renders the Terminal HUD."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.CYAN}Establishing Satellite Uplink... Please wait.")
        time.sleep(2)
        
        try:
            while True:
                raw_data = self.extract_telemetry()
                if raw_data:
                    # Transform and Load to SQL
                    df = pd.DataFrame([raw_data])
                    with sqlite3.connect(self.database) as conn:
                        df.to_sql("telemetry_logs", conn, if_exists="append", index=False)
                    
                    # Refresh Terminal Dashboard
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Fore.GREEN}{'='*70}")
                    print(f"{Fore.WHITE}{Style.BRIGHT}   ASTRODATA ENGINE v1.0 | GLOBAL ORBITAL TRACKING SYSTEM")
                    print(f"{Fore.GREEN}{'='*70}\n")
                    
                    # Display Data Table
                    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
                    
                    print(f"\n{Fore.BLUE}[INFO] Signal Status: STABLE")
                    print(f"{Fore.WHITE}[DB] Local Storage: {self.database}")
                    print(f"{Fore.RED}[TERMINATE] Press CTRL+C to close connection.")
                
                time.sleep(5)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Uplink Disconnected. All telemetry saved successfully.")

if __name__ == "__main__":
    engine = OrbitalDataPipeline()
    engine.run_pipeline()
