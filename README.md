# 🚁 Discord Drone Bot

A comprehensive Discord bot for drone enthusiasts, pilots, and builders. Get drone specifications, weather conditions, component recommendations, and regulatory information directly in your Discord server.

## Features

- **Drone Information**: Access specifications and details for popular drone models (DJI, Parrot, etc.)
- **Weather Integration**: Check real-time weather conditions with flight safety assessments
- **Component Database**: Learn about drone components for custom builds
- **Regulations Guide**: Get drone flying regulations by country
- **Flight Safety Alerts**: Automatic wind speed assessment for safe flying conditions
- **Rich Discord Embeds**: Clean, organized information display

## Requirements

- Python 3.8+
- discord.py
- aiohttp

## Installation

### 1. Clone or Download the Bot Files
```bash
git clone <repository-url>
cd discord-drone-bot
```

### 2. Install Dependencies
```bash
pip install discord.py aiohttp
```

### 3. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "Drone Bot")
3. Go to the "Bot" section and click "Add Bot"
4. Copy your bot token and save it securely
5. Enable required intents under "MESSAGE CONTENT INTENT" and "PRIVILEGED GATEWAY INTENTS"
6. Go to "OAuth2" → "URL Generator"
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Embed Links`, `Read Messages/View Channels`
9. Copy the generated URL and open it to invite the bot to your server

### 4. Get API Keys

**OpenWeatherMap API (Free tier available):**
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to API keys section and copy your key

### 5. Configure the Bot

Edit the bot file and replace:
```python
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Your OpenWeatherMap API key
bot.start('YOUR_DISCORD_BOT_TOKEN')  # Your Discord bot token
```

### 6. Run the Bot

```bash
python drone_bot.py
```

You should see:
```
✅ Bot logged in as YourBotName#0000
```

## Commands

### General Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `!droneinfo` | `!droneinfo [model]` | Get drone model specifications |
| `!weather` | `!weather <city>` | Check weather and flight safety |
| `!dronebuild` | `!dronebuild [component]` | Learn about drone components |
| `!regulations` | `!regulations [country]` | Get drone flying regulations |

### Command Examples

**Get drone information:**
```
!droneinfo dji
!droneinfo parrot
!droneinfo
```

**Check weather conditions:**
```
!weather New York
!weather London
```

**Explore components:**
```
!dronebuild motor
!dronebuild battery
!dronebuild
```

**Get regulations:**
```
!regulations us
!regulations uk
!regulations eu
```

## Supported Features

### Drone Models
- DJI Air 3S
- DJI Avata 3
- Parrot Anafi

### Weather Data
- Temperature
- Humidity
- Wind Speed
- Weather Conditions
- Flight Safety Assessment

### Drone Components
- Frame
- Motor
- ESC (Electronic Speed Controller)
- Battery
- Camera
- Receiver
- Propeller

### Regulations by Country
- US (FAA Part 107)
- UK (EASA)
- EU (European Regulations)

## Flight Safety Assessment

The bot automatically assesses flight conditions based on wind speed:

| Wind Speed | Status | Recommendation |
|------------|--------|-----------------|
| < 6 m/s | ✅ Safe | Good conditions for flying |
| 6-10 m/s | ⚠️ Caution | Moderate wind - exercise caution |
| > 10 m/s | ❌ Not Safe | High winds - do not fly |

## Configuration

### Adding More Drone Models

Edit the `drone_info()` command to add more models:
```python
elif model.lower() == "your_drone":
    embed.add_field(
        name="Your Drone Model",
        value="**Max Speed:** XX km/h\n**Max Flight Time:** XX min\n**Camera:** Specs\n**Range:** XX km",
        inline=False
    )
```

### Expanding Regulations

Add more countries to the `regulations` dictionary:
```python
regulations = {
    "us": "FAA regulations...",
    "uk": "EASA regulations...",
    "your_country": "Your regulations..."
}
```

### Adding Components

Extend the `components` dictionary:
```python
components = {
    "existing": "...",
    "new_component": "Description of the component"
}
```

## Troubleshooting

### Bot not responding
- Ensure the bot has message permissions in your server
- Check that `MESSAGE_CONTENT_INTENT` is enabled
- Verify your bot token is correct

### Weather command returns error
- Verify your OpenWeatherMap API key is correct
- Check that the city name is spelled correctly
- Ensure your API key is active (not rate-limited)

### Import errors
- Run `pip install --upgrade discord.py aiohttp`
- Ensure Python 3.8+ is installed

## API Documentation

### OpenWeatherMap
- **Endpoint**: Current Weather API
- **Free Tier**: 60 calls/minute
- **Docs**: https://openweathermap.org/current

## Future Enhancements

- Real-time airspace data integration
- Flight simulator integration
- Drone flight log tracking
- Community drone builds showcase
- Maintenance reminders
- Battery calculator
- GPS coordinate validation
- Integration with drone manufacturer APIs

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the repository or contact the developer.

## Disclaimer

This bot provides informational content about drones and regulations. Always follow local laws and regulations regarding drone operation. Check with local aviation authorities before flying. The bot's information is for reference only and should not be relied upon as legal advice.

---

**Happy Flying! 🚁✈️**
