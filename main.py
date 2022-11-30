from threading import Thread, Lock

class StingySpendy:
    #Qeusta classe conente predere la variabile comunque e farci le operazioni sfruttando il multi thread
    money = 100
    #questa varibaile constente di sicronizzare. Questo consentirà di bloccare e sbloccare le risorse condivise.
    mutex = Lock()

    def stingy(self):
        """questa funzione consente di aggiungere sul conto (money) dei soldi"""
        for i in range(10000):
            self.mutex.acquire() #questo metodo consente di bloccare la memoria codivisa a questo thread
            self.money += 10
            self.mutex.release() #questo metodo consente di sbloccare la memoria condivisa dopo aver fatto le operazioni sul conto
        print("Stingy done")

    def spendy(self):
        """questo metodo consente di togliere sul conto (money) dei soldi"""
        for i in range(10000):
            self.mutex.acquire() #questo metodo consente di bloccare la mmeoria codivisa a questo thread per essere utilizzata e modificata solo da quel thread
            self.money -= 10
            self.mutex.release()#questo metodo consente di sbloccare la memoria condivisa dopo aver fatto le operazioni sul conto
        print("Stingy done")


if __name__ == '__main__':
    ss = StingySpendy()
    #creo il thread
    threadstingy = Thread(target=ss.stingy, args=())
    threadspendy = Thread(target=ss.spendy, args=())
    #mando i thread in esecuzione
    threadstingy.start()
    threadspendy.start()
    #questo consente di astettare che i thread terminano. (Nel caso in cui un thread si blocchi attendera 100 secondi, dopo di che me lo arresterà
    threadstingy.join(100)
    threadspendy.join(100)
    print(ss.money)
