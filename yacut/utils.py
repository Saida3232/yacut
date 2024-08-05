import random

from .constants import LENGTH_SHORT_LINK, OTP_CHARS


def get_unique_short_id():
    short_url = ''.join(random.choices(OTP_CHARS, k=LENGTH_SHORT_LINK))
    return short_url