def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def days_from_civil(y, m, d):
    y -= 1 if m <= 2 else 0
    era = y // 400 if y >= 0 else -((-y - 1) // 400 + 1)
    yoe = y - era * 400
    mp = m + (9 if m <= 2 else -3)
    doy = (153 * mp + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468

def parse_line(line):
    date_str, tz = line.strip().split()
    y, m, d = map(int, date_str.split("-"))
    sign = 1 if tz[3] == "+" else -1
    hh = int(tz[4:6])
    mm = int(tz[7:9])
    return y, m, d, sign * (hh * 3600 + mm * 60)

def to_utc_seconds(y, m, d, off):
    return days_from_civil(y, m, d) * 86400 - off

by, bm, bd, boff = parse_line(input())
cy, cm, cd, coff = parse_line(input())

cur = to_utc_seconds(cy, cm, cd, coff)

def bday_utc(year):
    mm, dd = bm, bd
    if mm == 2 and dd == 29 and not is_leap(year):
        dd = 28
    return to_utc_seconds(year, mm, dd, boff)

cand = bday_utc(cy)
if cand < cur:
    cand = bday_utc(cy + 1)

delta = cand - cur
print(0 if delta == 0 else (delta + 86399) // 86400)
