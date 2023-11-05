import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GmailLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()  # Using Firefox browser (GeckoDriver)
        self.driver.maximize_window()

    def test_login_to_gmail(self):
        self.driver.get("https://mail.google.com/")
        self.assertIn("Gmail", self.driver.title)

        email = "f0xii540@gmail.com"
        password = "your_password"

        email_input = self.driver.find_element(By.ID, "identifierId")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        # Explicit wait for the password input field
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Wait for the Gmail inbox page to load after login
        self.driver.implicitly_wait(10)

        # Example assertion: You can modify this according to your test scenario
        self.assertIn("Inbox", self.driver.title)

    def tearDown(self):
        try:
            self.driver.close()
        except Exception as e:
            # Handle the exception gracefully, log, or handle based on your requirement
            pass

if __name__ == '__main__':
    unittest.main()
