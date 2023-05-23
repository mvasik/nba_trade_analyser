# needed libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import time
headers=["name","position","games played","games started","mpg","fg%","3p","3p%","ft%","trb","ast","stl","blk","tov","pts"]
#headers=["name","age","team","league","position","games played","games started","mpg","fg","fga","fg%","3p","3pa","3p%","2p","2pa","2p%","efg%","ft","fta","ft%","orb","drb","trb","ast","stl","blk","tov","pf","pts"]

header_index=[3, 4, 5, 6, 9, 10, 12, 19, 22, 23, 24, 25, 26, 28]

def getinfo(soup):
    stats=soup.find("tr",{"id":"per_game.2023"})
    statstd = stats.findAll('td')
    
    x=0
    temp_list=[]
    for j in statstd:
        if x in header_index:
           temp_list.append(statstd[x])
           
        x+=1
    
    
    statstext = [th.getText() for th in temp_list]
    statstext_replaced=[w.replace('.', '.') for w in statstext]
    
        
    k=0
    
    for i in statstext_replaced:
        if i=="":
            continue
        if i[0]==".":
            statstext_replaced[k]="0"+statstext_replaced[k]
        else:
            pass
        k+=1
    return list(statstext_replaced)



    
def output_give(p_list):
    global player_stats_list_give
    
    for player in p_list:
        aramaurl = f"https://www.basketball-reference.com/search/search.fcgi?search={parse.quote(player)}"
        html = urlopen(aramaurl)
        soup = BeautifulSoup(html, features="lxml")
            
        try:
            print(getinfo(soup))
            player_stats_list_give.append(getinfo(soup))
            
        except:
            try:
                playerlink = soup.find('div', {'class' : 'search-item'}).find("a", href=True)['href']
                playerurl = f"https://www.basketball-reference.com/{playerlink}"
                html = urlopen(playerurl)
                soup = BeautifulSoup(html, features="lxml")
                print(getinfo(soup))
                player_stats_list_give.append(getinfo(soup))
                
            except:
                print("hata")
                
def output_get(p_list):
    global player_stats_list_get
    
    for player in p_list:
        aramaurl = f"https://www.basketball-reference.com/search/search.fcgi?search={parse.quote(player)}"
        html = urlopen(aramaurl)
        soup = BeautifulSoup(html, features="lxml")
            
        try:
            print(getinfo(soup))
            player_stats_list_get.append(getinfo(soup))
            
        except:
            try:
                playerlink = soup.find('div', {'class' : 'search-item'}).find("a", href=True)['href']
                playerurl = f"https://www.basketball-reference.com/{playerlink}"
                html = urlopen(playerurl)
                soup = BeautifulSoup(html, features="lxml")
                print(getinfo(soup))
                player_stats_list_get.append(getinfo(soup))
                
            except:
                print("hata")


count=0                
for i in range(1000):                
    player_name_give="curry"
    player_list_give=player_name_give.split(",")

                

    player_name_get="lebron"
    player_list_get=player_name_get.split(",")


    #globals for output function
    player_stats_list_give=[]
    player_stats_list_get=[]

    #function to fill stats lists
    output_give(player_list_give)   
    output_get(player_list_get) 


            

    final_header=["fg%","3p","ft%","trb","ast","stl","blk","tov","pts"]
    indexes=[3,4,6,7,8,9,10,11,12,13]

    team_give_sum=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    team_get_sum=[0,0,0,0,0,0,0,0,0,0,0,0,0]



    for i in range(len(player_stats_list_give)):
        
        team_give_sum=[float(k)+float(j) for k,j in zip(team_give_sum,player_stats_list_give[i][1:])]

    for i in range(len(player_stats_list_get)):
        team_get_sum=[float(k)+float(j) for k,j in zip(team_get_sum,player_stats_list_get[i][1:])]


    #yüzdeleri ortalama almak için     
    team_give_sum[3]=team_give_sum[3]/len(player_stats_list_give)
    team_get_sum[3]=team_get_sum[3]/len(player_stats_list_get)

    team_give_sum[6]=team_give_sum[6]/len(player_stats_list_give)
    team_get_sum[6]=team_get_sum[6]/len(player_stats_list_get)


        
        
    difference_stat=[round((float(j)-float(k)),2) for k,j in zip(team_give_sum,team_get_sum)]

    final_stats={}

    print(player_stats_list_give)
    print(team_give_sum)

    for i in range(len(indexes)-1):
        final_stats[final_header[i]]=difference_stat[indexes[i]]
        
        
    def dumpclean(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if hasattr(v, '__iter__'):
                    print(k)
                    dumpclean(v)
                else:
                    print ('%s : %s' % (k, v))
        elif isinstance(obj, list):
            for v in obj:
                if hasattr(v, '__iter__'):
                    dumpclean(v)
                else:
                    print (v)
        else:
            print (obj)
        
    dumpclean(final_stats)
    count=count+1
    print(f"COUNT : {count}")
    time.sleep(60)









"""




#  numerik yapamıyorum, nokta yerine virgül vs muhabbeti zorladı 

df_give=DataFrame(player_stats_list_give)
df_get=DataFrame(player_stats_list_get)


new_header=["fg%","3p","ft%","trb","ast","stl","blk","tov","pts"]


df_difference=-(df_give.iloc[:,[4,5,7,8,9,10,11,12,13]].astype(float).sum()-df_get.iloc[:,[4,5,7,8,9,10,11,12,13]].astype(float).sum())




# ["name"1,"position"2,"games played"2,"games started"3,"mpg"4,"fg%"5,"3p"6,"3p%"7,"ft%"8,"trb"9,"ast"10,"stl"11,"blk"12,"tov"13,"pts"14]

df_final=DataFrame(df_difference)
df_final=df_final.T
df_final.columns=new_header
print(df_final.T)



"""





        
        
