import discord
from discord.ext import commands
import os
import json
client = commands.Bot(command_prefix=";")
import asyncio
from persp import score
import persp



@client.event
async def on_ready():
	print("IM READY LOL")

client.remove_command("help")

@client.command()
async def suspend(ctx):
    if ctx.author.id == 687673595153219602:
        await ctx.bot.logout()


@client.command()
async def stats(ctx,member:discord.Member):
        await open_user(member)
        user = member
        pfp = member.avatar_url
        user = member
        with open("users.json","r") as f:
            users = json.load(f)
        toxic = users[str(user)]["Toxic Rating"]
        flirt_rating = users[str(user)]["Flirt Rating"]
        mesg = users[str(user)]["Messages Recorded"]
        a=users[str(user)]["0.9+"]
        b=users[str(user)]["0.8+"]
        c=users[str(user)]["0.7+"]

        embed = discord.Embed(title = f"Report for {user}" ,colour = discord.Colour.orange())
        embed.add_field(name = "Toxicity Rating", value = toxic,inline =False)
        embed.add_field(name = "Flirt Rating", value = flirt_rating,inline =False)
        embed.add_field(name = "Messages Recorded", value = mesg,inline =False)
        embed.add_field(name = " No of Very Toxic Messages Sent",value = a,inline =False)
        embed.add_field(name = " No of Slightly Toxic Messages Sent",value = b,inline =False)
        embed.add_field(name = " No of Potentially Toxic Messages Sent",value = c,inline =False)
        embed.set_thumbnail(url= pfp)

        await ctx.channel.send(embed = embed)
    
    
@client.command()
async def open_user(user):
    with open("users.json","r") as f:
        users = json.load(f)

    if str(user) in users:
        return False
    else:
        users[str(user)]={}
        users[str(user)]["Toxic Rating"]=0
        users[str(user)]["Flirt Rating"]=0
        users[str(user)]["toxic score"]=0
        users[str(user)]["Messages Recorded"]=0
        users[str(user)]["0.9+"]=0
        users[str(user)]["0.8+"]=0
        users[str(user)]["0.7+"]=0
        users[str(user)]["flirt"]=0

        with open("users.json","w") as f:
            json.dump(users,f)





@client.event
async def on_message(msg):
    if msg.author==client.user:
            return

    print(msg.content)
    user = msg.author
    score(msg.content)
    toxicvalue = float(persp.toxic_value)
    flirtvalue = float(persp.flirt_value)
    url= msg.jump_url
    channl=client.get_channel(840114052482990090)
    
    print(user)

    with open("users.json","r") as f:
        users = json.load(f)

    if str(user) in users:
        with open("users.json","r") as f:
            users = json.load(f)
        

        users[str(user)]["toxic score"] += toxicvalue
        users[str(user)]["Messages Recorded"]+=1
        users[str(user)]["flirt"]+=flirtvalue
        toxic_score = users[str(user)]["toxic score"]
        flirt_score = users[str(user)]["flirt"]
        mesg = users[str(user)]["Messages Recorded"]
        users[str(user)]["Toxic Rating"]= toxic_score/mesg
        users[str(user)]["Flirt Rating"] = flirt_score/mesg
        
    else:
        users[str(user)]={}
        users[str(user)]["Toxic Rating"]=0
        users[str(user)]["toxic score"]=0
        users[str(user)]["Flirt Rating"] = 0
        users[str(user)]["0.9+"]=0
        users[str(user)]["0.8+"]=0
        users[str(user)]["0.7+"]=0
        users[str(user)]["flirt"]=0
        users[str(user)]["Messages Recorded"]=0

        with open("users.json","w") as f:
            users = json.dump(users , f)


        with open("users.json","r") as f:
            users = json.load(f)
        
        users[str(user)]["toxic score"] += toxicvalue
        users[str(user)]["Messages Recorded"]+=1
        users[str(user)]["flirt"]+=flirtvalue
        toxic_score = users[str(user)]["toxic score"]
        flirt_score = users[str(user)]["flirt"]
        mesg = users[str(user)]["Messages Recorded"]
        users[str(user)]["Toxic Rating"]= toxic_score/mesg
        users[str(user)]["Flirt Rating"] = flirt_score/mesg
        





        

    
    
    with open("users.json","w") as f:
            json.dump(users,f)
            
            

    

    if toxicvalue >=0.84:
        with open("users.json","r") as f:
            users = json.load(f)
        users[str(user)]["0.9+"]+=1
        with open("users.json","w") as f:
            json.dump(users,f)
        await msg.add_reaction("👿")
        embed = discord.Embed(title = "Message Flagged for Toxicity",colour = discord.Colour.orange())
        embed.add_field(name = "Content", value = msg.content,inline =False)
        embed.add_field(name = "User", value = msg.author,inline =False)
        embed.add_field(name = "link",value = url, inline = False)
        if msg.guild.id == 819906864258089040:
            chnl=client.get_channel(820997954701492255)
            await chnl.send(embed = embed)
        elif msg.guild.id == 814543377919508570:
            chnl=client.get_channel(833605799979778098)
            await chnl.send("<@&833605902237171722>",embed = embed)
        elif msg.guild.id == 806257058558640130:
            chnl = client.get_channel(811171032860721184)
            await chnl.send(embed = embed)

    
    elif 0.8 < toxicvalue < 0.9:
        with open("users.json","r") as f:
            users = json.load(f)
        users[str(user)]["0.8+"]+=1

        with open("users.json","w") as f:
            json.dump(users,f)

    elif 0.7 < toxicvalue < 0.8:
        with open("users.json","r") as f:
            users = json.load(f)
        
        users[str(user)]["0.7+"]+=1

        with open("users.json","w") as f:
            json.dump(users,f)


    elif persp.flirt_value >=0.85:
        if msg.content=="<:cute:826710691628711976>":
            return False
        else:
            with open("users.json","r") as f:
                users = json.load(f)
            users[str(user)]["flirt"]+=1
            with open("users.json","w") as f:
                json.dump(users,f)
            await msg.add_reaction("❤️")
            embed = discord.Embed(title = "Message Flagged for Flirtatious",colour = discord.Colour.orange())
            embed.add_field(name = "Content", value = msg.content,inline =False)
            embed.add_field(name = "User", value = msg.author,inline =False)
            embed.add_field(name = "link",value = url, inline = False)
        if msg.guild.id == 819906864258089040:
            chnl=client.get_channel(820997954701492255)
            await chnl.send(embed = embed)
        elif msg.guild.id == 814543377919508570:
            chnl=client.get_channel(840114052482990090)
            await chnl.send("<@&833605902237171722>",embed = embed)
        elif msg.guild.id == 806257058558640130:
            chnl = client.get_channel(811171032860721184)
            await chnl.send(embed = embed)
    
    await client.process_commands(msg)
        

        



client.run("ODE0NTk5NDExNDY3ODEyODk0.YDgM0g.ZvSj3qCEO06WHSJe7IxK99xpMWo")
