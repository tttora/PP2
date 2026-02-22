def days_from_civil(y, m, d):
    y -= 1 if m <= 2 else 0
    era = y // 400 if y >= 0 else -((-y - 1) // 400 + 1)
    yoe = y - era * 400
    mp = m + (9 if m <= 2 else -3)
    doy = (153 * mp + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468

def parse_line(line):
    date_str, time_str, tz = line.strip().split()
    y, m, d = map(int, date_str.split("-"))
    hh, mm, ss = map(int, time_str.split(":"))
    sign = 1 if tz[3] == "+" else -1
    th = int(tz[4:6])
    tm = int(tz[7:9])
    off = sign * (th * 3600 + tm * 60)
    return y, m, d, hh, mm, ss, off

def to_utc_seconds(y, m, d, hh, mm, ss, off):
    return days_from_civil(y, m, d) * 86400 + hh * 3600 + mm * 60 + ss - off

s = parse_line(input())
e = parse_line(input())

start_utc = to_utc_seconds(*s)
end_utc = to_utc_seconds(*e)

print(end_utc - start_utc)
