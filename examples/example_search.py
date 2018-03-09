from Scrapers import Biddergy

# Login with credentials from file.
# Must be formatted as "USER:PASSWORD"
with open('login.txt') as f:
    credentials = f.readline().strip().split(':')
b = Biddergy(credentials[0], credentials[1])

# Login does not work yet, leave it disabled.
# b.login()

# This will print a list of items matching your search parameters.
print(b.search_by_title('ford'))

# Leave disabled.
# b.logout()
