"""Runtime configuration loaded from environment variables."""

import os


BASE_URL = os.getenv("BASE_URL", "https://anastasiyasg.github.io/portfolio/")
HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"
DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "10000"))
