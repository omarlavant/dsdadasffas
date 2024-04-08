import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import requests
import json

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

#HELP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@bot.command()
async def code(ctx):
    embed = discord.Embed(title="Help on BOT", description="Some useful commands")
    embed.add_field(name="$hello", value="Greets the user")
    embed.add_field(name="$users", value="Prints number of users")
    embed.add_field(name="$clean <num>", value="Deletes messages")
    embed.add_field(name="$roll <num>", value="Rolls the dice")
    embed.add_field(name="$quote", value="Prints inspirational quotes")
    embed.add_field(name="$offline <num>", value="Shutdown the bot or turn of some minutes")
    embed.add_field(name="$guess <num>", value="Number guessing game")
    await ctx.send(embed=embed)


@bot.command(name='ban', help='Kullanıcıyı banlar')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    # Kullanıcı banlanacak mı diye kontrol edilir
    if not member.bannable:
        await ctx.send("Bu kullanıcıyı banlayamam. Belki daha yüksek bir role sahiptir.")
        return

    # Ban atılacak kullanıcının ID'si alınır
    user_id = member.id

    # Kullanıcı banlanır
    await member.ban(reason=reason)

    # Ban atılan kullanıcının ID'si ve sebep yazdırılır
    await ctx.send(f'{member.mention} kullanıcısı banlandı. Sebep: {reason}')

    # Banlanan kullanıcının ID'si ve sebep log kanalına yazdırılır (isteğe bağlı)
    log_channel_id = 123456789012345678  # Log kanalının ID'si
    log_channel = ctx.guild.get_channel(log_channel_id)
    if log_channel:
        await log_channel.send(f'{member.mention} ({user_id}) kullanıcısı banlandı. Sebep: {reason}')

@bot.command
async def on_message(message):
    if message.author == bot.user:
        return
    
    elif message.content.startswith('$merhaba'):
        await message.channel.send("OOO! Paşam gelmiş, hoş gelmiş.")

    elif message.content.startswith('$gülegüle'):
        await message.channel.send("\\U0001f642"),
    

    elif message.content.startswith('$küresel ısınma'):
     await message.channel.send("Dünyanın hiçbir köşesi iklim değişikliğinin yıkıcı sonuçlarından muaf değil.Artan sıcaklıklar çevresel bozulmayı, doğal afetleri, aşırı hava koşullarını, gıda ve su güvensizliğini, ekonomik bozulmayı, çatışmayı ve terörizmi körüklüyor. Deniz seviyeleri yükseliyor, Kuzey Kutbu eriyor, mercan resifleri ölüyor, okyanuslar asitleniyor ve ormanlar yanıyor. İşlerin her zamanki gibi yeterince iyi olmadığı açık. İklim değişikliğinin sonsuz maliyeti geri dönülemez boyutlara ulaşırken, şimdi cesur kolektif eylem zamanı.")

    elif message.content.startswith('$küresel ısınma sonuçları'):
        await message.channel.send("Sera gazı emisyonları Dünya'yı kapladığından güneşin ısısını hapsediyorlar. Bu da küresel ısınmaya ve iklim değişikliğine yol açıyor. Dünya artık kayıtlı tarihin herhangi bir noktasından daha hızlı ısınıyor. Zamanla artan sıcaklıklar hava düzenlerini değiştiriyor ve doğanın olağan dengesini bozuyor. Bu durum insanlar ve Dünya üzerindeki diğer tüm yaşam formları için pek çok risk oluşturmaktadır.")


    elif message.content.startswith('$enayrıntılıbilgi'):
        await message.channel.send("Kömür, petrol ve gaz üretiminin bir sonucu olarak her yıl atmosfere milyarlarca ton CO2 salınıyor. İnsan faaliyetleri rekor düzeyde sera gazı emisyonu üretiyor ve hiçbir yavaşlama belirtisi yok. UNEP Emisyon Açığı raporlarının on yıllık özetine göre, “işlerin olağan seyrinde” gidişatını sürdürme yolunda ilerliyoruz.")

    else:
        await message.channel.send(message.content)
@bot.command
async def on_message(message):
    async def hello(ctx):
     await ctx.send('Hello! Welcome :D')

def get_global_warming_info():
    url = "https://api.climateapi.io/globalwarming"
    response = requests.get(url)
    data = response.json()
    return data



# '!isınma' komutu ile küresel ısınma bilgilerini gösteren komut
@bot.command(name='isınma', help='Küresel ısınma hakkında bilgi alın')
async def global_warming_info(ctx):
    data = get_global_warming_info()
    message = f"**Küresel Isınma Bilgileri**\n\n"
    message += f"Ortalama Sıcaklık Artışı: {data['data']['current']['temperature']}°C\n"
    message += f"Son 50 Yılın Ortalama Sıcaklık Artışı: {data['data']['historical']['temperature']}°C\n"
    message += f"Deniz Seviyesi Yükselmesi: {data['data']['current']['sealevel']} mm\n"
    message += f"Son 50 Yılın Ortalama Deniz Seviyesi Yükselmesi: {data['data']['historical']['sealevel']} mm\n"
    await ctx.send(message)




# Rol verme komutu
@bot.command()
async def rolver(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'{member.mention} kullanıcısına {role.name} rolü verildi!')

# Hata yönetimi
@rolver.error
async def rolver_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Kullanım: !hacknickname <kullanıcı_adı> <rol_adı>')















@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready to go!')

@bot.command(name='join', help='Botu ses kanalına davet eder')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='Botu ses kanalından çıkarır')
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name='play', help='YouTube üzerinden müzik çalar')
async def play(ctx, url):
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_channel = get(ctx.guild.voice_channels, name=ctx.author.voice.channel.name)
        voice_channel.play(discord.FFmpegPCMAudio(url2))
