from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import csv
import time
import os
from stockkdata.models import CompanyUpdate,ListOfCompanies,NewListing,CorpAction,SAST,Result,BoardMeeting,AGM_EGM,Random

from django.core.management.base import BaseCommand,CommandError

DIR_PATH=os.path.dirname(__file__)

class Command(BaseCommand):
    help="fill data"
    def handle(self,*args,**options):
        options=webdriver.ChromeOptions()
        browser=webdriver.Chrome(executable_path=str(DIR_PATH+"/chromedriver"),chrome_options=options)
        with open(str(DIR_PATH+"/ListOfScrips.csv"), "r") as csvfile:
            readfile=csv.reader(csvfile)
            counter=0
            with open("outstanding_comapanies.csv","w") as outcsv:
                writer=csv.writer(outcsv)
                for row in readfile:

                    if(counter==100):
                        break
                    if(row[0]!='Security Code' and int(row[0])>500031 and int(row[0])!=500068):
                        print("Count-",counter)
                        time.sleep(5)
                        url="https://www.bseindia.com/corporates/ann.html?scrip={}&dur=A".format(row[0])
                        company=ListOfCompanies.objects.get(company_id=row[0])

                        browser.get(url)
                        test_endof_company_data=[]
                        total_data=[]

                        while(True):
                            try:
                                temp=[]

                                headings=browser.find_elements_by_css_selector("td[class='tdcolumngrey']")
                                category=browser.find_elements_by_css_selector("td[class='tdcolumngrey ng-binding']")
                                time_object=browser.find_elements_by_css_selector("tr[class='ng-scope']")
                                number_of_posts=len(time_object)
                                print(number_of_posts)
                                if(len(time_object)==1 and time_object[0].text==""):
                                    print("error in company ",row[0])
                                    writer.writerow(row[0])

                            # for heading in category:
                                #
                                #     temp.append(heading.text)
                                #     total_data.append(heading.text)
                                for post in range(0, number_of_posts - 1):
                                    temp.append(headings[post].text)


                                if(temp==test_endof_company_data):
                                    break
                                else:

                                    test_endof_company_data=temp
                                    link_to_next_page=browser.find_elements_by_css_selector("a[ng-click='selectPage(page + 1, $event)']")


                                    for post in range(0, number_of_posts - 1):
                                        x = time_object[post].text

                                        dissemination_time = x[x.index("Exchange Disseminated Time") + 27:x.index(
                                            "Exchange Disseminated Time") + 27 + 19]
                                        dissemination_time = datetime.strptime(dissemination_time, "%d-%m-%Y %H:%M:%S")
                                        data = None
                                        category_name = category[post].text

                                        if (category_name == "Company Update"):
                                            test_data=CompanyUpdate.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = CompanyUpdate(company=company, title=headings[post].text,
                                                                 category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "AGM/EGM"):
                                            test_data=AGM_EGM.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = AGM_EGM(company=company, title=headings[post].text,
                                                           category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "Result"):
                                            test_data=Result.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = Result(company=company, title=headings[post].text,
                                                          category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "Corp. Action"):
                                            test_data=CorpAction.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = CorpAction(company=company, title=headings[post].text,
                                                              category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "Board Meeting"):
                                            test_data=BoardMeeting.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = BoardMeeting(company=company, title=headings[post].text,
                                                                category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "Insider Trading / SAST"):
                                            test_data=SAST.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = SAST(company=company, title=headings[post].text,
                                                        category=category[post].text, time=dissemination_time)
                                            data.save()

                                        elif (category_name == "New Listing"):
                                            test_data=NewListing.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = NewListing(company=company, title=headings[post].text,
                                                              category=category[post].text, time=dissemination_time)
                                            data.save()
                                        else:
                                            test_data=Random.objects.filter(time=dissemination_time)
                                            if(len(test_data)>=1):
                                                print("repeated")
                                                continue
                                            data = Random(company=company, title=headings[post].text,
                                                          category="Random", time=dissemination_time)
                                            data.save()
                                    print(len(headings), len(time_object))
                                    for link in link_to_next_page:
                                        print(link.text)
                                        link.click()
                                    time.sleep(2)
                            except Exception as e:
                                print(e)

                        counter+=1

# def crawl_info_current_page(browser):
#     with open("./ListOfScrips.csv","r") as csvfile:
#         readfile=csv.reader(csvfile)
#         counter=0
#         for row in readfile:
#
#             if(counter==1):
#                 break
#             if(row[0]!='Security Code'):
#
#                 url="https://www.bseindia.com/corporates/ann.html?scrip={}&dur=A".format(row[0])
#                 company=ListOfCompanies.objects.get(company_id=row[0])
#
#                 browser.get(url)
#                 test_end_company_data=[]
#                 total_data=[]
#
#                 while(True):
#                     try:
#                         temp=[]
#
#                         headings=browser.find_elements_by_css_selector("td[class='tdcolumngrey']")
#                         category=browser.find_element_by_css_selector("td[class='tdcolumngrey ng-binding']")
#                         time_object=browser.find_elements_by_css_selector("tr[class='ng-scope']")
#                         number_of_posts=len(time_object)
#                         if(len(time_object)==1 and time_object[0].text=""):
#                             print("error in company ",row[0])
#                             break
#
#                         # for heading in headings:
#                         #
#                         #     temp.append(heading.text)
#                         #     total_data.append(heading.text)
#
#                         for post in range(0,number_of_posts):
#                             x=time_object[post].text
#                             dissemination_time=x[x.index("Exchange Disseminated Time")+27:x.index("Exchange Disseminated Time")+27+19]
#                             dissemination_time=datetime.strptime(dissemination_time,"%d-%m-%Y %H:%M:%S")
#                             data=None
#                             if(category[post].text==""):
#                                 data=CompanyUpdate(company=company,title=headings[post].text,category=category[post].text,time=dissemination_time)
#                             else:
#                                 category_name=category[post].text
#                                 if(category_name=="Company Update"):
#                                     data = CompanyUpdate(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="AGM/EGM"):
#                                     data=AGM_EGM(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="Result"):
#                                     data=Result(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="Corp. Action"):
#                                     data=CorpAction(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="Board Meeting"):
#                                     data=BoardMeeting(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="Insider Trading/SAST"):
#                                     data=SAST(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#                                 elif(category_name=="New Listing"):
#                                     data=NewListing(company=company, title=headings[post].text,
#                                                          category=category[post].text, time=dissemination_time)
#
#
#
#                         if(temp==test_end_company_data):
#                             break
#                         else:
#                             data.save()
#                             test_end_company_data=temp
#                             link_to_next_page=browser.find_elements_by_css_selector("a[ng-click='selectPage(page + 1, $event)']")
#                             print(len(headings), len(time_object))
#
#                             for link in link_to_next_page:
#                                 print(link.text)
#                                 link.click()
#                             time.sleep(2)
#                     except:
#                         print()
#
#                 # print(*test_end_company_data)
#
#                 # print(total_data)
#                 counter+=1
# if __name__=="__main__":
#
#     options=webdriver.ChromeOptions()
#
#     browser=webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
#     crawl_info_current_page(browser)
#
#
#
