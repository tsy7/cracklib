import cracklib

hashes = [
    "5f4dcc3b5aa765d61d8327deb882cf99", # MD5 password
    "58acb7acccce58ffa8b953b12b5a7702bd42dae441c1ad85057fa70b", # SHA224 admin
    "c90023380fc1d5721a5e20d230077a13cd3c0f9c2f407fa7bde17abecac0301dd95baf3fe5784e833a185218763ac549", # SHA3_384 glitch
]

for Hash in hashes:
    app = cracklib.Cracker("glitch")
    if app.crackHash(Hash):
        print("Done : ", Hash)
    else:
        print("Error : ", Hash)