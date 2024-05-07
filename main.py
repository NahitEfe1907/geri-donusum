import discord
from discord.ext import commands
import random

# Discord botunun komutlarını tanımlamak için bir client oluştur
bot = commands.Bot(command_prefix='!')

# Botun hazır olduğunda yapılacak işlemler
@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

# Geri dönüşüm ipuçları komutu
@bot.command()
async def geri_dönüşüm_ipuçları(ctx):
    ipuçları = [
        "Plastik şişelerin kapaklarını ayırarak geri dönüşüm yapın.",
        "Kağıt ürünlerini temizleyerek geri dönüşüme hazır hale getirin.",
        "Cam ürünlerini kırılmadan geri dönüşüm kutularına atın."
    ]
    await ctx.send("\n".join(ipuçları))

# Geri dönüşüm merkezleri komutu
@bot.command()
async def geri_dönüşüm_merkezleri(ctx):
    bilgi = "Yakınınızdaki geri dönüşüm merkezleri ve toplama noktaları için belediyenizin web sitesini ziyaret edebilirsiniz."
    await ctx.send(bilgi)

# Geri dönüşüm istatistikleri komutu
@bot.command()
async def geri_dönüşüm_istatistikleri(ctx):
    # Rastgele bir puan oluştur
    puan = random.randint(0, 100)
    await ctx.send(f'Son 30 gün içindeki geri dönüşüm puanınız: {puan}')

# Geri dönüşüm hatırlatıcıları komutu
@bot.command()
async def geri_dönüşüm_hatırlatıcıları(ctx):
    await ctx.send("Unutmayın! Düzenli olarak geri dönüşüm yapmak çevre için önemlidir.")

# Geri dönüşüm tavsiyeleri komutu
@bot.command()
async def geri_dönüşüm_tavsiyeleri(ctx):
    tavsiyeler = [
        "Organik atıkları kompost yaparak değerlendirin.",
        "Evde kullanmadığınız eşyaları bağışlayarak geri dönüşüm yapın.",
        "Elektronik atıkları geri dönüştürmek için belediyenizin toplama noktalarını kullanın."
    ]
    await ctx.send("\n".join(tavsiyeler))

# Geri dönüşüm görevleri komutu
@bot.command()
async def geri_dönüşüm_görevleri(ctx):
    görevler = [
        "Bu hafta boyunca plastik atıkları ayrı bir kutuda toplayın.",
        "Cam şişeleri geri dönüşüm kutularına atarak çevreye katkıda bulunun.",
        "Kullanılmış kağıtları geri dönüştürerek kağıt tüketimini azaltın."
    ]
    await ctx.send("\n".join(görevler))

# Geri dönüşüm ilhamı komutu
@bot.command()
async def geri_dönüşüm_ilhamı(ctx):
    ilham = [
        "Dünya için bir adım atın, geri dönüşüm yapın!",
        "Çevremizi koruyalım, doğayı temiz tutalım.",
        "Küçük adımlar büyük değişiklikler yapabilir, geri dönüşüm yapmaya bugün başlayın."
    ]
    await ctx.send(random.choice(ilham))

# Geri dönüşüm soru-cevap komutu
@bot.command()
async def geri_dönüşüm_soru_cevap(ctx, soru):
    if soru.lower() == "plastik geri dönüşümü nasıl yapılır?":
        await ctx.send("Plastik geri dönüşümü için plastik ürünleri ayrı bir kutuda toplayın ve geri dönüşüm merkezlerine götürün.")
    elif soru.lower() == "geri dönüşümün çevreye faydaları nelerdir?":
        await ctx.send("Geri dönüşüm çevreye enerji tasarrufu, doğal kaynak koruması ve atık azaltımı gibi birçok fayda sağlar.")

# Geri dönüşüm liderlik tablosu komutu
@bot.command()
async def geri_dönüşüm_liderlik(ctx):
    # Kullanıcıların rastgele puanlar oluşturulur (örnek amaçlı)
    kullanıcılar = ["Kullanıcı1", "Kullanıcı2", "Kullanıcı3"]
    puanlar = [random.randint(0, 100) for _ in kullanıcılar]

    # Liderlik tablosu oluşturulur
    liderlik_tablosu = "Geri Dönüşüm Liderlik Tablosu:\n"
    for kullanıcı, puan in zip(kullanıcılar, puanlar):
        liderlik_tablosu += f"{kullanıcı}: {puan} puan\n"

    await ctx.send(liderlik_tablosu)

# !help komutu
@bot.command()
async def help(ctx):
    komutlar = """
    **Geri Dönüşüm Botu Komutları:**
    !geri_dönüşüm_ipuçları : Geri dönüşüm ipuçları verir.
    !geri_dönüşüm_merkezleri : Yakınınızdaki geri dönüşüm merkezleri hakkında bilgi verir.
    !geri_dönüşüm_istatistikleri : Geri dönüşüm istatistiklerinizi gösterir.
    !geri_dönüşüm_hatırlatıcıları : Geri dönüşüm yapmayı hatırlatır.
    !geri_dönüşüm_tavsiyeleri : Geri dönüşüm tavsiyeleri verir.
    !geri_dönüşüm_görevleri : Geri dönüşüm görevleri oluşturur.
    !geri_dönüşüm_ilhamı : Geri dönüşüm ile ilgili ilham verici mesajlar gönderir.
    !geri_dönüşüm_soru_cevap <soru> : Geri dönüşümle ilgili sorularınıza cevap verir.
    !geri_dönüşüm_liderlik : Geri dönüşüm liderlik tablosunu gösterir.
    """
    await ctx.send(komutlar)

# Diğer komutlar ve özellikler buraya eklenebilir

# Discord botunu çalıştır
bot.run('yor token here')
