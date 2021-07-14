num = int(input('輸入初始蘋果數量?')) 
mon = int(input('輸入蘋果價格?'))     
def BuyIn():  
    Add = int(input('進貨多少蘋果?')) 
    return Add                       
def SellOut():  
    Sell = int(input('賣了多少蘋果?')) 
    return Sell         
print('/--------------------------------/')
print('/  1.進貨                        /')
print('/  2.出貨                        /')
print('/  3.營業統計                    /')
print('/  4.庫存統計                    /')
print('/  5.離開系統                    /')
print('/  請選擇 : (1/2/3/4/5)          /')
print('/------------------------------- /')            
i = 0                                      
sell = []                                  
while i == 0:                             
    choose = int(input('輸入要執行的功能 1.進貨 2.出貨 3.營業統計 4.庫存統計 5.離開系統:'))  
    if choose == 1:
        Add = BuyIn()               
        num = num + Add 
        print('進貨蘋果數量:', Add)
        print('累計蘋果數量:', num)
    if choose == 2:                        
        Sell = SellOut()             
        if num >= Sell:        
            num = num - Sell  
            sell.append(Sell)         
            print('賣出蘋果數:', Sell)
            print('累計蘋果數量:', num)
            print('總共收了', Sell * mon, '塊錢')
        else:                              
            print('抱歉,庫存不足')
    if choose == 3:                        
        print('今天總共有', len(sell), '筆交易')
        print('今天的的販售紀錄:')
        for x in sell:                     
            print(x,'個')
        print('一共收了:', sum(sell) * mon, '元')  
    if choose == 4:                      
        print('剩下的蘋果:',num)
    if choose == 5:                      
        i = 1                            
        print('系統關閉')
            
        




