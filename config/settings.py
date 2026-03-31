from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

#____PATHS____
PROJECT_ROOT = Path(__file__).resolve().parent.parent 
#Path(file).resolve obtains the full absolute path of this setting file, parent goes up one folder (to config), so parent 
#Twice goes to the project root, this way it stays general no matter where this repo is


DATA_DIR = PROJECT_ROOT/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
PROCESSED_DATA_DIR = DATA_DIR/"processed"
DB_PATH = DATA_DIR / "qts.db"

OUTPUTS_DIR = PROJECT_ROOT/"outputs"
LOGS_DIR = PROJECT_ROOT/"logs"


#____UNIVERSE____
UNIVERSE = ["AAPL", "JPM", "XOM", "JNJ", "WMT" ]
BENCHMARK = "SPY"
ASSET_CLASS = "equities"


#____DATE RANGE____
START_DATE = "2010-01-01"
END_DATE = datetime.today().strftime('%Y-%m-%d')

#____DATA PARAMETERS____
BAR_FREQUENCY = "1d"
AUTO_DOWNLOAD = True
SAVE_RAW_DATA = True
USE_ADJUSTED_PRICES = True
OVERWRITE_RAW_DATA = False
DROP_MISSING_ROWS = True

DATE_COLUMN = "Date"
PRICE_COLUMN = "Close"
VOLUME_COLUMN = "Volume"
TIMEZONE = "UTC"
MIN_OBSERVATIONS = 252

#____CAPITAL AND RISK PARAMETERS____
INITIAL_CAPITAL = 100000.0
COMMISSION_RATE = 0.001
SLIPPAGE_RATE = 0.0005
MAX_POSITION_WEIGHT = 0.20
ALLOW_FRACTIONAL_SHARES = False
RISK_FREE_RATE = 0.02

ALPACA_KEY = os.getenv("ALPACA_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not ALPACA_KEY or not ALPACA_SECRET:
    raise ValueError("Alpaca API key and secret must be set in the .env file.")

if not ANTHROPIC_API_KEY:
    raise ValueError("Anthropic API key must be set in the .env file.")