from bs4 import BeautifulSoup
from robobrowser import RoboBrowser


class Biddergy(object):
    def __init__(self, email="None", passwd="None"):
        self.email = email
        self.passwd = passwd

    # =======|URL Shortcuts|========
    url_Base = 'https://www.biddergy.com'
    url_Watching = 'https://www.biddergy.com/Account/Bidding/Watching'
    url_Bidding = 'https://www.biddergy.com/Account/Bidding/Active'
    url_Won = 'https://www.biddergy.com/Account/Bidding/Won'
    url_NotWon = 'https://www.biddergy.com/Account/Bidding/Lost'
    url_Purchases = 'https://www.biddergy.com/Account/Invoice/Purchases'
    url_CreditCards = 'https://www.biddergy.com/Account/CreditCards'
    url_Login = 'https://www.biddergy.com/Account/Logon'
    url_Logout = 'https://www.biddergy.com/Account/Logoff'
    url_Search = 'http://www.biddergy.com/Search'
    url_UpcomingAuctions = 'http://www.biddergy.com/Listing/UpcomingAuctions'
    url_PastAuctions = 'http://www.biddergy.com/Listing/PastAuctions'
    url_Summary = 'https://www.biddergy.com/Account/Summary'

    # Old. May need to be removed or updated.
    url_Account = 'https://www.biddergy.com/myauction.asp?tab=account'
    url_Billing = 'https://www.biddergy.com/myauction.asp?tab=billing'

    browser = RoboBrowser(history=True, parser='lxml')

    # Log in to biddergy.com
    def login(self):
        print('Logging in as: ', self.email)
        self.browser.open(self.url_Login)
        frm_login = self.browser.get_form(action='/Account/Logon')
        frm_login['username'] = self.email
        frm_login['password'] = self.passwd
        self.browser.session.headers['Referer'] = self.url_Base
        self.browser.submit_form(frm_login)

        # Sanity check (^_^)
        self.loggedin = False
        if self.browser.find('body', attrs={'class': '  guest'}):
            print('Logged in as GUEST.')
        if self.browser.find('body', attrs={'class': '  loggedin'}):
            print('Logged in as {}.'.format(self.email))
            self.loggedin = True

    # Log out of biddergy.com
    def logout(self):
        print('Logging out...')
        self.browser.open(self.url_Logout)
        self.loggedin = False

    # Get account summary from biddergy
    def get_summary(self):
        if self.loggedin:
            print('Loading summary...')
            self.browser.open(self.url_Summary)
            broth = str(self.browser.parsed)
            soup = BeautifulSoup(broth, 'lxml')

            print(soup.find_all('li', attrs={'class': 'list-group-item'}))
            summary_soup = soup.find_all('div', attrs={'class': 'col-xs-12 col-md-10'})

            print(summary_soup)
            tags = ['watched', 'bidding', 'won', 'not_won', 'wonAwaiting', 'invoiceAwaiting']
            data = []
            summary = {}

            # for info in soup.find_all('li', attr={'class': 'list-group-item'}):
            # num = re.search('^\S*', info.text).group(0)
            # for x in range(len(tags)):
            #   summary.update({tags[x]: data[x]})
            return summary
        return 0

    def search_by_title(self, search_query=" "):
        print('Searching for: "' + search_query + '"')
        self.browser.open(self.url_Search)
        frm_search = self.browser.get_form(action="/Search")
        frm_search['FullTextQuery'] = search_query
        self.browser.submit_form(frm_search)

        no_items = self.browser.find('div', class_='col-xs-12 col-md-9')

        print(no_items)
        # If items ARE found then...
        # if no_items is None:
        #    s = str(self.browser.find('div', class_='HPDesc').a)
        #    parsed = re.search(r'(?i)<a href="([^>]+)">(.+?)</a>', s)
        #    link = str(parsed.group(1))
        #    linktitle = str(parsed.group(2))
        #    if link:
        #        print('Found:', linktitle+'!')
        #        return link
        # else:
        #    print('No active items found.')
        #    return '404'

    def get_item_info(self, item):
        """
        Returns an auction item as a dictionary object.
        Tags 'format', 'price', 'bids', 'opens', 'location', 'start', 'end', 'highbidder', 'description', 'images'.
        """
        item_tags = ['format', 'price', 'bids', 'opens', 'location',
                     'start', 'end', 'highbidder', 'description', 'images']
        data = {}
        # Deal with not found errors
        if item == '404':
            for x in item_tags:
                data.update({x: '-'})
            return data
        self.browser.open(item)
        broth = str(self.browser.parsed)
        soup = BeautifulSoup(broth, 'lxml')

        # Get title, lot number, and Listing number
        x = soup.find('div', id='DetailTitleRow').b.get_text()
        lot_number = x[5:11]
        title = x[12:]
        x = soup.find('div', id='DetailTitleRow').get_text()
        listing_number = x.split('\r\n')[1:][0][10:]
        data.update({'title': title, 'lot_number': lot_number, 'listing_number': listing_number})
        del x

        # Put Biddergy's item status block in dictionary.
        table = soup.find('table', attrs={'cellpadding': '2', 'cellspacing': '0'})
        rows = table.find_all('tr')
        item_data = []
        x = 0
        for row in rows:
            if x < 9:
                x += 1
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                item_data.append(cols[1])
        item_data.pop(7)
        for x in range(0, 8):
            data.update({item_tags[x]: item_data[x]})

        # Find Images and add the web links to the dictionary.
        images = []
        photos = soup.find('div', id='IDThumb')
        for a in photos.find_all('a', href=True):
            images.append(a['href'])
        print("Found", len(images), "images.")
        data.update({'images': images})

        # Find Description and add it to the dictionary.
        desc = soup.find('div', id='ItemDesc')
        data.update({'description': str(desc)})
        return data

    def get_upcoming_auctions(self):
        # Grab html for upcoming auctions
        self.browser.open(self.url_UpcomingAuctions)
        broth = str(self.browser.parsed)
        soup = BeautifulSoup(broth, 'lxml')
        # Grab only auction blocks (no menus, sidebar html, etc)
        auctions = soup.find_all('div', attrs={'class': 'AuctionRow row'})
        # Set up dictionary element
        auctionList = {}
        count = 0
        for auction in auctions:
            # Get Auction
            title = auction.find('span', attrs={'class': 'AuctionTitle'}).get_text()
            date = auction.find('span', attrs={'class': 'AuctionTime visible-xs'}).get_text()
            description = auction.find('span', attrs={'class': 'AuctionDescription'}).get_text()
            link = auction.a.get('href')

            # Put them all together and add them to the dictionary (browse)
            auctionList.update({count: {'date': date, 'title': title, 'description': description, 'link': link}})
            count += 1
        return auctionList
