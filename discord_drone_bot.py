import discord
from discord.ext import commands
import aiohttp
import json
from datetime import datetime

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuration
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
OPENSKY_API = "https://opensky-network.org/api"
DRONEDB_API = "https://api.dronesnap.com"

class DroneBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    async def cog_load(self):
        self.session = aiohttp.ClientSession()

    async def cog_unload(self):
        await self.session.close()

    @commands.command(name='droneinfo')
    async def drone_info(self, ctx, model: str = None):
        """Get information about drone models"""
        embed = discord.Embed(
            title="🚁 Drone Information",
            color=discord.Color.blue(),
            timestamp=datetime.now()
        )
        
        if not model:
            embed.add_field(
                name="Available Commands",
                value="`!droneinfo dji` - DJI drone specs\n`!droneinfo parrot` - Parrot drone specs\n`!droneinfo auterion` - Auterion specs",
                inline=False
            )
        elif model.lower() == "dji":
            embed.add_field(
                name="DJI Air 3S",
                value="**Max Speed:** 75 km/h\n**Max Flight Time:** 46 min\n**Camera:** 48MP + 70mm medium tele\n**Range:** 15 km",
                inline=False
            )
            embed.add_field(
                name="DJI Avata 3",
                value="**Max Speed:** 140 km/h\n**Max Flight Time:** 23 min\n**Camera:** 48MP\n**Type:** FPV Drone",
                inline=False
            )
        elif model.lower() == "parrot":
            embed.add_field(
                name="Parrot Anafi",
                value="**Max Speed:** 55 km/h\n**Max Flight Time:** 26 min\n**Camera:** 48MP + 32x zoom\n**Weight:** 320g",
                inline=False
            )
        else:
            embed.add_field(
                name="Error",
                value=f"Unknown drone model: `{model}`",
                inline=False
            )
        
        await ctx.send(embed=embed)

    @commands.command(name='weather')
    async def check_weather(self, ctx, city: str = None):
        """Check weather conditions for drone flight operations"""
        if not city:
            await ctx.send("❌ Please provide a city name. Usage: `!weather <city>`")
            return

        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            async with self.session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    embed = discord.Embed(
                        title=f"🌤️ Weather for {data['name']}, {data['sys']['country']}",
                        color=discord.Color.green(),
                        timestamp=datetime.now()
                    )
                    
                    temp = data['main']['temp']
                    humidity = data['main']['humidity']
                    wind_speed = data['wind']['speed']
                    description = data['weather'][0]['description']
                    
                    embed.add_field(name="Temperature", value=f"{temp}°C", inline=True)
                    embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
                    embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
                    embed.add_field(name="Conditions", value=description.capitalize(), inline=False)
                    
                    # Flight safety assessment
                    if wind_speed > 10:
                        safety = "❌ **Not Safe** - High wind speeds"
                    elif wind_speed > 6:
                        safety = "⚠️ **Caution** - Moderate wind"
                    else:
                        safety = "✅ **Safe** - Good conditions"
                    
                    embed.add_field(name="Flight Safety", value=safety, inline=False)
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"❌ City not found: {city}")
        except Exception as e:
            await ctx.send(f"❌ Error fetching weather: {str(e)}")

    @commands.command(name='dronebuild')
    async def drone_build(self, ctx, component: str = None):
        """Get drone component recommendations for custom builds"""
        embed = discord.Embed(
            title="🔧 Drone Components",
            color=discord.Color.orange(),
            timestamp=datetime.now()
        )
        
        components = {
            "frame": "Aluminum or Carbon Fiber frames for lightweight durability",
            "motor": "Brushless motors (4-6S LiPo) for efficiency and reliability",
            "esc": "Electronic Speed Controllers for motor regulation",
            "battery": "LiPo or LiPo-S batteries for extended flight time",
            "camera": "HD/4K cameras with stabilization gimbals",
            "reciever": "Radio frequency receivers for control signal",
            "propeller": "Folding or fixed props depending on drone type"
        }
        
        if not component:
            embed.add_field(
                name="Available Components",
                value=", ".join(f"`{c}`" for c in components.keys()),
                inline=False
            )
        elif component.lower() in components:
            embed.add_field(
                name=component.capitalize(),
                value=components[component.lower()],
                inline=False
            )
        else:
            embed.add_field(name="Error", value=f"Unknown component: `{component}`", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='regulations')
    async def drone_regulations(self, ctx, country: str = None):
        """Get drone regulations and flying rules"""
        embed = discord.Embed(
            title="⚖️ Drone Regulations",
            color=discord.Color.red(),
            timestamp=datetime.now()
        )
        
        regulations = {
            "us": "FAA Part 107 rules apply. Fly under 400ft, maintain visual line of sight, no night flights without waiver",
            "uk": "EASA rules. Need flyer ID and operator ID, max 500ft, no populated area flights",
            "eu": "European regulations. Class C drones require special permissions, follow local airspace rules"
        }
        
        if not country:
            embed.add_field(
                name="Available Regions",
                value=", ".join(f"`{c}`" for c in regulations.keys()),
                inline=False
            )
        elif country.lower() in regulations:
            embed.add_field(
                name=country.upper(),
                value=regulations[country.lower()],
                inline=False
            )
        else:
            embed.add_field(
                name="Info",
                value="Country not in database. Check local aviation authority.",
                inline=False
            )
        
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the skies 🚁"))

async def main():
    async with bot:
        await bot.add_cog(DroneBot(bot))
        await bot.start('YOUR_DISCORD_BOT_TOKEN')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
