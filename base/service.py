from datetime import date
def str_to_date(a):
    y, m, d = a.split('-')
    return date(int(y), int(m), int(d))