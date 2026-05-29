class LoginTizimi:
    def __init__(self):
        self.foydalanuvchilar = {
            "admin": "password",
            "user": "password"
        }

    def login(self, username, password):
        if username in self.foydalanuvchilar and self.foydalanuvchilar[username] == password:
            return True
        return False

login_tizimi = LoginTizimi()

while True:
    print("Login tizimi")
    print("1. Kirish")
    print("2. Chiqish")
    print("3. Foydalanuvchi qo'shish")
    print("4. Foydalanuvchi o'chirish")
    print("5. Foydalanuvchilar ro'yxati")
    print("6. Chiqish")
    print("7. Dasturni to'xtatish")
    
    tanlov = input("Tanlovni tanlang: ")
    
    if tanlov == "1":
        username = input("Foydalanuvchi nomi: ")
        password = input("Parol: ")
        if login_tizimi.login(username, password):
            print("Tizimga muvaffaqiyatli kirildi!")
        else:
            print("Foydalanuvchi nomi yoki parol noto'g'ri!")
            
    elif tanlov == "2":
        print("Tizimdan chiqish!")
        
    elif tanlov == "3":
        username = input("Foydalanuvchi nomi: ")
        password = input("Parol: ")
        login_tizimi.foydalanuvchilar[username] = password
        print("Foydalanuvchi qo'shildi!")
        
    elif tanlov == "4":
        username = input("Foydalanuvchi nomi: ")
        if username in login_tizimi.foydalanuvchilar:
            del login_tizimi.foydalanuvchilar[username]
            print("Foydalanuvchi o'chirildi!")
        else:
            print("Foydalanuvchi topilmadi!")
            
    elif tanlov == "5":
        for username, password in login_tizimi.foydalanuvchilar.items():
            print(f"Foydalanuvchi nomi: {username}, Parol: {password}")
            
    elif tanlov == "6":
        print("Tizimdan chiqish!")
        
    elif tanlov == "7":
        print("Dastur to'xtatildi!")
        break
        
    else:
        print("Notog'ri tanlov!")
