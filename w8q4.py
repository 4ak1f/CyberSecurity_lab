p = next_prime(100)  
q = next_prime(p + 1)  
n = p * q  
phi_n = (p - 1) * (q - 1)  
e = 65537  
d = inverse_mod(e, phi_n)  

message = 123  
ciphertext = power_mod(message, e, n)  
decrypted_message = power_mod(ciphertext, d, n)  

print("Public Key:", (e, n))  
print("Private Key:", (d, n))  
print("Ciphertext:", ciphertext)  
print("Decrypted Message:", decrypted_message)
