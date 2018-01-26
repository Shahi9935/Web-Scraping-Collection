import requests,bs4
usr=input("Enter username\n");
page=1
stri=""
usrexi=1
cont=0
print("Wait...")
while True:
    usrlink="https://github.com/"+usr+"?page="+str(page)+"&tab=repositories"
    res=requests.get(usrlink);
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    if(cont==0):
        nor=soup.find("span",{"class":"Counter"}).text
        usrname=soup.find("span",{"itemprop":"name"}).text.strip()
        norstr=usrname+" has created "+nor.strip()+" repositories."
        print("Getting the names of "+nor.strip()+" repositories")
        stri=stri+norstr+"\n\n"
    div = soup.find("div", {"id": "user-repositories-list"})
    if(div==None):
        print("No such user")
        usrexi=0
        break
    for a in div.find_all('a',{"itemprop":"name codeRepository"}):
        stri=stri+a.text.strip()+"\n"
    morepages=soup.find("div",{"class":"pagination"})
    if(morepages==None):
        cont=0
    else:
        cont=1
        page=page+1
        islast=soup.find("span",{"class":"next_page disabled"})
        if(islast==None):
            cont=1
        else:
            cont=0
    if(cont==0):
        break
if(usrexi==1):
    filename=usr+"-Repositories.txt"
    f=open(filename,"w")
    f.write(stri)
    f.close()
    print("Done. Text file created")

