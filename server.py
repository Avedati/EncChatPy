# Forked from https://www.youtube.com/watch?v=D_PfV_IcUdA
# And https://www.youtube.com/watch?v=Ar94t2XhKzM
import socket
from communication import recv_message, send_message
from diffie_hellman import server_diffie_hellman
from utils import get_aes_key

def server_main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("localhost", 9998))
	server.listen()
	client, addr = server.accept()

	shared = server_diffie_hellman(client)
	aes_key = get_aes_key(shared)

	server_username = send_message(client, aes_key, 'Please enter a username: ')
	if server_username is None:
		return
	print("Successfully began a chat!")
	client_username = recv_message(client, aes_key)
	if client_username is None:
		return
	print(f"[{client_username}] joined the chat!")

	while True:
		if send_message(client, aes_key, '[You] ') is None:
			break
		message = recv_message(client, aes_key)
		if message is None:
			break
		print(f"[{client_username}] {message}")

if __name__ == '__main__':
	server_main()
