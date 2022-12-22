
import arithClass

def encode_binary(text: str) -> str:
    return ' '.join(format(ord(x), 'b') for x in text)

def read_symbols(filename, with_probabilities=False) -> dict or list:
    with open(filename) as f:
        symbols = f.readline().split()
        if not with_probabilities:
            return symbols
        probabilities = [float(x.replace(",",".")) for x in f.readline().split()]
        return {s: p for s, p in zip(symbols, probabilities)}

probabilities = read_symbols("settings.txt", True)

AE = arithClass.ArithmeticEncoding(probabilities)

original_msg = input("Your word to encode:")

print("Original Message: {msg}".format(msg=original_msg))


# Encode the message
encoded_msg , interval_min_value, interval_max_value = AE.encode(msg=original_msg, 
                                                                          probability_table=AE.probability_table)

print("Encoded Message: {msg}".format(msg=encoded_msg))
print(len(original_msg))

def encode_binary(text: str) -> str:
    return ' '.join(format(ord(x), 'b') for x in text)

binary_code = encode_binary(str(encoded_msg))

print("The binary code is: {binary_code}".format(binary_code=binary_code))


with open("encoded.txt", "w") as file:
    file.write(binary_code + "\n" + encode_binary(str(len(original_msg))))


