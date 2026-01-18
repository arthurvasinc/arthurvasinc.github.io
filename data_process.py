import pandas as pd
import json

# Ez a script demonstrálja az adatfeldolgozást a 10. heti követelményekhez.
# Forrás: Kaggle Cybersecurity Dataset (szimulált CSV)
# Cél: Tidy JSON formátum a Vega-Lite számára

def process_data():
    # 1. Adatok beolvasása (szimulált CSV log)
    # df = pd.read_csv('raw_security_logs.csv')
    
    # Minta adatkeret létrehozása demonstrációs céllal
    data = {
        'timestamp': ['2023-01-12 08:30', '2023-01-15 14:20', '2023-02-05 09:10'],
        'attack_type': ['Malware', 'DDoS', 'Ransomware'],
        'severity_level': [3, 2, 5], # 1-5 skála
        'impact_cost': [12000, 4500, 55000],
        'target_dept': ['Finance', 'IT', 'Finance']
    }
    df = pd.DataFrame(data)

    # 2. Adattranszformáció (Tidy Data Principles)
    # Dátum konvertálása
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    
    # Súlyosság átnevezése olvasható kategóriákká
    severity_map = {1: 'Low', 2: 'Low', 3: 'Medium', 4: 'High', 5: 'Critical'}
    df['severity'] = df['severity_level'].map(severity_map)
    
    # Szükséges oszlopok kiválasztása
    clean_df = df[['date', 'attack_type', 'severity', 'impact_cost', 'target_dept']]
    clean_df.columns = ['date', 'type', 'severity', 'cost', 'department']

    # 3. Exportálás JSON-be
    # A 'records' orientáció fontos a Vega-Lite számára!
    clean_df.to_json('attacks_data.json', orient='records')
    print("Adatok sikeresen exportálva: attacks_data.json")

if __name__ == "__main__":
    process_data()
