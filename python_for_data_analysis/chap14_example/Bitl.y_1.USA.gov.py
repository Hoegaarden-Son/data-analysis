# data:  http://github.com/wesm/pydata-book
import collections
import json
import pandas as pd
import seaborn as sns


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def top_counts(data_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in data_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


def get_timezone():
    path = './../datasets/bitly_usagov/example.txt'
    # open(path).readline()
    records = [json.loads(line) for line in open(path)]

    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print(time_zones[:10])

    # method 1. by using dict
    counts = get_counts(time_zones)
    print(len(time_zones))
    print(counts['America/New_York'])
    print(counts[''])
    print(len(counts.keys()))
    print(top_counts(counts, n=3))

    # method 2. counter
    counts = collections.Counter(time_zones)
    print(counts.most_common(5))


def get_timezone_by_pandas():
    path = './../datasets/bitly_usagov/example.txt'
    records = [json.loads(line) for line in open(path)]
    df = pd.DataFrame(records)
    # df.info()
    # print(df['tz'][:10])

    tz_counts = df['tz'].value_counts()
    print(tz_counts[:10])

    clean_tz = df['tz'].fillna('N/A')
    clean_tz[clean_tz == ''] = '_'
    tz_counts = clean_tz.value_counts()
    print(tz_counts[:10])

    subset = tz_counts[:10]
    sns.barplot(y=subset.index, x=subset.values)








# get_timezone()
get_timezone_by_pandas()
