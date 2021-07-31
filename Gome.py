class Gome:

    def __init__(self):

        self.my_hp=1200
        self.my_power=100
        self.you_hp=1200
        self.you_power=99
        self.hh=0

    def Fill(self):
        while True:
            self.my_hp = self.my_hp - self.you_power
            self.you_hp = self.you_hp - self.my_power
            print('我的血量{}VS敌人的血量{}'.format(self.my_hp,self.you_hp))
            self.hh+=1
            print(f'回合数:{self.hh}')

            if self.my_hp<=0:
                print('我输了')
                break
            elif self.you_hp<=0:
                print('我赢了')
                break
if __name__=='__main__':
    zhangfei=Gome()
    zhangfei.Fill()
    # houyi=Gome()
    # houyi.Fill(20)