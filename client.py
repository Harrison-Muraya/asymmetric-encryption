import rsa
import os

if os.path.isfile("private.pem" and "public.pem"):

    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

else:

    public_key, private_key = rsa.newkeys(1024)

    with open("public.pem","wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem","wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

"""
msg = "great it have been good, rsa is making me mad, actually i like it a lot so far. this is great "

encrypted_msg = rsa.encrypt(msg.encode(),public_key)

with open("encrypted.harr", "wb") as f:
    f.write(encrypted_msg)

"""

cipher = open("encrypted.harr", "rb").read()

crear_msg = rsa.decrypt(cipher,private_key)

print(crear_msg.decode())
