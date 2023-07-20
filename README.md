# EncChatPy

EncChatPy is a simple chat via socket that is encrypted with 128-bit AES. To generate an AES key, the program uses Diffie-Hellman key exchange with.
To generate the required 2048 bit random primes, the standard Python 3.11.4 random library is used in conjunction with the Miller-Rabin primality test.
Each of these three algorithms is written in Python 3 using only standard libraries. All of the sources used to write these algorithms are linked
in the comments proceeding them.

## Testing
I have written a small test suite for the AES algorithm and the relevant padding functions. The following commands runs the test suite:
```bash
python3 aes_test.py
```

To run the server and client themselves, type the following commands in separate terminals (start the server first):
```bash
python3 server.py
```

```bash
python3 client.py
```

## Disclaimers

Currently, this program functions more as a proof of concept of my implementation of AES, Diffie-Hellman, Miller-Rabin, and various algorithms.
Due to the fact that "localhost" is hardcoded in the `server.py` and `client.py` files, the program cannot be used to create a chat between two separate computers.
In the future, I plan on implementing this feature.

Although the relevant functions in this program should be secure in theory, I have only done minimal testing, and thus user discretion is advised.
There are many potential security flaws in this chat, including but not limited to any security flaws in Python 3 itself or my usage of it.
