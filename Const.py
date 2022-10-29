name_image = 'anime'
image = 'picture/' + name_image + '.png'

ERROR = 700
block_col = 1
block_row = 1

block_height = 8
block_width = 8
compressed_block_height = 3
compressed_block_width = 3
first_layer = block_height * block_width * 3
second_layer = compressed_block_width * compressed_block_height * 3

block_max_col = int(256 / block_width)
block_max_row = int(256 / block_height)

number_blocks = int(256 * 256 / (block_height * block_width))

alpha = 0.0007

W1 = None
W2 = None
h1 = None
h2 = None

size2 = int(block_max_row * compressed_block_height)
size1 = int(block_max_col * compressed_block_width)


def get_number_blocks():
    if 256 % block_height == 0 and 256 % block_width == 0:
        return True
    else:
        return False


out_image = [[[0 for k in range(3)] for n in range(256)] for j in range(256)]
middle_image = [[[0 for q in range(3)] for w in range(size1)] for e in range(size2)]

epoch = 0
