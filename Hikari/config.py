class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24537973
    API_HASH = "44b90ee5bfe73b7a7624ab6b55a6fb71"

    CASH_API_KEY = "K4BXMO9H11RWO6YB"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://dwykrhhe:snAGRjL9CAfcwOZAvRqVoGFYSJ9LbbJc@tiny.db.elephantsql.com/dwykrhhe"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001922247598)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Botmusickenz:Fian99kofer@cluster0.2gjgwft.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/a18d00f0a91e6e61f8b03.jpg"
    
    ARQ_API_URL = "http://arq.hamker.dev"
    
    ARQ_API = "HWEZFZ-EUKCYS-JWZPAL-VVSKAJ-ARQ"

    ARQ_API_KEY = "HWEZFZ-EUKCYS-JWZPAL-VVSKAJ-ARQ"

    SUPPORT_CHAT = "ZeroManagerSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6176939566:AAHcnb9ZRAu2jv1LrJ42Gnt3JEibnbNfjKs"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "7WMA3YLV6OEB"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6029970020  # User id of your telegram account (Must be integer)

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
