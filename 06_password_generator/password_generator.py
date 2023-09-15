import string
import secrets

def has_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        
    return False

def has_symbol(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> bool:
    combination: str = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
        
    if uppercase:
        combination += string.ascii_uppercase
        
    new_password = ''
    
    for _ in range(length):
        new_password += combination[secrets.randbelow(len(combination))]
        
    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass = generate_password(length=10, symbols=True, uppercase=True)
        spec: str = f'U: {has_upper(new_pass)}, S: {has_symbol(new_pass)}'
        print(f'{i} -> {new_pass} ({spec})')