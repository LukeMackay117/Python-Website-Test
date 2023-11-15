from seleniumbase import BaseCase
import time

class CNNAutomationTest(BaseCase):

    def test_email_invalid(self):
        self.open('https://www.cnn.com/')
        time.sleep(3)
        self.click('button:contains("Log In")')
        time.sleep(2)
        self.type('input[placeholder="Email address"]', "joe123@gmail")
        time.sleep(4)
        self.type('input[placeholder="Password"]', "123456")
        time.sleep(4)
        self.assert_text('Please enter a valid email address')

    def test_login_fail(self):
        self.open('https://www.cnn.com/')
        time.sleep(3)
        self.click('button:contains("This Should Fail")')
       
       
       