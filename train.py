import torch


def main():
    # read it in to inspect it
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    print("length of dataset in characters: ", len(text))

    # here are all the unique characters that occur in this text
    chars = sorted(list(set(text)))

    vocab_size = len(chars)
    print(''.join(chars))
    print(vocab_size)

    #create a mapping from characters to integers
    stoi = { ch:i for i,ch in enumerate(chars) }
    itos = { i:ch for i,ch in enumerate(chars) }

    encode = lambda s: [stoi[c] for c in s] #encoder: take a string, output a list of integers
    decode = lambda l: ''.join([itos[i] for i in l]) #decoder: take a list of integers, output a string

    encoded_message = encode("You mama is a guy")
    decoded_message = decode(encoded_message)

    print(f'Encoded message: {encoded_message}'
          f'\nDecoded message: {decoded_message}')
    
if __name__ == "__main__":
    main()