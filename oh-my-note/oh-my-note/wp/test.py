import random
import string
import time
import datetime
def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)

    return ''.join([random.choice(alphabet) for _ in range(32)])

random.seed(1610676432.8124)
a = get_random_id()
b = 1610676432.8226
post_at = datetime.datetime.fromtimestamp(b, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
random.seed(a + post_at)
c = get_random_id()
print(c)



