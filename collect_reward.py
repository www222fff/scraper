import os, re, csv
from exchangelib import DELEGATE, Account, Credentials, Configuration

# Define your email credentials
email_address = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
server = 'mail.nokia-sbell.com'

# Set up credentials and configuration
credentials = Credentials(username=email_address, password=password)
config = Configuration(server=server, credentials=credentials)

# Set up the account
account = Account(
    primary_smtp_address=email_address,
    credentials=credentials,
    config=config,
    autodiscover=False,
    access_type=DELEGATE
)

# Define the regex pattern to extract the link
link_pattern = re.compile(r'https://nokia\.sharepoint\.com/sites/learn/achiev/SitePages/index\.aspx/reward/\d+')
csv_file = 'input.csv'
unique_links = set()

# Fetch emails from the inbox and search for links
try:
    for item in account.inbox.filter().order_by('-datetime_received')[:10000]:
        subject = item.subject
        sender = item.sender.email_address
        body = item.body
        if hasattr(body, 'body'):
            body = body.body
        if body is None:
            body = ""

        # Extract links matching the pattern
        links = link_pattern.findall(body)
        for link in links:
            print(f'found link {link}')
            unique_links.add(link)  # Add link to the set to ensure uniqueness

except Exception as e:
    import traceback
    print("An error occurred:")
    traceback.print_exc()


# Write unique links to the CSV file
try:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for link in unique_links:
            writer.writerow([link])  # Write each unique link

except Exception as e:
    print("An error occurred while writing to the CSV file:")
    print(e)

print(f'Unique links have been saved to {csv_file}')

