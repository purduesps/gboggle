import numpy as np
import matplotlib.pyplot as plt
import re
from string import ascii_lowercase

paths = ['./english.txt']
maxlength = 20
arrlength = maxlength+2
num_lengths = np.zeros(arrlength, dtype=np.int)
vowels = np.array([])
lengths = np.array([])
first_letters = np.zeros(26, dtype=np.int)

for n,path in enumerate(paths):
    with open(path) as file:
        for line in file:
            line = re.sub('\(.*\)|[^a-z]', '', line.strip('\n'))
            l = len(line)
            if l > 0:
                v = len(re.findall('[aeiou]',line))
                vowels = np.append(vowels, v)
                lengths = np.append(lengths, l)

                first_letters[ascii_lowercase.index(line[0])] += 1
                
                try:
                    num_lengths[len(line)] += 1
                except IndexError:
                    num_lengths[-1] += 1

    ### plot word length
    plt.figure(100*n+1, figsize=(12,5))
    plt.subplot(121)
    plt.title('word lengths')
    plt.bar(np.linspace(0,arrlength-1,arrlength), num_lengths)
    plt.subplot(122)
    plt.title('log( word lengths )')
    plt.bar(np.linspace(0,arrlength-1,arrlength), np.log10(num_lengths))

    ### plot ratio of vowels to word length
    plt.figure(100*n+2, figsize=(12,5))
    plt.subplot(121)
    plt.title('vowels vs word length')
    plt.hist2d(vowels, lengths, bins=(np.max(vowels),np.max(lengths)), cmin=1)
    plt.subplot(122)
    plt.title('vowels / word length')
    plt.hist2d(vowels / lengths, lengths, bins=(48,np.max(lengths)), cmin=1)

    ### plot first letter distribution
    plt.figure(100*n+3, figsize=(6,5))
    plt.title('first letter distribution')
    plt.bar(np.linspace(0,25,26), first_letters)

    ### relative first letter distribution
    for k,letter in enumerate(first_letters):
        print(ascii_lowercase[k], str(letter / np.sum(first_letters)))

plt.show()
