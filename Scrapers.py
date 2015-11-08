from robobrowser import RoboBrowser
import re
import sys


class Biddergy(object):
    def __init__(self, email="None", passwd="None"):
        self.email = email
        self.passwd = passwd
        self.login(self.email, self.passwd)

    # =======|URL Shortcuts|========
    urlBase =         'https://www.biddergy.com/'
    page_MyAccount =  'https://www.biddergy.com/myauction.asp'
    page_Watching =   'https://www.biddergy.com/myauction.asp?tab=watching'
    page_Bidding =    'https://www.biddergy.com/myauction.asp?tab=bidding'
    page_Won =        'https://www.biddergy.com/myauction.asp?tab=won'
    page_NotWon =     'https://www.biddergy.com/myauction.asp?tab=notwon'
    page_Purchases =  'https://www.biddergy.com/myauction.asp?tab=purchases'
    page_Account =    'https://www.biddergy.com/myauction.asp?tab=account'
    page_Billing =    'https://www.biddergy.com/myauction.asp?tab=billing'
    page_Login =      'https://www.biddergy.com/login.asp'
    page_Logout =     'https://www.biddergy.com/index.asp?logoff=1'
    browser = RoboBrowser(history=True, parser='lxml')

    # Log in to biddergy.com
    def login(self, email, passwd):
        print('Logging in...')
        self.browser.open(self.page_Login)



        frm_login = self.browser.get_form(action='/login.asp')
        frm_login['email'] = email
        frm_login['password'] = passwd
        self.browser.session.headers['Referer'] = self.urlBase
        self.browser.submit_form(frm_login)

    # Log out of biddergy.com
    def logout(self):
        print('Logging out...')
        self.browser.open(self.page_Logout)

    # Get summary from biddergy
    def summary(self):
        print('Loading summary...')
        self.browser.open(self.page_MyAccount)
        summary_data = []
        for info in self.browser.find_all('li', class_='MySummaryInfo'):
            num = re.search('^\S*', info.text).group(0)
            summary_data.append(num)
        print(summary_data)
        return summary_data
