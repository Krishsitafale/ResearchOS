"""
Central logging configuration.

Every module imports the same logger.
"""

import logging
import sys

# -------------------------------------------------------

logger = logging.getLogger("ResearchOS")

logger.setLevel(logging.INFO)

# -------------------------------------------------------

formatter = logging.Formatter(

    "%(asctime)s | %(levelname)s | %(message)s"

)

# -------------------------------------------------------

console_handler = logging.StreamHandler(sys.stdout)

console_handler.setFormatter(formatter)

# -------------------------------------------------------

logger.handlers.clear()

logger.addHandler(console_handler)

logger.propagate = False