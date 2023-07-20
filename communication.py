from aes import aes_encrypt_128, aes_decrypt_128, key_expansion, pad, unpad
import math

def send_blocks(client, key, message):
	if len(message) == 0:
		return -1
	padded = pad(message)
	expanded_keys = key_expansion(key)
	blocks = []
	for i in range(0, len(padded), 16):
		blocks.append(aes_encrypt_128(padded[i : i + 16], expanded_keys))
	n_blocks = int.to_bytes(len(blocks), length=max(1, math.ceil(math.log(len(blocks)) / math.log(256))))
	if len(n_blocks) > 16:
		print("(send_blocks) error: your message is too large, please split it up into blocks of 1,048,560 bytes at a time.")
		return -1
	client.send(pad(n_blocks))
	for block in blocks:
		client.send(block)

def recv_blocks(client, key):
	expanded_keys = key_expansion(key)
	plaintext_bytes = bytearray() 
	n_blocks = int.from_bytes(unpad(client.recv(16)))
	for i in range(n_blocks):
		ciphertext = client.recv(16)
		block = aes_decrypt_128(ciphertext, expanded_keys)
		plaintext_bytes += block
	plaintext = unpad(plaintext_bytes).decode('utf-8')
	return plaintext

def send_message(client, key, prompt):
	while True:
		message = input(prompt)
		if send_blocks(client, key, message) == -1:
			continue
		if message == 'quit()':
			return None
		break
	return message

def recv_message(client, key):
	plaintext = recv_blocks(client, key)
	if plaintext == 'quit()':
		return None
	return plaintext
