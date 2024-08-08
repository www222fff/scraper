# download chrome driver as below example:

wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip

wget https://dl.google.com/linux/deb/pool/main/g/google-chrome-stable/google-chrome-stable_126.0.6478.182-1_amd64.deb

sudo apt install ./google-chrome-stable_126.0.6478.182-1_amd64.deb

Note:

Do not run with proxy env variable setting, as below error will be triggered when init driver = webdriver.Chrome(service=service, options=options)

"504 DNS look up failed" and "The proxy server reported that an error occurred while trying to access the website."
