from operator import itemgetter

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_fname = sorted(rows, key=lambda a: a['fname'])

rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_fuid = sorted(rows, key=lambda a: a['uid'])

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
rows_by_lfname = sorted(rows, key=lambda a: (a['lname'], a['fname']))

print(rows_by_fname)
print(rows_by_uid)
print(rows_by_lfname)