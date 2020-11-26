#
#IMPORTS
#
import os
import discord
import amino
#
#VARIABLES
#
token = os.getenv("TOKEN")
client = discord.Client()
aminoClient = amino.Client()
#
#ON_READY
#
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    activity = discord.Game(name=",h | @adskoe96", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
#
#START & HELP MENU
#
@client.event
async def on_message(message):
	if message.content.startswith(',h'):
		await message.channel.send(embed = discord.Embed(title = 'Помощь по командам:', description = ',h - Помощь.\n,getGlobalProfile [Profile URL] - Получить информацию о глобальном профиле.\n,getId [USER | CHAT | BLOG URL] - Вычислить Object ID.\n,updates - Узнать нововведения бота.\n\ndeveloped by - <@413001095720337409>\npowered by Amino.py', color=0x24ff00))
#
#GETID
#
	if message.content.startswith(',getId'):
		try:
			split = message.content.split(" ")
			id = aminoClient.get_from_code(split[1]).objectId
			await message.channel.send(id)
		except:
			await message.channel.send(embed = discord.Embed(title="Ошибка получения Object ID:", description="Проверьте правильность написания.", color=0xff0000))
#
#GET_GLOBAL_PROFILE
#
	if message.content.startswith(',getGlobalProfile'):
		try:
			split = message.content.split(" ")
			id = aminoClient.get_from_code(split[1]).objectId
			uzer = aminoClient.get_user_info(id)
			x = uzer.nickname
			y = uzer.content
			z = uzer.icon
			c = uzer.userId
			v = uzer.onlineStatus
			b = uzer.aminoId
			n = uzer.accountMembershipStatus
			if n == 1:
				n = 'Amino+ в наличии'
			elif n == 0:
				n = 'Amino+ отсутствует'
			else:
				pass
			if v == 1:
				v = '✔ В сети'
			elif v == 2:
				v = '❌ Не в сети'
			else:
				pass
			await message.channel.send(embed = discord.Embed(title = '{0}'.format(x), description = 'Ник: {0}\nОписание: {1}\nUser ID: {2}\nСсылка на аватар: {3}\nОнлайн статус: {4}\nAminoID: {5}\nAmino+ статус: {6}\nСсылка на пользователя: http://aminoapps.com/u/{7}'.format(x, y, c, z, v, b, n, b), color=0x24ff00).set_thumbnail(url=z))
		except:
			await message.channel.send(embed = discord.Embed(title="Ошибка получения глобального профиля:", description="Проверьте правильность написания.", color=0xff0000))
#
#UPDATES
#
	if message.content.startswith(',updates'):
		try:
			await message.channel.send(embed = discord.Embed(title="AminoBot 0.15", description="https://pastebin.com/raw/CJ9JY79Q", color=0x0000ff))
		except:
			await message.channel.send(embed = discord.Embed(title="Ошибка на получение информации об обновлениях:", description="Проверьте правильность написания.", color=0xff0000))

#
#CLIENT RUN
#
client.run(token)
