
# / ALL PLUGİNİ / TRCUMHURBASKANI
from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from asyncio import sleep

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("all")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.all(?: |$)(.*)",groups_only=True)
async def _(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(seasons, i.first_name, i.id))
		await sleep(2.5)


@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)", groups_only=True)
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 50:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(seasons, i.first_name, i.id))
		await sleep(1.74)


CmdHelp('all').add_command(
	'all', (LANG['ALL1']), (LANG['ALL2'])
	).add_command(
	"alladmin", (LANG['ALLADMİN1']), (LANG['ALLADMİN2'])
    ).add_command(
    "kill all", None, (LANG['KİLLALL1'])
).add()

