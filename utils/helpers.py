"""Small helpers used by fixtures and tests."""

import os
from collections.abc import AsyncIterator

from dotenv import load_dotenv


def load_test_config() -> dict[str, str]:
    """Load optional local environment overrides without requiring secrets."""
    load_dotenv()
    return {
        "base_url": os.getenv(
            "BASE_URL", "https://anastasiyasg.github.io/portfolio/"
        ),
    }


async def close_safely(resource: AsyncIterator) -> None:
    """Close an async Playwright resource when it exists."""
    if resource is not None:
        await resource.close()
