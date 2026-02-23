import pandas as pd


INPUT_FILE = "London_Estate_Agents_BULLDOZER.xlsx"

OUTPUT_FILE = "SITEYE_IHTIYACI_OLANLAR.xlsx"

print("📂 Excel dosyası açılıyor...")
df = pd.read_excel(INPUT_FILE)

target_leads = df[df['Website'] == 'Yok']

print(f"🔍 Analiz yapıldı. Toplam {len(df)} satır içinden...")
print(f"🎯 {len(target_leads)} tane potansiyel müşteri bulundu!")


target_leads.to_excel(OUTPUT_FILE, index=False)
print(f"✅ Dosya hazır: {OUTPUT_FILE}")