import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		print(binary)
		print("Step 1: ", binary[:4], int(binary[:4], 2))
		print("Step 1: ", binary[4:], int(binary[4:], 2))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(c, k):
	t2 = ord(k) + LOWERCASE_OFFSET
	t3 = ord(c) + LOWERCASE_OFFSET
	return ALPHABET[(t3 - t2) % len(ALPHABET)]

def b16_decode(enc):
	plain = ""
	for i in range(0, len(enc), 2):
		binary_whole = ""
		c1 = ALPHABET.index(enc[i])
		c2 = ALPHABET.index(enc[i+1])
		binary1 = "{0:04b}".format(c1)
		binary2 = "{0:04b}".format(c2)
		binary_whole += binary1
		binary_whole += binary2
		plain += chr(int(binary_whole, base=2))
	return plain

'''
#flag_enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
#key = "b"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

print(ALPHABET)



b16 = b16_encode(flag)
print("Encoded flag: " + b16)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
	print(i, c, enc)
print(enc)
'''

enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
for key in ALPHABET:
	unshifted = ""
	for i in range(0, len(enc), 2):
		unshifted += unshift(enc[i], key[0])
		unshifted += unshift(enc[i+1], key[0])
	plain = b16_decode(unshifted)
	print(plain)


