import os, threading

filepath = 'tmp'
path = f'{filepath}'
outpath = 'complete'

file_list = os.listdir(path)
print(file_list)

threads = []


def leap_year(year):
    return (year // 4 == 0 and year // 100 != 0) or (year // 400 == 0)


def which_day(year, month, day):
    total = 0
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index in range(month - 1):
        total += days_of_month[index]
    if month > 2 and leap_year(year):
        total += 1
    return total + day


# For Modis
def clean_data_M(f, fo):
    print(f.readline())  # Read first line
    for r in f:
        elements = r.split(',')
        dates = elements[5].split('-')
        day = which_day(int(dates[0]), int(dates[1]), int(dates[2]))
        elements[5] = day
        if elements[13] == 'D':
            elements[13] = 0
        else:
            elements[13] = 1

        del elements[7]
        del elements[7]
        # print(elements[:-1])
        res = ""
        for s in elements:
            res += str(s) + ","
        # res[:-1] = '\n'
        fo.write(res[:-1])
        # fo.write()


# For VIIRS
def clean_data(f, fo):
    print(f.readline())  # Read first line
    for r in f:
        elements = r.split(',')
        dates = elements[5].split('-')
        day = which_day(int(dates[0]), int(dates[1]), int(dates[2]))
        elements[5] = day
        if elements[13] == 'D':
            elements[13] = 0
        else:
            elements[13] = 1

        conf_lev = {'h': 0, 'l': 1, 'n':2}
        elements[9] = conf_lev[elements[9]]

        del elements[7]
        del elements[7]
        # print(elements[:-1])
        res = ""
        for s in elements:
            res += str(s) + ","
        # res[:-1] = '\n'
        fo.write(res[:-1])
        # fo.write()


for file in file_list:
    print(file)
    with open(f'{filepath}/{file}', 'r') as f:
        with open(f'{outpath}/{file}', 'w+') as fo:
            a_thread = threading.Thread(target=clean_data_M(f, fo))
            threads.append(a_thread)
    # break

for i in threads:
    i.start()
