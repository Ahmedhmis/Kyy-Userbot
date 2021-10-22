# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
# Fix By Kyy @IDnyaKosong


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮"


async def get_call(event):
    kyy = await event.client(getchat(event.chat_id))
    kyy = await event.client(getvc(kyy.full_chat.call))
    return kyy.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Mematikan Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(e):
    await e.edit("`Sedang Mengivinte Member...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`Invited {z} users`")


@register(outgoing=True, pattern=r"^\.vctittle", groups_only=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await e.edit("**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await e.edit("Berhasil Mengubah Judul VCG Menjadi `{title}`")
    except Exception as ex:
        await e.edit(f"**ERROR:** `{ex}`")


CMD_HELP.update({
    "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
    \n↳ : Untuk Memulai voice chat group.\
    \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
    \n↳ : Untuk Memberhentikan voice chat group.\
    \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
    \n↳ : Mengundang Member group ke voice chat group. (You must be joined).\
    \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vctittle`\
    \n↳ : Untuk Mengubah title/judul voice chat group."
})
