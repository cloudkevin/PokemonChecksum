import sys

with open(sys.argv[1], 'rb+') as f:
	ram = bytearray(f.read())
	checksum = 0xff
	for c in ram[0x2598:0x3523]:
		checksum -= c
	ram[0x3523]=checksum&0xff
	f.seek(0,0)
	f.write(ram)
	print('checksum {} written'.format(checksum&0xff))