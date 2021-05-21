"""
"About" cog for discordbot - https://github.com/pvyParts/allianceauth-discordbot

Since we don't want to have it branded for "The Initiative", we have to build our own ..
"""

import logging

import pendulum
from aadiscordbot import app_settings
from aadiscordbot.app_settings import get_site_url
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from discord.utils import get

from django.conf import settings

from allianceauth.eveonline.evelinks.eveimageserver import (
    alliance_logo_url,
    corporation_logo_url,
)

logger = logging.getLogger(__name__)


class About(commands.Cog):
    """
    All about me!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self, ctx):
        """
        All about the bot
        """

        await ctx.trigger_typing()

        embed = Embed(title="TN-NT Discord Services")

        try:
            if settings.TNNT_TEMPLATE_ENTITY_ID == 1:
                embed.set_thumbnail(url=get_site_url + "static/icons/allianceauth.png")
            else:
                if settings.TNNT_TEMPLATE_ENTITY_TYPE == "alliance":
                    embed.set_thumbnail(
                        url=alliance_logo_url(settings.TNNT_TEMPLATE_ENTITY_ID, 256)
                    )
                elif settings.TNNT_TEMPLATE_ENTITY_TYPE == "corporation":
                    embed.set_thumbnail(
                        url=corporation_logo_url(settings.TNNT_TEMPLATE_ENTITY_ID, 256)
                    )

        except AttributeError:
            pass

        embed.colour = Color.green()

        embed.description = (
            "This is a multi-functional discord bot tailored "
            "specifically for Terra Nanotech.\n\nType `!help` for more information."
        )

        url = get_site_url()

        embed.add_field(
            name="Auth Link",
            value="[{auth_url}]({auth_url})".format(auth_url=url),
            inline=False,
        )

        embed.set_footer(
            text="Developed by Aaron Kable, forked for Terra Nanotech by Rounon Dax"
        )

        return await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def uptime(self, ctx):
        """
        Returns the uptime
        """

        if ctx.message.author.id not in app_settings.get_admins():
            return await ctx.message.add_reaction(chr(0x1F44E))

        await ctx.send(
            pendulum.now(tz="UTC").diff_for_humans(
                self.bot.currentuptime, absolute=True
            )
        )

    @commands.command(hidden=True)
    async def get_webhooks(self, ctx):
        """
        Returns the webhooks for the channel
        """

        if ctx.message.author.id not in app_settings.get_admins():
            return await ctx.message.add_reaction(chr(0x1F44E))

        hooks = await ctx.message.channel.webhooks()
        if len(hooks) == 0:
            name = "{}_webhook".format(ctx.message.channel.name.replace(" ", "_"))
            hook = await ctx.message.channel.create_webhook(name=name)
            await ctx.message.author.send(f"{hook.name} - {hook.url}")

        else:
            for hook in hooks:
                await ctx.message.author.send(f"{hook.name} - {hook.url}")

        return await ctx.message.delete()

    @commands.command(hidden=True)
    async def new_channel(self, ctx):
        """
        create a new channel in a category.
        """

        if ctx.message.author.id not in app_settings.get_admins():
            return await ctx.message.add_reaction(chr(0x1F44E))

        await ctx.message.channel.trigger_typing()

        input_string = ctx.message.content[13:].split(" ")
        if len(input_string) != 2:
            return await ctx.message.add_reaction(chr(0x274C))

        everyone_role = ctx.guild.default_role
        channel_name = input_string[1]
        target_cat = get(ctx.guild.channels, id=int(input_string[0]))

        found_channel = False

        for channel in ctx.guild.channels:  # TODO replace with channel lookup not loop
            if channel.name.lower() == channel_name.lower():
                found_channel = True

        if not found_channel:
            channel = await ctx.guild.create_text_channel(
                channel_name.lower(), category=target_cat
            )  # make channel

            await channel.set_permissions(
                everyone_role, read_messages=False, send_messages=False
            )

        return await ctx.message.add_reaction(chr(0x1F44D))

    @commands.command(hidden=True)
    async def add_role(self, ctx):
        """
        add a role from a channel.
        """

        if ctx.message.author.id not in app_settings.get_admins():
            return await ctx.message.add_reaction(chr(0x1F44E))

        await ctx.message.channel.trigger_typing()

        input_string = ctx.message.content[10:].split(" ")
        if len(input_string) != 2:
            return await ctx.message.add_reaction(chr(0x274C))

        target_role = get(ctx.guild.roles, name=input_string[1])
        channel_name = get(ctx.guild.channels, name=input_string[0])

        if channel_name:
            await channel_name.set_permissions(
                target_role, read_messages=True, send_messages=True
            )

        return await ctx.message.add_reaction(chr(0x1F44D))

    @commands.command(hidden=True)
    async def rem_role(self, ctx):
        """
        remove a role from a channel.
        """

        if ctx.message.author.id not in app_settings.get_admins():
            return await ctx.message.add_reaction(chr(0x1F44E))

        await ctx.message.channel.trigger_typing()

        input_string = ctx.message.content[10:].split(" ")
        if len(input_string) != 2:
            return await ctx.message.add_reaction(chr(0x274C))

        target_role = get(ctx.guild.roles, name=input_string[1])
        channel_name = get(ctx.guild.channels, name=input_string[0])

        if channel_name:
            await channel_name.set_permissions(
                target_role, read_messages=False, send_messages=False
            )

        return await ctx.message.add_reaction(chr(0x1F44D))


def setup(bot):
    """
    setup the cog
    :param bot:
    """

    bot.add_cog(About(bot))
