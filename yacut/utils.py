import random

from .constants import LENGTH_SHORT_LINK, OTP_CHARS


def get_unique_short_id():
    return ''.join(random.choices(OTP_CHARS, k=LENGTH_SHORT_LINK))