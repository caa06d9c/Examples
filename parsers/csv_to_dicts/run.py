import json
import contextlib
import csv

if __name__ == '__main__':

    res = dict()
    with contextlib.closing(open('file.csv', 'r')) as csv_file:
        reader_orig = csv.reader(csv_file, delimiter=';')
        for el in reader_orig:
            local_id = el[0]
            res[local_id] = dict()
            res[local_id]['url'] = el[1]
            res[local_id]['tab'] = el[2]

    print(json.dumps(res))
