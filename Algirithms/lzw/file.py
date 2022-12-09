import json
from operator import itemgetter


def lzw_decode(str_to_decode_binary, A):
    
    # Переводим в десятичную систему
    list_to_decode = list(map(lambda x: int(x, 2), str_to_decode_binary))

    result = ""
    previous_word = A[list_to_decode.pop(0)]
    result += previous_word
    for k in list_to_decode:
        if k in A:
            word = A[k]
        else:
            word = previous_word + previous_word[0]
        result += word

        A[len(A)] = previous_word + word[0]

        previous_word = word
    return result


def bw_restore(I, L):
    n = len(L)
    X = sorted([(i, x) for i, x in enumerate(L)], key=itemgetter(1))

    T = [None for i in range(n)]
    for i, y in enumerate(X):
        j = y[0]
        T[j] = i

    Tx = [I]
    for i in range(1, n):
        Tx.append(T[Tx[i - 1]])

    S = [L[i] for i in Tx]
    S.reverse()
    return ''.join(S)


def from_file():
    A = {}
    
    words = ['00000000', '00000001', '00000010', '00000011', '00000110', '00000000', '00000110', '00000101', '00000000']
    
    with open("lzw.txt", "r") as file:
        text = file.readlines()
        
        for i in range(len(text[0].split())):
            A[int(text[1].split()[i])] = text[0].split()[i]
    
    lzw = lzw_decode(words, A)
    print(lzw)

    print(bw_restore(1, lzw))

def main():
    while True:
        pick = input("1 read from file \n2 read from console\n")
        if pick == '1':
            from_file()
        

if __name__ == '__main__':
    main()
