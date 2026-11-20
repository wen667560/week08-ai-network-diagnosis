import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)


LOG_FILE = LOG_DIR / "network.log"


logging.basicConfig(
    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[
        logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        ),

        logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)