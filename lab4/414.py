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
    days = days_from_civil(y, m, d)

    sign = 1 if tz[3] == "+" else -1
    hh = int(tz[4:6])
    mm = int(tz[7:9])
    offset_sec = sign * (hh * 3600 + mm * 60)

    utc_seconds = days * 86400 - offset_sec
    return utc_seconds

t1 = parse_line(input())
t2 = parse_line(input())

diff_days = abs(t1 - t2) // 86400
print(diff_days)
