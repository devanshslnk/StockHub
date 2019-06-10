from bs4 import BeautifulSoup
import requests,urllib
import html5lib
from pprint import pprint
import csv


def crawler_code(url_extension,received_time,writefile):
    #fetching url
    base_url="https://www.bseindia.com/corporates/"

    
    current_url=base_url+url_extension
    print(current_url)
    url_content=requests.get(current_url)

    # using beautiful soup to parse data

    soup=BeautifulSoup(url_content.content,'html5lib')



    main_header_info=soup.find_all("td",attrs={"class":"TTHeadergrey"})
    
    summary=soup.find_all("td",attrs={"class":"TTRow_leftnotices"})

    next_page_link=soup.find("span",attrs={"id":"ctl00_ContentPlaceHolder1_lblNext"})
    # print(next_page_link.a['href'])
    counter=1
    for i in range((len(summary)-1)//2):
        # print(summary[counter].text)
        ls=[main_header_info[4*i].text,main_header_info[(4*i)+1].text,summary[counter].text]
        counter+=2
        writer=csv.writer(writefile)
        writer.writerow(ls)

    print(next_page_link.a["href"])
    next_page_link.a['href'].replace(" ","%")
    return  next_page_link.a["href"]


def main_crawler_controller():
    with open("ListOfScrips.csv","r") as readfile:
        reader=csv.reader(readfile)
        counter=0 
        
        for row in reader:
            if(row[0]=="Security Code"):
                continue
            if(counter==5):
                break
            first_page_url_path="ann.aspx?scrip={}%20&dur=A".format(row[0])
            
            with open("{}_scraped_data1.csv".format(row[1]),"w") as writefile:
                new_path=crawler_code(first_page_url_path,0,writefile)

                for i in range(0,4):
                    new_path=crawler_code(new_path,0,writefile)
            counter+=1
            # print(new_path)
# crawler_code("ann.aspx?expandable=0",0)
if __name__=="__main__":
    main_crawler_controller()


