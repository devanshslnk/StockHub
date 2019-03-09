import os
import csv
from innostock import settings
from stockkdata.models import ListOfCompanies
from django.core.management.base import  BaseCommand,CommandError

DIR_PATH=os.path.dirname(__file__)

class Command(BaseCommand):
    help='Add company data'
    def handle(self, *args, **options):
        with open(str(DIR_PATH+'/ListOfScrips.csv'),'r') as csvfile:
            reader=csv.reader(csvfile)
            # company = ListOfCompanies.objects.get(company_id='Security Code').delete()
            for row in reader:
                if(row[0]=='Security Code' or int(row[0])<=500458):
                    continue
                url="https://www.bseindia.com/corporates/ann.aspx?scrip={}%20&dur=A".format(row[0])
                company=ListOfCompanies(company_id=row[0],security_id=row[1],security_name=row[2],status=row[3],url=url)
                company.save()

