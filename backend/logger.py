# AccidentDetectionApp/backend/logger.py

import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

if __name__ == "__main__":
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Logger configured successfully.")
