#! /usr/bin/env python
import argparse
import json
from operator import itemgetter

def bw_restore(I, L):
    n = len(L)
    X = sorted([(i, x) for i, x in enumerate(L)], key=itemgetter(1))

    T = [None for i in range(n)]
    for i, y in enumerate(X):
        j, _ = y
        T[j] = i

    Tx = [I]
    for i in range(1, n):
        Tx.append(T[Tx[i-1]])

    S = [L[i] for i in Tx]
    S.reverse()
    return ''.join(S)

def lzw_decode(str_to_decode_binary):
    with open("alphabet.txt", "r") as file:
        dictionary_reversed = json.loads(file.read())

    dictionary = {key: value for value, key in dictionary_reversed.items()}

    list_to_decode = list(map(lambda x: int(x, 2), str_to_decode_binary))
    dict_size = len(dictionary)

    result = ""
    w = dictionary[list_to_decode.pop(0)]
    result += w
    for k in list_to_decode:
        if k in dictionary:
            entry = dictionary[k]
        else:
            entry = w + w[0]
        result += entry

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Decode LZW +  Burrows Wheeler ')
    parser.add_argument('STRING', type=str, help='Decode this string.')
    parser.add_argument('NUMBER', type=int, help='Original strung number.')
    args = parser.parse_args()

    mylist = (args.STRING).split(" ")

    decompressed = lzw_decode(mylist)
    decoded = bw_restore(args.NUMBER ,decompressed)
    print(decoded)

