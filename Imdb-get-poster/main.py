import requests,bs4
name=input("Enter movie/Tv series name\n");
print("Wait...")
try:
    googlelink="https://www.google.com/search?q=imdb "+name
    #print(googlelink)
    res=requests.get(googlelink);
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    #print(soup)
    div = soup.find("div", {"class": "hJND5c"})
    cite = div.find("cite")
    unknown="episodes"
    link="https://www.imdb"+cite.contents[2];
    '''if(link.endswith(unkown)):
        link=link[:]'''
    print(link)
    res=requests.get(link)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    div=soup.find("div",{"class":"poster"})
    image=div.find("img",{"itemprop":"image"})
    ilink=image['src']
    iname=name+".jpg"
    f=open(iname,'wb')
    f.write(requests.get(ilink).content)
    f.close()
    print("DONE. Image saved as "+iname)
except:
    print("There was some error. Check name or internet connection")

