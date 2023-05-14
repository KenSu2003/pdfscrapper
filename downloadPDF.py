from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()


options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'



#Pick correct user to access the website from
options.add_argument('--user-data-dir=~/Library/Application Support/Google/Chrome/')
options.add_argument('--profile-directory=Profile 2')


options.add_argument('--kiosk-printing')



driver = webdriver.Chrome(options=options)
driver.get('https://umass.khpcontent.com/mathcompsci/page/practice6?type=question-list&page_type=11143201')

driver.execute_script('window.print();')

driver.quit()
