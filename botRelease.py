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
		await message.channel.send(embed = discord.Embed(title = 'Помощь по командам:', description = ',h - Помощь.\n,getGlobalProfile [Profile URL] - Получить информацию о глобальном профиле.\n,getId [USER | CHAT | BLOG URL] - Вычислить Object ID.\n\ndeveloped by - <@413001095720337409>\npowered by Amino.py', color=0x24ff00))
#
#GETID
#
	if message.content.startswith(',getId'):
		try:
			split = message.content.split(" ")
			id = aminoClient.get_from_code(split[1]).objectId
			await message.channel.send(f"`{id}`")
		except:
			await message.channel.send(embed = discord.Embed(title="Ошибка получения Object ID:", description=":exclamation: | Проверьте правильность написания.", color=0xff0000))
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
			m = uzer.createdTime
			if n == 1:
				n = '✅'
			elif n == 0:
				n = '❎'
			else:
				pass
			if v == 1:
				v = '✔ В сети'
			elif v == 2:
				v = '❌ Не в сети'
			else:
				pass
			await message.channel.send(embed = discord.Embed(title = '{0}'.format(x), description = 'Ник: {0}\nОписание: {1}\nUser ID: {2}\nСсылка на аватар: {3}\nОнлайн статус: {4}\nAminoID: {5}\nAmino+ статус: {6}\nСсылка на пользователя: http://aminoapps.com/u/{7}\nДата создания аккаунта: {8}'.format(x, y, c, z, v, b, n, b, m), color=0x24ff00).set_thumbnail(url=z))
		except:
			await message.channel.send(embed = discord.Embed(title="Ошибка получения глобального профиля:", description=":exclamation: | Проверьте правильность написания.", color=0xff0000))
#
#GET_BLOG_INFO (ADD IT SOON)
#
#	if message.content.startswith(',getBlogInfo'):
#		try:
#			split = message.content.split(" ")
#			id = aminoClient.get_from_code(split[1]).objectId
#			getblog = aminoClient.get_blog_info(id)
#			blog_content = getblog.blog.content
#			blog_title = getblog.blog.title
#			await message.channel.send(embed = discord.Embed(title = f'{blog_title}', description = f'Название поста: {blog_title}\nОписание Поста: {blog_content}\nАйди поста: {id}', color=0x24ff00))
#		except:
#			await message.channel.send(embed = discord.Embed(title="Ошибка получения информации от поста:", description=":exclamation: | Проверьте правильность написания.", color=0xff0000))

#
#CLIENT RUN
#
client.run(token)
