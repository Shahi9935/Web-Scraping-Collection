import requests,bs4
print("Wait...It will take few minutes")
link="https://summerofcode.withgoogle.com/archive/2017/organizations/"
res=requests.get(link)
soup=bs4.BeautifulSoup(res.text,'html.parser')
ul=soup.find("ul",{"class":"organization-list-container no-style-list"})
z=ul.find_all("li",{"class":"organization-card__container"})
stri="GSOC-2017 Organization with required skills\n\n"
for li in z:
    alink="https://summerofcode.withgoogle.com"+li.find('a')['href']
    stri=stri+li.text.strip()+"\n  "
    rese=requests.get(alink)
    soupe=bs4.BeautifulSoup(rese.text,'html.parser')
    ule=soupe.find("ul",{"class":"org__tag-container"})
    for lie in ule.find_all('li',{'class':'organization__tag organization__tag--technology'}):
        stri=stri+lie.text.strip()+"\n  "
    stri=stri+"\n\n"
fname="GSOC2017.txt"
f=open(fname,"w")
f.write(stri)
f.close()
print("Done. Text file containing details has been created")
