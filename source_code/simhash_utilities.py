import gmpy
from simhash import Simhash, SimhashIndex

def myhamdist(a, b , **oo):
  return hamdist(int(a.item(0)),int(b.item(0)))

def hamdist(x, y):
  return gmpy.hamdist(x, y)/64.0  
  
def compute_simhash_from_file(text_file):
        shakes = open(text_file, 'r')
        text = shakes.read()
        if len(text)==0:
            return 0
        words = text.decode('utf-8', errors='ignore').split()
        words.sort()
        return Simhash(" ".join(words)).value

def compute_simhash(words):
        words.sort()
        return Simhash(" ".join(words)).value

def remove_near_duplicate(collection, base_dir):
    reduced_collection = []

    with open("{}/timemap_removednearduplicates.txt".format(base_dir), 'w') as f:
        with open("{}/timemap_simhash_scores.txt".format(base_dir), 'w') as g:

            for uri_id in collection:
                timemap = collection[uri_id]
                reduced_timemap = remove_near_duplicate_tm(timemap, uri_id, g)
                for m in reduced_timemap:
                    f.write("{}\t{}\t{}\t{}\n".format(m[0], m[1], m[2], m[3]))
                    reduced_collection.append(m)

    return reduced_collection

def remove_near_duplicate_tm(timemap, uri_id, simhash_file):
    new_timemap = []
    last_simhash = 0

    for idx, val in enumerate(timemap):
        if idx == 0:
            new_timemap.append(val)
            last_simhash = val[2]
            continue
        (dt, mem_uri, simhash_value, damage) = val

        simhash_file.write("{}\t{}\t{}\t{}\n".format(dt, mem_uri, simhash_value, damage))

        if hamdist(simhash_value, last_simhash) > 0.2:
            last_simhash = simhash_value
            new_timemap.append((dt, mem_uri, simhash_value, damage))

    return new_timemap
