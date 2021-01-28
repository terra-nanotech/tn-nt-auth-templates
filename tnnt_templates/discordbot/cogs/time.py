"""
"Time" cog for discordbot - https://github.com/pvyParts/allianceauth-discordbot
"""

import logging

from datetime import datetime

import pytz

from discord.ext import commands
from discord.embeds import Embed
from discord.colour import Color

from aadiscordbot.app_settings import get_site_url, timezones_active


logger = logging.getLogger(__name__)


class Time(commands.Cog):
    """
    A series of Time tools
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def time(self, ctx):
        """
        Returns EVE Time
        """

        fmt = "%H:%M:%S\n%A %d. %b %Y"
        url = None

        await ctx.trigger_typing()

        embed = Embed(title="Time")
        embed.colour = Color.green()

        embed.add_field(
            name="EVE Time",
            value=datetime.utcnow().strftime(fmt),
            inline=False,
        )

        if timezones_active():
            from timezones.models import Timezones

            url = get_site_url() + "/timezones/"
            configured_timezones = Timezones.objects.filter(is_enabled=True)

            if configured_timezones.count() > 0:
                for configured_timezone in configured_timezones:
                    embed.add_field(
                        name=configured_timezone.panel_name,
                        value=(
                            datetime.utcnow()
                            .astimezone(
                                pytz.timezone(
                                    configured_timezone.timezone.timezone_name
                                )
                            )
                            .strftime(fmt)
                        ),
                        inline=True,
                    )
            else:
                from timezones.constants import AA_TIMEZONE_DEFAULT_PANELS

                configured_timezones = AA_TIMEZONE_DEFAULT_PANELS

                for configured_timezone in configured_timezones:
                    embed.add_field(
                        name=configured_timezone["panel_name"],
                        value=(
                            datetime.utcnow()
                            .astimezone(
                                pytz.timezone(
                                    configured_timezone["timezone"]["timezone_name"]
                                )
                            )
                            .strftime(fmt)
                        ),
                        inline=True,
                    )

        if url is not None:
            embed.add_field(
                name="Timezones Conversion",
                value=url,
                inline=False,
            )

        return await ctx.send(embed=embed)


def setup(bot):
    """
    setup the cog
    :param bot:
    """

    bot.add_cog(Time(bot))
