# RainAlert - Weather Monitoring System

## 🎯 Project Description  
Get automatic WhatsApp notifications if rain is predicted in your area using real-time weather data from OpenWeatherMap.

## 📦 Deliverables  
- Python script with dual API integration  
- Environment variables configuration  
- Weather condition analysis system  
- Automated WhatsApp messaging  

## 🚀 Key Features  
- 🌧️ Precipitation detection  
- 📱 Instant WhatsApp notifications  
- 🔐 Secure credential management  
- 📡 API error handling  

## 🛠️ Technologies Used  
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Language**           | Python 3                            |
| **Weather API**        | OpenWeatherMap                      |
| **Messaging API**      | Twilio                              |
| **Env Management**     | python-dotenv                       |

## ⚙️ Installation & Setup  

### 1. Clone Repository  
```bash
git clone https://github.com/My-Py-Projects/rain-alert.git
cd rain-alert
```

### 2. Install Dependencies  
```bash
pip install requests python-dotenv twilio
```

### 3. Environment Configuration  
Create a `.env` file in root directory with:

```ini
# OpenWeather
API_KEY=your_api_key_here
LAT=-23.5505
LON=-46.6333

# Twilio
ACCOUNT_SID=your_account_sid
AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+1415523...
USER_WHATSAPP_NUMBER=whatsapp:+5511...
```

### 4. Run Application 
```bash
python main.py
```

**Important Notes:**  
```plaintext
1. Requires active accounts on:
   - OpenWeatherMap: https://openweathermap.org/api
   - Twilio: https://www.twilio.com/docs/whatsapp/quickstart/python

2. Required formats:
   - Coordinates: Decimal (e.g. LAT: -23.5505)
   - Phone numbers: E.164 format (e.g. whatsapp:+5511999999999)
```