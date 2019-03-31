from django.db import models


# Create your models here.
class ListOfCompanies(models.Model):
    company_id=models.CharField(max_length=10,unique=True)
    security_id=models.CharField(max_length=200,unique=True)
    security_name=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    url=models.URLField(verbose_name='BSE company url', default=None)
    def __str__(self):
        return self.security_name

class CompanyUpdate(models.Model):
    company=models.ForeignKey(ListOfCompanies,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')


    def __str__(self):
        return self.title

class BoardMeeting(models.Model):

    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title

class AGM_EGM(models.Model):

    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title

class CorpAction(models.Model):
    company = models.ForeignKey(ListOfCompanies,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title

class SAST(models.Model):
    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title

class NewListing(models.Model):
    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')
    def __str__(self):
        return self.title

class Result(models.Model):
    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title

class Random(models.Model):
    company = models.ForeignKey(ListOfCompanies, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    link_to_pdf = models.URLField(verbose_name='actual_pdf_url')

    def __str__(self):
        return self.title
class NewFilter(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name