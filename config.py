import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8242490066:AAFipgPD_KGhaa7vUuevTLG3U_cLm3ol_kE")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27094872"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ce333b172c9eeec0a46d8328fe34d8cf")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "123456789"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sarab9968:XSXhVMVLFJ47Q9am@cluster0.ljeycyu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "beastxsrcb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
