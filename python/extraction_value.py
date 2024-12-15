import re


def get_bs_value(csv_data, regex):
    csv_data_split = re.findall(r"" + regex, csv_data)
    for i in csv_data_split:
        data = i.split("\t")
        if '"CurrentYearInstant"' in data:
            return int(data[-1].replace('"', ""))
    return None


def get_pl_value(csv_data, regex):
    csv_data_split = re.findall(r"" + regex, csv_data)

    for i in csv_data_split:
        data = i.split("\t")
        if '"CurrentYearDuration"' in data:
            return int(data[-1].replace('"', ""))
    return None
