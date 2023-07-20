from aes import aes_decrypt_128, aes_encrypt_128, key_expansion, naive_pad, naive_unpad, pad, unpad

# Test from https://www.youtube.com/watch?v=4pmR49izUL0&t=1416s
def test_encryption():
	message = 'This is a message we will encrypt with AES!'
	padded = naive_pad(message)
	key = bytearray(list(range(1, 17)))
	expanded_keys = key_expansion(key)
	blocks = []
	for i in range(0, len(padded), 16):
		blocks.append(aes_encrypt_128(padded[i : i + 16], expanded_keys))
	encrypted = []
	for block in blocks:
		encrypted += [x for x in block]

	correct = bytearray(b'\xb6\x4b\x27\xbb\x16\x15\xa6\xf5\x32\x18\x6c\xc5\xfa\x94\xb5\x5e\x5c\x54\xea\x1b\xdf\x97\x1e\x3d\xe3\x1b\xfc\x02\x75\x22\x76\x52\xd5\x7b\xd5\x42\xba\x0f\x68\x50\xcd\xfd\x59\xb8\xeb\x0e\x83\xd1')
	idx = 0
	for i, j in zip(encrypted, correct):
		if i != j:
			print(f"test_encryption: mismatch (index = {idx}): expected {hex(j)}, got {hex(i)}")
			return
		idx += 1

	print("test_encryption passed!")

def test_padding_simple():
	message = bytearray(range(14))
	padded = pad(message)
	if len(padded) != 16:
		print(f"test_padding_simple: expected len(padded) to be 16, got {len(padded)}")
		return
	for i in [14, 15]:
		if padded[i] != 2:
			print(f"test_padding_simple: expected padded[{i}] to be 2, got {padded[i]}")
			return
	print("test_padding_simple passed!")

def test_padding_complex_1():
	message = bytearray(range(27))
	padded = pad(message)
	if len(padded) != 32:
		print(f"test_padding_complex_1: expected len(padded) to be 32, got {len(padded)}")
		return
	for i in range(27, 32):
		if padded[i] != 5:
			print(f"test_padding_complex_1: expected padded[{i}] to be 5, got {padded[i]}")
			return
	print("test_padding_complex_1 passed!")

def test_padding_complex_2():
	message = bytearray(range(48))
	padded = pad(message)
	if len(padded) != 64:
		print(f"test_padding_complex_2: expected len(padded) to be 64, got {len(padded)}")
		return
	for i in range(48, 64):
		if padded[i] != 0:
			print(f"test_padding_complex_2: expected padded[{i}] to be 0, got {padded[i]}")
			return
	print("test_padding_complex_2 passed!")

def test_pad_unpad():
	message = bytearray(range(30))
	padded = pad(message)
	unpadded = unpad(message)
	if unpadded != message:
		print(f"test_pad_unpad: mismatch between original message and unpadded result, {message} and {unpadded} respectively")
		return
	print("test_pad_unpad passed!")

def test_naive_pad_unpad():
	message = bytearray(range(30))
	padded = naive_pad(message)
	unpadded = naive_unpad(message)
	if unpadded != message:
		print(f"test_naive_pad_unpad: mismatch between original message and unpadded result, {message} and {unpadded} respectively")
		return
	print("test_naive_pad_unpad passed!")

def test_encrypt_decrypt():
	message = bytearray(range(12))
	key = bytearray([x * 2 for x in range(16)])
	expanded_keys = key_expansion(key)
	padded = pad(message)
	encrypted = aes_encrypt_128(padded, expanded_keys)
	decrypted = aes_decrypt_128(encrypted, expanded_keys)
	unpadded = unpad(decrypted)
	if unpadded != message:
		print(f"test_encrypt_decrypt: mismatch between original message and decrypted result, {message} and {unpadded} respectively")
		return
	print("test_encrypt_decrypt passed!")
	
if __name__ == '__main__':
	test_encryption()
	test_padding_simple()
	test_padding_complex_1()
	test_padding_complex_2()
	test_pad_unpad()
	test_naive_pad_unpad()
	test_encrypt_decrypt()
