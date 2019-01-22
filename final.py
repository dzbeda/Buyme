from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys


### Variables ###
first_name = 'Dudu'
email_reg = 'dud4.confirm@gmail.com'
password = 'Duduzbeda1'
send_to = 'טליה'
send_from = 'דודו'

### Upload Driver ###
#chrom_driver = webdriver.Chrome(executable_path="C:\\Users\\zbeda\\Dropbox\\DevOps\\selenium\\selenium_driver\\chromedriver.exe")
chrom_driver = webdriver.Chrome(executable_path="C:\\Users\\dzbeda\\Dropbox\\DevOps\\selenium\\selenium_driver\\chromedriver.exe")

##Read website from website.txt file
myfile = open("website.txt",'r+')   # append in the end of the file
website=myfile.readlines()

#login to buyme.co.il site
chrom_driver.get(website[0])
sleep(1)

##########  Registration ####################

# find element הרשמה | כניסה using xpath and click it
click_main_page = chrom_driver.find_element_by_xpath('//*[@id="ember589"]/div/ul[1]/li[3]/a/span[1]')
click_main_page.click()


# find element הרשמה using xpath and click it
register = chrom_driver.find_element_by_xpath('//*[@id="ember570"]/div/div[1]/div/div/div[3]/p/span')
register.click()



#update information for registry process
first_name_box = chrom_driver.find_element_by_xpath('//*[@placeholder="שם פרטי"]')
first_name_box.send_keys(first_name)


email_box = chrom_driver.find_element_by_xpath('//*[@placeholder="מייל"]')
email_box.send_keys(email_reg)


password_box = chrom_driver.find_element_by_xpath('//*[@placeholder="סיסמה"]')
password_box.send_keys(password)


re_password_box = chrom_driver.find_element_by_xpath('//*[@placeholder="אימות סיסמה"]')
re_password_box.send_keys(password)


#Check the i agree
re_password_box.send_keys(Keys.TAB + Keys.SPACE)

#Submit
chrom_driver.find_element_by_xpath("//*[text()='הרשמה ל-BUYME']").click()

sleep(5)
########  HOME Screen ############

##Choose price

chrom_driver.find_element_by_xpath('//*[@id="ember662_chosen"]/a/span').click()
chrom_driver.find_element_by_xpath('//*[@id="ember662_chosen"]/div/ul/li[2]').click()


##Choose region

chrom_driver.find_element_by_xpath('//*[@id="ember677_chosen"]/a/span').click()
chrom_driver.find_element_by_xpath('//*[@id="ember677_chosen"]/div/ul/li[2]').click()


##Choose category

chrom_driver.find_element_by_xpath('//*[@id="ember686_chosen"]/a/span').click()
chrom_driver.find_element_by_xpath('//*[@id="ember686_chosen"]/div/ul/li[4]').click()

##Submit search

chrom_driver.find_element_by_id('ember721').click()

sleep(2)

########  Choose Bussines Screen ##########


##choose bussines
chrom_driver.find_element_by_xpath('//*[@href="https://buyme.co.il/supplier/1605382"]').click()
sleep(2)

##choose amount
amount = chrom_driver.find_element_by_xpath('//*[@placeholder="מה הסכום?"]')
amount.click()
amount.send_keys('250')
chrom_driver.find_element_by_xpath("//*[text()='לבחירה']").click()

sleep(2)


#############   Sender & Reciver ###############


#send to name
to = chrom_driver.find_element_by_xpath('//*[@data-parsley-required-message="מי הזוכה המאושר? יש להשלים את שם המקבל/ת"]')
to.click()
to.clear()
to.click()
to.send_keys(send_to)

#send from name
sender = chrom_driver.find_element_by_xpath('//*[@data-parsley-required-message="למי יגידו תודה? שכחת למלא את השם שלך"]')
sender.click()
sender.clear()
sender.click()
sender.send_keys(send_from)

#event
chrom_driver.find_element_by_xpath("//*[text()='לאיזה אירוע?']").click()
chrom_driver.find_element_by_xpath('//*[@id="ember1304_chosen"]/div/ul/li[4]').click() # Need to improv

#wish
wish = chrom_driver.find_element_by_xpath('//*[@id="ember1318"]/textarea') # Need to improve
wish.click()
wish.clear()
wish.send_keys('yesssss')

#Upload picture
chrom_driver.find_element_by_xpath('//*[@name="fileUpload"]').send_keys('C:\pic\dudu.jpg')


#how to send
chrom_driver.find_element_by_xpath('//*[@id="ember1253"]/div[4]/div/div[1]/div[2]').click()  # Need to improve
email = chrom_driver.find_element_by_xpath('//*[@placeholder="כתובת המייל של מקבל/ת המתנה"]')
email.click()
email.clear()
email.click()
email.send_keys(email_reg)
sleep(2)
chrom_driver.find_element_by_xpath("//*[text()='שמירה']").click()


#Submit
chrom_driver.find_element_by_xpath("//*[text()='תשלום']").click()

