import discord
import asyncio
from discord.ext import commands
from discord.utils import get



client = discord.Client()




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('with Skiera´s mom'),status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('crashing Skiera'), status=discord.Status.online)
        await asyncio.sleep(3)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$gay"):
        await message.channel.send("Gay men are 10-15 times more likely than straight men to have eating disorders. 40% to 60% of serial killers are homosexuals. Homosexual men are more likely to have been abused by their partners than straight men. Monogamy is not a central feature of most homosexual relationships. Married homosexual are 50% more likely than straight couples to divorce. In the Netherlands, the average homosexual in a 'steady relationship' has seven to eight affairs per year. Over 20% of older homosexuals have had more than 500 different sex partners. The average gay man has several dozen sex partners per year. 28% of homosexuals have has sex with over a thousand Most 'long term relationships' between gay men last less than eight years. Among gay Canadian men is 'committed relationships, only 25% here' monogamous. In one study, only 9% of gay men were monogamous.")

    if message.content.startswith('$kys'):
        for j in range(10):
            await message.channel.send("<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!\r\n"
                                       "<@!615665475430383673> sucks dicks for free!")

    if message.content.startswith('aayan9016'):
        for j in range(3):
            await message.channel.send("He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder\r\n"
                                   "He is a fucking gay ass stupid cringy modder")

    if message.content.startswith('skiera'):
        for j in range(1):
            await message.channel.send("Skiera? He is a gay ass polish faggot\r\n"
                                       "Skiera? He is a gay ass polish faggot\r\n"
                                       "Skiera? He is a gay ass polish faggot\r\n"
                                       "Skiera? He is a gay ass polish faggot\r\n"
                                       "Skiera? He is a gay ass polish faggot")

    if message.content.startswith('$nigga'):
        for j in range(1):
            await message.channel.send("Blacks commit 53% of all murder, despite being only 12% of the population.\r\n"
                                       "Source: FBI Crime in America 2018 Database\r\n"
                                       "Blacks make up 56.2% of all serial killers, despite being only 12% of the population. Source: Radford University Serial Killer Database\r\n"
                                       "Despite making up less than 7% of the US population, and only 12% of the\r\n"
                                       "male population, black males commit 1 in every 3 rapes. Source: FBI Crime in\r\n"
                                       "America 2013 Database\r\n"
                                       "Blacks commit 56% of all robbery, despite being only 12% of the population. \r\n"
                                       "Source: FBI Crime in America 2013 Database\r\n"
                                       "Young black men kill 14X more than young white men. Source: Time\r\n"
                                       "Magazine\r\n"
                                       "African Americans commit 1 in 3 aggravated assaults, despite being only 12% \r\n"
                                       "of the population. Source: FBI Crime in America 2013 Database\r\n"
                                       "African Americans commit 41% of all prostitution offenses, despite being \r\n"
                                       "only 12% of the population. Source: FBI Crime in America 2013 Database\r\n"
                                       "African Americans commit 1 in 3 burglaries, arson crimes, fraud crimes and \r\n"
                                       "offenses against family/children, despite being only 12% of the population.\r\n"
                                       "Source: FBI Crime in America 2013 Database\r\n"
                                       "Blacks accounted for a notable 42 percent of all cop killers in 2013. Source: \r\n"
                                       "FBI 2013 Statistics on Law Enforcement Officers Killed and Assaulted\r\n"
                                       "Blacks victims of homicide are 93% of the time killed by other blacks. Source: \r\n"
                                       "US Department of Justice\r\n"
                                       "In 2006, blacks made up nearly 40% of the total prison population, despite\r\n"
                                       "being only 12% of the general population. Source: Bureau of Justice\r\n"
                                       "Poor whites commit less crime than niģgers.")





client.run("ODIyODAyMjUyMjY3NjUxMDgy.YFXkTw.TjBcie1R0jw76Ne8yzYOUaXtiiE")



