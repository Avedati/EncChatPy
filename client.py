import socket
from communication import recv_message, send_message
from diffie_hellman import client_diffie_hellman
from utils import get_aes_key

def client_main():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(("localhost", 9998))

	shared = client_diffie_hellman(client)
	aes_key = get_aes_key(shared)

	server_username = recv_message(client, aes_key)
	if server_username is None:
		return
	print(f"[{server_username}] began a chat!")
	client_username = send_message(client, aes_key, 'Please enter a username: ')
	if client_username is None:
		return
	print(f"Successfully joined the chat!")

	while True:
		message = recv_message(client, aes_key)
		if message is None:
			break
		print(f"[{server_username}] {message}")
		if send_message(client, aes_key, f'[You] ') is None:
			break

if __name__ == '__main__':
	client_main()
