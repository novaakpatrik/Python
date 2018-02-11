import re
from collections import Counter
from math import ceil

f = open('scorelib.txt', 'r')

composers = Counter()
centuries = Counter()
c_minor_count = 0

for line in f:
    re_composer = re.compile(r"Composer: ([\w, ]+)")
    matched_composer = re_composer.match(line)

    re_century = re.compile(r"Composition Year: .*(\d{4})")
    matched_century = re_century.match(line)

    # how many in the key of c minor?
    if 'c minor' in line:
        c_minor_count += 1

    # how many pieces by each composer?
    if matched_composer:
        composer_name = matched_composer.group(1).replace(',', '').strip()
        composers[composer_name] += 1

    # how many pieces composed in a given century?
    if matched_century:
        century = ceil(int(matched_century.group(1).strip())/100)
        centuries[century] += 1

print('Top 10 composers by number of pieces:')
for composer, count in composers.most_common(10):
    print('{0} \t {1}'.format(count, composer))

print('\n')
print('Number of pieces per century:')
for century, count in centuries.most_common():
    print('{0}th century: {1}'.format(century, count))

print('\n')
print('Number of pieces in c minor: {}'.format(c_minor_count))
