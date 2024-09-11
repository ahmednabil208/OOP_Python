

import re
from os import write


def check_email(email):
    pattern_email=r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern_email,email)


"""
send_mail (to, subject, msg, receiver_name ):

Create Email File like the next page specification (Email Composer)
"""

