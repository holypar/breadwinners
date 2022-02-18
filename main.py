#Import Discord Package
import discord
import keep_alive
from discord.ext import commands
import pandas as pd
import bs4
import requests
import os



client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game('with all this bread!'))




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$commands"):
        myCommands = discord.Embed(title= f"Commands", color = 0x5db35d)
        myCommands.add_field(name = "$price", value= "Returns the current stock ticker price.")
        myCommands.add_field(name = "$ptarget", value= "Returns 12-month price forecasts according to multiple analysts")
        myCommands.set_footer(text="Lets get that bread!")
        myCommands.set_author(name ="BreadWinner$ Bot")
        await message.channel.send(embed = myPrice)

    if message.content.startswith('$price'):
        #Splitting the input from $price to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://finance.yahoo.com/quote/"

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        stock_price = soup.findAll(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text
        myPrice = discord.Embed(title= f"➤ {stock.upper()}", color = 0x5db35d)
        myPrice.add_field(name = "Current Price", value= f"The stock price for {stock.upper()} is ${stock_price} currently.")
        myPrice.set_footer(text="Lets get those profits!")
        myPrice.set_author(name ="Profits Bot")
        await message.channel.send(embed = myPrice)
        

    if message.content.startswith('$ptarget'):  #price target
        #Splitting the input from $ptarget to read input text from user.
        stock = message.content.split(' ')[1]
        url = "https://money.cnn.com/quote/forecast/forecast.html?symb="

        full_url = url + stock

        response = requests.get(full_url).content

        soup = bs4.BeautifulSoup(response, 'html.parser')

        price_target = soup.findAll(class_ = "wsod_twoCol clearfix")[0].text

        myPriceTargetEmbed = discord.Embed(title= f"➤ {stock.upper()}", color = 0x5db35d)
        myPriceTargetEmbed.add_field(name = "Stock Forecast", value = price_target)
        myPriceTargetEmbed.set_footer(text="Lets get those profits!")
        myPriceTargetEmbed.set_author(name ="Profits Bot")
        await message.channel.send(embed = myPriceTargetEmbed)


keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)