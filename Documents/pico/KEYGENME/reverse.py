import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = "SCHOFIELD"
bUsername_trial = b"SCHOFIELD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

index_order = [4, 5, 3, 6, 2, 7, 1, 8]

dynamic = ''

for index in index_order:
	dynamic += hashlib.sha256(bUsername_trial).hexdigest()[index]

print(key_part_static1_trial + dynamic + key_part_static2_trial)