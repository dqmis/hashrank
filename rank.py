"""
Hash ranking function.
"""

import sys
from difflib import SequenceMatcher
import os
from time import time
import random
import string
from tqdm import tqdm

random.seed(42)

def unihash(hash_name, str_):
    '''Uses built hasing executable and hashes your input.'''

    return os.popen('./{} "{}"'.format(hash_name, str_)).read()

def similar(st1, st2):
    '''Returns how similar two strings are.'''

    return SequenceMatcher(None, st1, st2).ratio()

def get_word(rn_):
    '''Returns random word with size of rn.'''

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn_))

def constitution(hash_name):
    '''Benchmarks how fast does your hash hashes Konstitucija.exe line by line.'''

    all_time = 0
    with open("./konstitucija.txt") as fp_:
        cnt = 0
        for line in fp_:
            start = time()
            unihash(hash_name, line.strip())
            all_time += (time() - start)
            cnt += 1

    print('Average hashing time of Konstitucija: {}s.'.format(round(all_time / cnt, 4)))

def letter_collision(hash_name):
    '''Benchmarks letter collision.'''
    coll_ = 0
    rn_ = 1000
    w_count = 100000
    similar_avg = 0
    all_start = time()
    for i in tqdm(range(w_count)):
        rw_ = get_word(rn_)
        st1 = ''.join(format(ord(x), 'b') for x in unihash(hash_name, rw_))
        rs_ = list(rw_)
        rs_[random.randint(0, rn_ - 2)] = ' '
        st2 = ''.join(format(ord(x), 'b') for x in unihash(hash_name, ''.join(rs_)))
        ss_ = similar(st1, st2)
        if ss_ == 1:
            coll_ += 1
        similar_avg += ss_

    print('Letter collision test took: {}s.'.format(round(time() - all_start, 4)))
    print('Letter similarity average: {}'.format(round(similar_avg / w_count, 4)))
    print('Found {} collision(s)'.format(coll_))

def word_collision(hash_name):
    '''Benchmarks word pair collision.'''
    coll_ = 0
    rn_ = 1000
    w_count = 100000
    similar_avg = 0
    all_start = time()
    for i in tqdm(range(w_count)):
        st1 = ''.join(format(ord(x), 'b') for x in unihash(hash_name, get_word(rn_)))
        st2 = ''.join(format(ord(x), 'b') for x in unihash(hash_name, get_word(rn_)))
        ss_ = similar(st1, st2)
        if ss_ == 1:
            coll_ += 1
        similar_avg += ss_

    print('Word collision test took: {}s.'.format(round(time() - all_start, 4)))
    print('Word similarity average: {}'.format(round(similar_avg / w_count, 4)))
    print('Found {} collision(s)'.format(coll_))

def main():
    '''Main function'''
    if len(sys.argv) < 2:
        print('You need to pass your hash executable\'s name!')
        return
    constitution(sys.argv[1])
    letter_collision(sys.argv[1])
    word_collision(sys.argv[1])

if __name__ == "__main__":
    main()
