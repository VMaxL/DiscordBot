import discord
from discord.ext import commands
import os

# TODO combine week command and PSBA week command to delete copied code
# TODO put the schedule files into a separate folder for cleanup

class Pickems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dic = {"Farmington Feraligatrs": "Eevee",
                    "Netherlands Nidokings": "Max",
                    "Indus Valley Infernapes": "Rohith & Sean",
                    "Vancouver Vespiquen": "Lakanus",
                    "Dutch Swellows": "Victor",
                    "Loli Lopunnys": "Flare",
                    "Boston Sceptiles": "Alex",
                    "Coal Valley Cobalions": "Quin",
                    "Miami Heatran": "Nada",
                    "The Roggen Rollers": "Autumn & Nunes",
                    "Kingston Wooloos": "Mimi",
                    "Adelaide Eelektross": "Jolty"}

    # PICHU pickems command, assumes a few things
    # 1. All weeks have 6 battles 2. The battles are in the format
    # [[team1] \t \t vs. \t \t [team2]\n"
    # 3. The emotes have the same names as the teams minus the spaces in between,
    #       e.g. the emote for "Netherlands Nidokings" is named "NetherlandsNidokings"
    @commands.command()
    async def week(self, ctx, weekNum=None):
        if weekNum == None:
            await ctx.send("Please enter a week number")
        else:
            with open('schedule.txt') as f:
                contents = f.readlines()

            await ctx.send("**--- Week {0} Pickems ---**".format(weekNum))
            numb = 6 * (int(weekNum) - 1)
            for i in contents[numb:numb+6]:
                coach1, coach2 = i.replace("\t", "").replace("\n", "").split("vs.")
                emote1 = discord.utils.get(self.bot.emojis, name=coach1.replace(" ", ""))
                emote2 = discord.utils.get(self.bot.emojis, name=coach2.replace(" ", ""))
                msg = await ctx.send("{0} ({1}) [{2}] vs. {3} ({4}) [{5}]".format(coach1, self.dic[coach1], emote1,
                                                                                  coach2, self.dic[coach2], emote2))
                await msg.add_reaction(emote1)
                await msg.add_reaction(emote2)


    # Basically the same as the week command but uses a different format ni the .txt file
    @commands.command()
    async def PSBAweek(self, ctx, weekNum=None):
        if weekNum == None:
            await ctx.send("Please enter a week number")
        else:
            with open('PSBAschedule.txt') as f:
                contents = f.readlines()

            await ctx.send("**--- Week {0} Pickems ---**".format(weekNum))
            numb = 7 * (int(weekNum) - 1)
            for i in contents[numb:numb + 7]:
                coach1, coach2 = i.replace("\t", "").replace("\n", "").replace("0","").split("vs")
                emote1 = discord.utils.get(self.bot.emojis, name=coach1.replace(" ", ""))
                emote2 = discord.utils.get(self.bot.emojis, name=coach2.replace(" ", ""))
                msg = await ctx.send("{0} [{1}] vs. {2} [{3}]".format(coach1, emote1, coach2, emote2))
                await msg.add_reaction(emote1)
                await msg.add_reaction(emote2)

    @commands.command()
    async def emote(self, ctx, emote=None):
        x = discord.utils.get(self.bot.emojis, name=emote)
        await ctx.send(x)


def setup(bot):
    bot.add_cog(Pickems(bot))
