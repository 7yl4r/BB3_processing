
from datetime import timedelta
from datetime import datetime
import os

from parse import parse

line_fmt = (
    '{:2d}/{:2d}/{:2d} {:2d}:{:2d}:{:2d} '
    '{:3d} {:4d} {:3d} {:4d} {:3d} {:4d} {:4d}'
)
dt_fmt = "%m/%d/%y  %H:%M:%S"
dt_prev = ""
# will edit out when wanting to put site in at same time
site = 0
file_name = ''
os.mkdir('BB3')
# TODO: need to have a way to create a file with incremental name with
#   data from the lines where true

# sample_file_name = input('Whats the file name?')  # change when doing runs
f = open('new_file.raw', "r")  # can just edit this before running anything
# use readline() to read the first line
line_of_text = f.readline()
while line_of_text:
        parsed_line = parse(line_fmt, line_of_text)
        time_of_sample = "{}/{}/{} {}:{}:{}".format(
            parsed_line[0], parsed_line[1], parsed_line[2],
            parsed_line[3], parsed_line[4], parsed_line[5s]
        )
        # print(liness)
        try:
            dt = datetime.strptime(time_of_sample, dt_fmt)
        except Exception:
            # print(line)
            # newfile = open('files_with_errors.txt', "a")
            # newfile.write(line)
            line_of_text = f.readline()
            continue
        if dt_prev == "":
            dt_prev = dt - timedelta(seconds=1)
        dt_new = dt

        if dt_new - dt_prev < timedelta(minutes=5):
            dt_prev = dt_new  # this makes the prev new time set as prev time
            if file_name == "":
                dt_prev = dt_new
                i = dt_new.strftime("%d_%m_%yT%H%M%S")
                # this is so can look up timestamp on spreadsheet
                print('Old time: ' + str(dt_new))
                # site = input("What is the site ID?")  # edit in later
                file_name = 'MBON_{}_site_{}.txt'.format(i, site)
                # print(file_name)  # probably dont need to see this
                newfile = open('BB3/' + file_name, "a")
                newfile.write(line_of_text)
            else:
                newfile = open('BB3/' + file_name, "a")
                newfile.write(line_of_text)
                # use readline() to read next line
        else:
            dt_prev = dt_new
            i = dt_new.strftime("%d_%m_%yT%H%M%S")
            print('Old time: ' + str(dt_new))
            # site = input("What is the site ID?")
            site = site + 1
            file_name = 'MBON_{}_site_{}.txt'.format(i, site)
            # print(file_name)  # probably dont need to see this
            newfile = open('BB3/' + file_name, "a")
            newfile.write(line_of_text)
        line_of_text = f.readline()
f.close()
