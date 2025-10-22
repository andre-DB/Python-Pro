import discord
import random
import requests
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'El bot se ha iniciado como {bot.user}')

# -------- COMANDOS BÁSICOS --------

@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola! Soy el bot {bot.user} 🤖')

@bot.command()
async def heh(ctx, cantidad: int = 5):
    await ctx.send("he" * cantidad)

@bot.command()
async def sumar(ctx, num1: int = None, num2: int = None):
    if num1 is None or num2 is None:
        await ctx.send("❗ Usa el comando así: `!sumar 5 10`")
        return
    try:
        await ctx.send(f"La suma es: **{num1 + num2}**")
    except Exception:
        await ctx.send("⚠️ Solo puedes sumar números enteros.")

@bot.command()
async def repetir(ctx, veces: int, *, texto='repitiendo...'):
    for i in range(veces):
        await ctx.send(texto)

@bot.command()
async def meme(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)   

@bot.command()
async def manualidad(ctx):
    """Da una idea de manualidad con materiales reciclados 🎨"""
    ideas = [
        "🪴 Usa botellas plásticas para hacer macetas pequeñas decoradas.",
        "💡 Convierte una caja de cartón en un organizador para tu escritorio.",
        "🎠 Con tapas de botellas puedes hacer collares o móviles decorativos.",
        "🕯️ Usa frascos de vidrio como portavelas o lámparas artesanales."
    ]
    await ctx.send(random.choice(ideas))

@bot.command()
async def reciclar(ctx, *, objeto):
    """Informa si un objeto se puede reciclar ♻️"""
    reciclables = {
        "botella": "♻️ Sí, las botellas plásticas se reciclan. Límpiala y llévala al punto verde.",
        "papel": "📄 Sí, pero asegúrate de que no esté sucio o mojado.",
        "cartón": "📦 Sí, se recicla fácilmente. Aplánalo antes de llevarlo.",
        "vidrio": "🍾 Sí, el vidrio es 100% reciclable.",
        "plástico": "♻️ Depende del tipo. Revisa el número dentro del triángulo de reciclaje.",
        "pilas": "❌ No se tiran a la basura. Llévalas a un punto de recolección especial.",
        "ropa": "👕 Sí, dónala o lleva los textiles a un centro de reuso."
    }
    objeto = objeto.lower()
    if objeto in reciclables:
        await ctx.send(reciclables[objeto])
    else:
        await ctx.send("🤔 No tengo información sobre ese objeto. Prueba con: botella, papel, cartón, vidrio, plástico, pilas o ropa.")

@bot.command()
async def ecoimagen(ctx):
    """Envía una imagen inspiradora sobre el planeta 🌍"""
    imagenes = [
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1470770903676-69b98201ea1c",
        "https://images.unsplash.com/photo-1493810329807-1f92e378d7f9"
    ]
    embed = discord.Embed(title="🌿 Cuida el planeta, es tu hogar.")
    embed.set_image(url=random.choice(imagenes))
    await ctx.send(embed=embed)

@bot.command()
async def descomposición(ctx, *, objeto):
    """Muestra el tiempo de descomposición de un objeto ⏳"""
    tiempos = {
        "botella": "🧴 Una botella plástica tarda unos 450 años en descomponerse 😬",
        "papel": "📄 El papel tarda entre 2 a 6 semanas en descomponerse 🌱",
        "cartón": "📦 El cartón tarda unos 2 meses en descomponerse 🍂",
        "vidrio": "🍾 El vidrio puede tardar más de 4,000 años o nunca desaparecer 😱",
        "plástico": "♻️ El plástico común tarda entre 100 y 1,000 años 🧃",
        "pilas": "🔋 Las pilas pueden tardar entre 500 y 1,000 años, y contaminan mucho ⚠️",
        "ropa": "👕 La ropa de algodón tarda unos 5 meses, pero la sintética puede durar siglos 👖"
    }

    objeto = objeto.lower()
    if objeto in tiempos:
        await ctx.send(tiempos[objeto])
    else:
        await ctx.send("🤔 No tengo info sobre ese objeto. Prueba con: botella, papel, cartón, vidrio, plástico, pilas o ropa.")

# -------- COMANDO DE AYUDA (EMBED EN ESPAÑOL) --------

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="📘 Centro de ayuda del bot",
        description="Hola 👋 soy un bot creado con **Python** y la librería **discord.py**.\n\nAquí puedes ver lo que puedo hacer:",
        color=discord.Color.gold()
    )

    embed.add_field(
        name="`$hola`",
        value="El bot te saluda con un mensaje amistoso.",
        inline=False
    )
    embed.add_field(
        name="`$heh [número]`",
        value="Repite la sílaba *he* varias veces. Ejemplo: `$heh 5`",
        inline=False
    )
    embed.add_field(
        name="`$sumar [num1] [num2]`",
        value="Suma dos números. Ejemplo: `$sumar 3 7`",
        inline=False
    )
    embed.add_field(
        name="`$repetir [veces] [texto]`",
        value="Repite el texto las veces que digas. Ejemplo: `$repetir 3 hola`",
        inline=False
    )

    await ctx.send(embed=embed)



# -------- EVENTO DE ERROR GLOBAL --------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Faltan argumentos en el comando.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❓ Ese comando no existe. Usa `!ayuda` para ver la lista.")
    else:
        await ctx.send("⚠️ Ocurrió un error inesperado.")

# -------- EJECUTAR EL BOT --------
bot.run("")
