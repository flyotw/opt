import itertools

def read_files_to_list(files):
    return list(itertools.chain.from_iterable(list(map((lambda file : open(file, "r").read().splitlines()), files))))