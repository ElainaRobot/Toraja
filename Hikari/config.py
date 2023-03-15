class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 18696108
    API_HASH = "270761e7fab5f5955102efcfab79725c"

    CASH_API_KEY = "JGI67Y9D1LGXYFSB"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://dwykrhhe:snAGRjL9CAfcwOZAvRqVoGFYSJ9LbbJc@tiny.db.elephantsql.com/dwykrhhe"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001832806148)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Botmusickenz:Fian99kofer@cluster0.2gjgwft.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/51c8712f990fd5ab751b8.jpg"
    
    ARQ_API_URL = "http://arq.hamker.dev"
    
    ARQ_API = "HWEZFZ-EUKCYS-JWZPAL-VVSKAJ-ARQ"

    ARQ_API_KEY = "HWEZFZ-EUKCYS-JWZPAL-VVSKAJ-ARQ"

    SUPPORT_CHAT = "YanzzSupportt"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5614679023:AAGVV1kI9rMpQXQxRznlreZs0zImFGypAIM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "7WMA3YLV6OEB"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1141626067  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
