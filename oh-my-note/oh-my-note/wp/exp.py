# from datetime import datetime
import time
import datetime
from dateutil.parser import parse
import random
import string


def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)

    return ''.join([random.choice(alphabet) for _ in range(32)])

print(datetime.datetime.utcnow())
a = round(time.time(), 4)
b = datetime.datetime.fromtimestamp(a, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
print(a)
print(b)
d = b.replace(' UTC','')

uncertain_datetimes = [
    # ['2020-09-22 00:00', 'n3jx'],
    ['2021-01-15 02:29', 'lj40n2p9qj9xkzy3zfzz7pucm6dmjg1u'],
    # ['2020-09-22 04:25', 'bctf'],
    # ['2020-09-22 13:37', 'vpir'],
    # ['2020-09-22 14:12', 'wanl'],
    # ['2020-09-22 20:09', '6645'],
    # ['2020-09-22 21:09', 'cfddcxulrhohtilq03qke9v0iqwddmvz'],
]

x = '2021-01-15 02:29 UTC'
for z in uncertain_datetimes:
    flag = 0
    for i in range(0, 60):
        flag = 0
        for j in range(0, 10000):

            c = parse(z[0] + ':' + str(i) + '.' + str(j))
            print(c)
            d = float(c.timestamp()) + (3600 * 8)
            print(d)
            # d = float(c.timestamp()) + 3600 * 5
            # if d > 1602852699: # 1602852697.4175
            #     print('failed!')
            #     flag = 1
            #     break
            # print(d)
            # if d == 1602850351.6681:
            #     random.seed(d)
            #     user_id = get_random_id()
            #     random.seed(user_id + x)
            #     note_id = get_random_id()
            #     print(user_id, note_id)
            #     flag = 1
            #     break
            # d = float(c.strftime("%s.%f")) + 3600 * 8
            random.seed(d)
            user_id = get_random_id()
            random.seed(user_id + x)
            note_id = get_random_id()
            # print(id_viewer)
            if note_id.startswith(z[1]):
                print('--------------------')
                print(z[0], z[1])
                print(c)
                print(d)
                # print('k is: ' + str(k))
                print('note_id: ' + note_id)
                print('user_id: ' + user_id)
                print('--------------------')
                flag = 1
                break
        if flag:
            break
        # print(c.timestamp())

# print(c)
# print(c.timestamp())
