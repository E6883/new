""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/xz5pd)"
        "\n[Repo](https://github.com/E6883/new)"
        "\n[Instagram](Instagram.com/)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/xz5pd/new/new/varshelper.txt)")


CMD_HELP.update({
    "lordhelper":
    "`.lordhelp`\
\nPenjelasan: Bantuan Untuk Userbot.\
\n`.lordvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
