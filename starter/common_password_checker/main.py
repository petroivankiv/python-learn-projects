def check_password(password: str):
    with open('starter/common_password_checker/passwords.txt', 'r') as f:
        common_pass: list[str] = f.read().splitlines()
        
    for i, p in enumerate(common_pass, start=1):
        if p == password:
            print(f'{password} X #{i}')
            return
        
    print(f'{password} - Унікальний!')
        
        
def main():
    user_password: str = input('Задайте гасло: ')
    check_password(user_password)
    
if __name__ == '__main__':
    main()