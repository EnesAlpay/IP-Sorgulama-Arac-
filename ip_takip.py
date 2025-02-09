import requests
import json

def ip_sorgula(ip_adresi):
    url = f"http://ip-api.com/json/{ip_adresi}"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data["status"] == "success":
            print("\n🌍 IP Adresi Konum Bilgileri")
            print("="*40)
            print(f"🔹 IP: {ip_adresi}")
            print(f"🌍 Ülke: {data['country']} ({data['countryCode']})")
            print(f"🏙 Şehir: {data['city']}")
            print(f"📌 Bölge: {data['regionName']} ({data['region']})")
            print(f"🕒 Zaman Dilimi: {data['timezone']}")
            print(f"📡 İnternet Servis Sağlayıcısı: {data['isp']}")
            print(f"🌎 Koordinatlar: {data['lat']}, {data['lon']}")
            print("="*40)
        else:
            print("❌ Geçersiz IP adresi veya API hatası!")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Bağlantı hatası: {e}")

if __name__ == "__main__":
    ip_adresi = input("Takip etmek istediğiniz IP: ").strip()
    ip_sorgula(ip_adresi)
