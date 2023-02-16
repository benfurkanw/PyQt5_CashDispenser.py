import time

class CashDispenser:
    def __init__(self):
        pass

    def Welcome(self):
        print("Hoşgeldiniz")
        time.sleep(1)

    def Login(self):
        print("Merhaba")

    def Register(self):
        self.Name = input("Adınızı giriniz: ")
        self.Password = input("Şifrenizi Giriniz: ")
        self.email = input("Email Adresinizi Giriniz: ")
        time.sleep(1)
        self.Completed = input("Geri gitmek için '0' Tuşuna Eğer bilgilernizi yanlış girdiyseniz Herhangi bir tuşa basınız: ")

    def While(self):
        while True:
            self.answer = input("Yapmak istediğiniz işlemi yazınız\nLogin - > 1\nRegister - > 2\nSeçimizi: ")
            if self.answer == "1":
                while True:
                    self.Login()
            
            if self.answer == "2":
                while True:
                    self.Register()

                    if self.Completed == "0":

                        print("Bilgileniriz Kaydedildi")
                        break



        


def Work():
    Work = CashDispenser()
    Work.Welcome()
    Work.While()


Work()





