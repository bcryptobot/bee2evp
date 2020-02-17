# *****************************************************************************
# \file belt.py
# \project bee2evp [EVP-interfaces over bee2 / engine of OpenSSL]
# \brief A python wrapper over belt methods
# \created 2019.12.09
# \version 2020.02.17
# \license This program is released under the GNU General Public License 
# version 3 with the additional exemption that compiling, linking, 
# and/or using OpenSSL is allowed. See Copyright Notices in bee2evp/info.h.
# *****************************************************************************

from openssl import openssl
from settings import *

def beltBlockEncr(block, key):
	assert len(block) * 8 == 128

	plain = b64_encoder(block)[0].decode()
	key = hex_encoder(key)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -e -belt-ecb{} -nosalt -nopad -e -K {}'.format(key_bitlen, key)
	retcode, block, er__ = openssl(cmd, prefix)
	return block


def beltBlockDecr(block, key):
	assert len(block) * 8 == 128

	plain = b64_encoder(block)[0].decode()
	key = hex_encoder(key)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -d -belt-ecb{} -nosalt -nopad -K {}'.format(key_bitlen, key)
	retcode, block, er__ = openssl(cmd, prefix)
	return block

def beltECBEncr(src, key):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -e -belt-ecb{} -nosalt -nopad -K {}'.format(key_bitlen, key)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltECBDecr(src, key):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -d -belt-ecb{} -nosalt -nopad -K {}'.format(key_bitlen, key)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest	

def beltCBCEncr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -e -belt-cbc{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltCBCDecr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -d -belt-cbc{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltCFBEncr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -e -belt-cfb{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltCFBDecr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -d -belt-cfb{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltCTREncr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -e -belt-ctr{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltCTRDecr(src, key, iv):
	assert (len(src) * 8) % 128 == 0

	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	iv = hex_encoder(iv)[0].decode()
	key_bitlen = len(key) * 4

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'enc -d -belt-ctr{} -nosalt -nopad -K {} -iv {}'.format(key_bitlen, key, iv)
	retcode, dest, er__ = openssl(cmd, prefix)
	return dest

def beltMAC(src, key):
	plain = b64_encoder(src)[0].decode()
	key = hex_encoder(key)[0].decode()
	key_bitlen = len(key)*4
	
	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'dgst -mac belt-mac{} -macopt hexkey:{}'.format(256, key)
	retcode, out, er__ = openssl(cmd, prefix)
	mac = out.decode().split(' ')[1][:-1]
	return bytes(hex_decoder(mac)[0])
	
def beltHash(src):
	plain = b64_encoder(src)[0].decode()

	prefix = 'echo ' + plain[:-1] + ' | python -m base64 -d |'
	cmd = 'dgst -belt-hash'.format()
	retcode, out, er__ = openssl(cmd, prefix)
	hash_ = out.decode().split(' ')[1][:-1]
	return bytes(hex_decoder(hash_)[0])



