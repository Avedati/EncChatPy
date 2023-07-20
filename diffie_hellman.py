import random
from utils import generate_prime

def server_diffie_hellman(client):
	# Diffie Hellman Key Exchange: Part 1
	g = generate_prime()
	client.send(str(g).encode('utf-8'))

	p = int(client.recv(2048).decode('utf-8'))
	# https://crypto.stackexchange.com/questions/1975/what-should-be-the-size-of-a-diffie-hellman-private-key
	a = random.getrandbits(256)
	client.send(str(pow(g, a, p)).encode('utf-8'))

	B = int(client.recv(2048).decode('utf-8'))
	shared = pow(B, a, p)

	return shared

def client_diffie_hellman(client):
	# Diffie Hellman Key Exchange: Part 2
	g = int(client.recv(2048).decode('utf-8'))
	p = generate_prime()
	client.send(str(p).encode('utf-8'))

	b = random.getrandbits(256)
	A = int(client.recv(2048).decode('utf-8'))
	client.send(str(pow(g, b, p)).encode('utf-8'))
	shared = pow(A, b, p)

	return shared
