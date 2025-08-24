import logging
import logging.config
from pathlib import Path
from .settings import Settings

from .logger_config import get_logger

from ._mode import mode

PROJECT_SETTINGS = Settings()


_logger_config = get_logger(PROJECT_SETTINGS.app.logger_level)
logging.config.dictConfig(_logger_config)

logger = logging.getLogger(__name__)


ROOT_PATH = Path(__file__).parent.parent.parent

logger.info(f"[APP] Path: {ROOT_PATH}")
logger.info(f"[APP] Develop: {mode(PROJECT_SETTINGS.app.develop)}")
