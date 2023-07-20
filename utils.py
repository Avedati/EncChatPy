import hashlib
import math
import random

def naive_is_prime(n):
	if n < 2:
		return False
	for i in range(2, n // 2 + 1):
		if n % i == 0:
			return False
	return True

def naive_generate_prime(min_value, max_value):
	prime = random.randint(min_value, max_value)
	while not naive_is_prime(prime):
		prime = random.randint(min_value, max_value)
	return prime

# https://medium.com/@ntnprdhmm/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test
# Tested with https://www.numberempire.com/primenumbers.php
# TODO: write a more comprehensive test for this function
def is_miller_rabin_prime(n, k = 128):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n <= 1:
		return False
	s = 0
	r = n - 1
	while r & 1 == 0:
		s += 1
		r //= 2
	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, r, n)
		for __ in range(s):
			y = pow(x, 2, n)
			if y == 1 and x != 1 and x != n - 1:
				return False
			x = y
		if y != 1:
			return False
	return True

def generate_prime_candidate(length):
	candidate = random.getrandbits(length)
	candidate |= (1 << (length - 1)) | 1
	return candidate

def generate_prime(length=2048):
	candidate = generate_prime_candidate(length)
	while not is_miller_rabin_prime(candidate):
		candidate = generate_prime_candidate(length)
	return candidate

def get_aes_key(shared):
	shared_bytes = int.to_bytes(shared, length=math.ceil(math.log(shared) / math.log(256)))
	aes_key = bytearray(hashlib.sha256(shared_bytes).digest())
	return aes_key[:16]
