from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "22127557")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "348f141a89ba55603d4c9360de9c5625")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6769506933:AAHwL-V4chkiTwTxH1Ax-nSxcRA8FuXr02g")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBu4aD5e6yLPCiUt5CF-j4b9REjMhCqUmM540uGRRwxI3T-PB-G8hngas3RYiUkVaCwzGQFkIFCdhMppe8r3SkxTdfXHwgAV779L8Y8ptsFGFUyVR8VhXaR5KI_HMtAcjth597gpvaJR43Yefc7R7uMXqe2NXyH53quvNYWvmt2qAguuZ2yQA9_ZXL1Sk6p1uygITokNFJB3f-Kmb2UDUf8wgJ4Gh8IGXI2x03oj68TjQjZmPTJXkVxbN2JMrrRTU0bUnMdpwenLAztxEQz__aEaIO_s5kWwjoQ4RBCLaRAY0E7ygyWpB4jEVR0cpPeDruw03scvE9zFZq4BK6O2S-iKM=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "iTsFlNe") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "sonng") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "assemble12bot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "iFlne") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6503661800").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6503661800").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
