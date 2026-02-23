from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random


KEYWORD = "Web Designers"  
LOCATION = "London"
TARGET_URL = f"https://www.yell.com/ucs/UcsSearchAction.do?keywords={KEYWORD.replace(' ', '+')}&location={LOCATION}"
EXCEL_NAME = "London_Web_Designers_BUYERS.xlsx"

print(f"💼 ALICI AVCSISI BAŞLATILIYOR... Hedef: {KEYWORD} in {LOCATION}")

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.page_load_strategy = 'eager' 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
full_data = []

try:
    print(f"🌍 Siteye gidiliyor: {TARGET_URL}")
    driver.get(TARGET_URL)
    
    print("\n" + "="*50)
    print("🛑 DİKKAT: Robot kontrolü varsa çöz.")
    print("👉 Listeyi görünce ENTER'a bas.")
    print("="*50 + "\n")
    input("Hazır olunca ENTER'a bas...")
    
    print("🚀 Ajanslar toplanıyor...")

   
    for page in range(1, 21):
        print(f"\n📄 Sayfa {page}/20 işleniyor... (Toplam Veri: {len(full_data)})")
        time.sleep(3)
        
        articles = driver.find_elements(By.CSS_SELECTOR, "article.businessCapsule")
        
        if not articles:
            print("⚠️ Sayfa yüklenmedi, tekrar deneniyor...")
            time.sleep(5)
            articles = driver.find_elements(By.CSS_SELECTOR, "article.businessCapsule")

        for article in articles:
            try:
               
                try:
                    name = article.find_element(By.CSS_SELECTOR, "h2.businessCapsule--name").text
                except:
                    continue 
                
               
                try:
                    phone_elem = article.find_element(By.CSS_SELECTOR, "span.business--telephoneNumber")
                    phone = phone_elem.get_attribute("textContent").strip()
                except:
                    phone = "Yok"

             
                try:
                    website_elem = article.find_element(By.CSS_SELECTOR, "a[data-test='localBusiness--website']")
                    website = website_elem.get_attribute("href")
                except:
                    website = "Yok"
                
                full_data.append({
                    "Agency Name": name,
                    "Phone": phone,
                    "Website": website,
                    "Source": "Yell.com"
                })

            except:
                continue 
        
       
        try:
            next_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pagination--next"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(random.uniform(2, 5))
            
        except:
            print("🏁 Liste bitti.")
            break

except KeyboardInterrupt:
    print("\n🛑 Durduruldu. Kaydediliyor...")

except Exception as e:
    print(f"\n❌ Hata: {e}")

finally:
    if full_data:
        df = pd.DataFrame(full_data)
        df.drop_duplicates(subset=['Agency Name'], inplace=True)
        df.to_excel(EXCEL_NAME, index=False)
        print("\n" + "="*50)
        print(f"✅ ALICI LİSTESİ HAZIR! {len(df)} ajans bulundu.")
        print(f"📁 Dosya: {EXCEL_NAME}")
        print("="*50)
    else:
        print("❌ Veri yok.")
    
    driver.quit()