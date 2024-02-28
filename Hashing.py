import hashlib
#algorithme choisi pour le hashing 
h= hashlib.new ("SHA256")
correct_password = "Mon mot de passe 123"
#input

h.update(correct_password.encode())
password_hash = h.hexdigest
print(password_hash)
#le resultat de hashing 

user_input = 'Monpdp12345678'
h= hashlib.new ("SHA256")
h.update(user_input.encode())
print(h.hexdigest)
