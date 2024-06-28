import dbm

with dbm.open("dbm1.db", "n") as db:

    db[b'one'] = b'1'
    db[b'two'] = b'2'
    db[b'three'] = b'3'
