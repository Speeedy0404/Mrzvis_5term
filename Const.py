name_image = 'forest'
image = 'picture/' + name_image + '.png'

ERROR = 0.22
block_height = 8
block_width = 4
compressed_block_height = 4
compressed_block_width = 2
alpha = 0.0007
iteration = 2000

block_col = 1
block_row = 1
block_max_col = int(256 / block_width)
block_max_row = int(256 / block_height)
first_layer = block_height * block_width * 3
second_layer = compressed_block_width * compressed_block_height * 3
number_blocks = int(256 * 256 / (block_height * block_width))

W1 = None
W2 = None
h1 = None
h2 = None

size2 = int(block_max_row * compressed_block_height)
size1 = int(block_max_col * compressed_block_width)

out_image = None
middle_image = None

epoch = 0
