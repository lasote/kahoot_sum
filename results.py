import csv
import operator

import sys
from collections import defaultdict

points = {"Very important": 3, "Important": 2, "Meh": 1, "Not important": 0}


def read(filepath):
    ret = defaultdict(list)
    with open(filepath, 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in list(spamreader)[1:]:
            ret[row[1]].append(points[row[8]])
    return ret

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("pass a path")
        exit(0)
    results = read(sys.argv[1])
    sums = {question: reduce(lambda x, y: int(x) + int(y), p) for question, p in results.items()}
    sorted_x = sorted(sums.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    for title, p in sorted_x:
        print("%s: %s points" % (title, p))
