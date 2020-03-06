import calendar
import os
import sys

month_dict = dict((v.lower(),k) for k,v in enumerate(calendar.month_abbr))
del month_dict['']

def convert_line(input_data):
    if 'month' in input_data.lower():
        for month, num in month_dict.iteritems():
            index = input_data.find(month)
            if index != -1:
                input_data = input_data[:index] + str(num) + input_data[index+3:]

    return input_data

if __name__ == "__main__":
    input_file = sys.argv[1]
    input_file_split = os.path.splitext(input_file)

    output_lines = list()
    with open(input_file, "r") as f:
        for line in f:
            output_lines.append(convert_line(line))

    output_file = open(input_file_split[0] + '.out' + input_file_split[1], "w+")
    output_file.write(''.join(output_lines))
