from djchoices import DjangoChoices,ChoiceItem


class UserTypeChoice(DjangoChoices):
    CUSTOMER=ChoiceItem('CTR')
    ADMIN=ChoiceItem('ADM')