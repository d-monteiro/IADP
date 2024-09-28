# Given an email address as input, print the corresponding username (the part before the @) and the domain (the part after the @).

email = input()

user, domain = email.split('@') 

print(f"Username: {user}")
print(f"Domain: {domain}")