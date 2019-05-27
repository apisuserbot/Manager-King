if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "805109027:AAFYjw4qRaje4WGdHd1_KxnYzE6v3yXqYfc"
    OWNER_ID = "721198993"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Prakaska"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://qfkohqymejypoc:7f310fd68b37d4f117a2dd4bbb9a52b35729f050ff1123d0baf6b3e449de623b@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d67rh30a38vehf'  # needed for any database modules
    MESSAGE_DUMP = -1001400546607  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = ANYTHING
    URL = "https://thugboy.herokuapp.com/"

    # OPTIONAL
    SUDO_USERS = [578256572 734772540 759400881 594483221 623317613 649156353 656268508 334575345 225296581 621013608]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [578256572 734772540 759400881 594483221 623317613 649156353 656268508 334575345 225296581 621013608]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [578256572 734772540 759400881 594483221 623317613 649156353 656268508 334575345 225296581 621013608]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = 'ed529683f29bb1bfe7a0392b81e37ff8' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
