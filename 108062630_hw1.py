
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.blockchain.com/eth/address/"

fi = open('input_hw1.txt','r')

fo = open('108062630_hw1_output.txt','w+')


def write_file(atr,data,date,reciver,amount,nextone):
    
    for i in range(1,7):
        x = atr[i].text + ': ' + data[i].text
        
        fo.writelines([x+'\n'])
        
    if nextone:    
        fo.writelines(['Date: ' + date + '\n'   ,   'To: ' + reciver + '\n'   ,    'Amount: ' + amount + '\n' ])
    fo.writelines(['--------------------------------------------------------------------------\n'])



def craw(adr):
    

    date=''
    reciver=''
    amount=''
    nextone = False
    
    html = urlopen(adr).read()
    soup = BeautifulSoup(html,"html.parser")
    
    
    #attribute
    atr = soup.find('div','hnfgic-0 blXlQu').find_all('span','sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh sc-1n72lkw-0 bKaZjn')
    
    #data
    data = soup.find('div','hnfgic-0 blXlQu').find_all('span','sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk')
    
    #transaction
    
    tx = soup.find('div','sc-1d6wz2a-0 gqRKsm').find_all('div','sc-1fp9csv-0 gkLWFf',direction='vertical')
            
    for t in reversed(tx):
        if(t.find('span','sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd')):
            
            nextone = True
            
            date = t.find('span','sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk').text
            
            reciver = t.find_all('a','sc-1r996ns-0 dEMBMB sc-1tbyx6t-1 gzmhhS iklhnl-0 dVkJbV')[2].text
            
            amount = t.find('span', 'sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk sc-85fclk-0 gskKpd').text
            
            break
            
            
    write_file(atr,data,date,reciver,amount,nextone)
    
    return nextone,reciver
        




if __name__ == '__main__':

    adr=fi.readline().strip('\n')
    
    while(adr):        
        
        nextone =True
        dest = adr
        path = ""
        i=0
        
        while(i<4 and nextone):
            
            
            path = path + dest + ' -> '
            
            dest_url = url + dest + '?view=standard'
            

            
            nextone,dest = craw(dest_url)
            

            
            i=i+1

        path = path[0:-4]
        
        fo.writelines([path + '\n'])
        fo.writelines(['--------------------------------------------------------------------------\n'])
            
        adr=fi.readline().strip('\n')
        
    fi.close()
    fo.close()






