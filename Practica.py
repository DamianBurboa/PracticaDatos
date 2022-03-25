import hashlib

#iniciando string de cifrar
str = "hello"
#string
encoded_str = str.encode()
#ibjetis
hash_obj_sha224 = hashlib.sha224(encoded_str) #SHA224
hash_obj_sha256 = hashlib.sha256(encoded_str) #SHA256
#Print
print("\nSHA224 Hash: ", hash_obj_sha224.hexdigest())
print("\nSHA256 Hash: ", hash_obj_sha256.hexdigest())
