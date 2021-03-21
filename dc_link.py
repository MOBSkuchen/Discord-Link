#Discord Link main file (only file lol)
#heres the code:
import random, string, discord
verified = "false"
def get_random_str(length):
    letters = string.ascii_lowercase
    scc = ''.join(random.choice(letters) for i in range(length))
    return scc
def say(author, content):
    author = author[:-5]
    sads = (author + "says:" + content)
    import win32com.client as wcc
    class Sprecher(object):
        def __init__(self):
            self.speaker = wcc.Dispatch("SAPI.SpVoice")
            self.sprechen()
        def sprechen(self):
            fasd = 90
            gdfh = 0
            juzk = 0
            textApp = sads
            tonSchnelle = int(juzk)
            tonLage = int(gdfh)
            tonVolume = int(fasd)
            self.speaker.Rate = tonSchnelle
            self.speaker.Volume = tonVolume
            text = """<pitch middle="{0}" > {1} </pitch> """.format(tonLage, textApp)
            self.speaker.Speak(text)
    a = Sprecher()
def decline_svr():
    print("Session not verified.")
    print("Try again.")
    verify()
def accept_svr():
    print("Your Session request was verified.")
    print("...")
    global verified
    verified = "true"
def verify():
    global name, scc
    scc = (get_random_str(5))
    name = input("What is your Discord-Name? (+Tag) ")
    print("Ok, your Code is " + scc + " usage: !verify " + scc)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as ' + str(self.user))
        print("...")
        verify()
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!notify'):
            smc = str("{0.author}".format(message))
            cmt = ("You got notified by " + smc)
            print(cmt)
        if message.content.startswith("!verify "):
            un = str("{0.author}".format(message))
            if un == name:
                con = str("{0.content}".format(message))
                await message.delete()
                de = con.replace("!verify ", "")
                if de == scc:
                    await message.channel.send("User Session verified.")
                    accept_svr()
                else:
                    await message.channel.send("User Session not verified.")
                    decline_svr()
            else:
                await message.channel.send("User Session not verified.")
                decline_svr()
        if message.content.startswith(''):
            author = str("{0.author}".format(message))
            con = str("{0.content}".format(message))
            if verified == "true":
                say(author, con)
                print(author + ": " + con)
client = MyClient()
client.run('ODEwOTcxODMwNzYwMjQzMjMx.YCraXw.r60OkWgNAdfYEli6mRb2IaVUeN8')
#and heres a cat
#                           |        |
#                           |\      /|
#                           | \____/ |
#                           |  /\/\  |
#                          .'___  ___`.
#                         /  \|/  \|/  \
#        _.--------------( ____ __ _____)
#     .-' \  -. | | | | | \ ----\/---- /
#   .'\  | | / \` | | | |  `.  -'`-  .'
#  /`  ` ` '/ / \ | | | | \  `------'\
# /-  `-------.' `-----.       -----. `---.
#(  / | | | |  )/ | | | )/ | | | | | ) | | )
# `._________.'_____,,,/\_______,,,,/_,,,,/
#
#------------------------------------------------
#from https://asciiart.website/index.php?art=animals/cats
