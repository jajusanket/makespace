from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import random


class TestQuestion2(unittest.TestCase):
    pass

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_question_2_script(self):
        """User should be able to make a booking appointment"""
        self.driver.get("https://dev.mksp.co/")
        phone_number = "855" + str(random.randint(1000000, 9999999))

        business_storage_nav_button = self.driver.find_element_by_id("homepage.click.business")
        assert business_storage_nav_button.is_enabled()

        try:
            self.__fill_in_big_form(phone_number)
        except NoSuchElementException:
            self.__fill_in_small_form()

        select_plan_buttons = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, "//button[text()='Select Plan']")))
        select_plan_buttons.__getitem__(1).click()

        bins_field = self.driver.find_element(By.XPATH, "//input[@class='makespace-ui-library-1ybr8iu e1ws5ted1']")
        bins_field.send_keys(4)

        continue_with_plan_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Continue with 5')]")
        sleep(1)
        continue_with_plan_button.click()

        got_it_button = self.driver.find_element_by_xpath("//button[@class='epfibpa8 makespace-ui-library-ctdhjf emakht90']")
        got_it_button.click()

        sleep(2)

        need_2_people_yes_button = self.driver.find_element_by_xpath("//label[@name='large-items'][@value='_yes']")
        need_2_people_yes_button.click()

        bulky_items_no_button = self.driver.find_element_by_xpath("//label[@for='radio-bulky-items-_no']")
        bulky_items_no_button.click()

        climb_stairs_yes_button = self.driver.find_element_by_xpath("//label[@for='radio-walk-up-_yes']")
        climb_stairs_yes_button.click()

        fragile_items_yes_button = self.driver.find_element_by_xpath("//label[@for='radio-fragile-items-_yes']")
        fragile_items_yes_button.click()

        disassemble_no_button = self.driver.find_element_by_xpath("//label[@for='radio-disassembly-_no']")
        disassemble_no_button.click()

        details_continue_button = self.driver.find_element_by_xpath("//button[text()='Continue']")
        self.driver.execute_script("arguments[0].scrollIntoView();", details_continue_button)
        details_continue_button.click()

        now = datetime.now()  # current date and time
        date_time_stamp = now.strftime("%Y%m%d%H%M%S")

        full_name_field = self.driver.find_element_by_name("full_name")
        full_name_field.send_keys("SJSJjk" + date_time_stamp)

        phone_field = self.driver.find_element_by_name("phone")
        phone_field.send_keys(phone_number)

        email_field = self.driver.find_element_by_name("email")
        email_field.send_keys("SJ+" + date_time_stamp + "@harrysqa.com")

        armed_forces_no_radio_option = self.driver.find_element_by_xpath("//label[@for='radio-is_military-_no']")
        armed_forces_no_radio_option.click()

        appointment_continue_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[text()='Continue']")))
        appointment_continue_button.click()

        appointment_address_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "address_pretty")))
        appointment_address_field.send_keys("123 William Street, New York, NY, USA")
        sleep(2)
        appointment_floor_field = self.driver.find_element_by_xpath(
            "//input[@placeholder='Optional'][@class='makespace-ui-library-1rat6ui e1ws5ted1']")
        appointment_floor_field.send_keys("Floor 22")
        appointment_address_field.send_keys(Keys.RETURN)

        confirm_and_continue_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Confirm and continue']"))
        )
        confirm_and_continue_button.click()

        in_2_days_time = datetime.today() + timedelta(2)
        in_2_days_time_date_stamp = in_2_days_time.strftime("%m/%d/%Y")

        appointment_date_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((
                By.XPATH, "//div[@class='react-datepicker__input-container']/input")))
        appointment_date_field.send_keys(in_2_days_time_date_stamp + Keys.RETURN)
        sleep(2)

        appointment_time_field = self.driver.find_element_by_name("Time")
        appointment_time_field.click()
        sleep(1)
        appointment_time_field.send_keys(Keys.ARROW_DOWN)
        appointment_time_field.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        appointment_time_field.send_keys(Keys.RETURN)

        confirm_and_continue_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Confirm and continue']"))
        )
        confirm_and_continue_button.click()

        payment_iframes = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((
                By.XPATH, "//iframe[contains(@name, '__privateStripeFrame')]")))
        self.driver.switch_to.frame(payment_iframes.__getitem__(0))

        card_number_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span/input[@name='cardnumber']")))
        card_number_field.send_keys("4111111111111111")

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(payment_iframes.__getitem__(1))

        card_expiry_field = self.driver.find_element_by_xpath("//span/input[@name='exp-date']")
        card_expiry_field.send_keys("0123")

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(payment_iframes.__getitem__(2))

        card_cvc_field = self.driver.find_element_by_xpath("//span/input[@name='cvc']")
        card_cvc_field.send_keys(777)

        self.driver.switch_to.default_content()

        card_name_field = self.driver.find_element_by_name("card-name")
        card_name_field.send_keys("SJSJ")

        agree_to_terms_radio_button = self.driver.find_element_by_xpath("//label[@class='makespace-ui-library-y3wtxm e2us3j20']")
        agree_to_terms_radio_button.click()

        book_appointment_button = self.driver.find_element_by_xpath("//button[text()='Confirm and book my appointment']")
        book_appointment_button.click()

        confirmation_date = in_2_days_time.strftime("%B %d, from 12pm-3pm")

        confirmation_date_element = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.bold:nth-child(1)"))
        )

        assert confirmation_date_element.text == confirmation_date

        done_button = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.ID, "js-skip"))
        )
        done_button.click()

        free_storage_modal = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='base-modal-close js-modal-close']"))
        )
        free_storage_modal.click()

        logged_in_account_nav_item = self.driver.find_element_by_id("menu-item--account-wrapper")

        assert logged_in_account_nav_item.text == "SJ"

    def __fill_in_big_form(self, phone_number):
        name_form_field = self.driver.find_element_by_name("name")
        name_form_field.send_keys("SJSJ")
        phone_number_form_field = self.driver.find_element_by_name("phone")
        phone_number_form_field.send_keys(phone_number)
        zip_code_form_field = self.driver.find_element_by_name("zip")
        zip_code_form_field.send_keys("10038")
        get_a_quote_button = self.driver.find_element_by_id("homepage.click.hero_get_a_quote")
        get_a_quote_button.click()

    def __fill_in_small_form(self):
        zip_code_form_fields = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Enter zip code']")))
        zip_code_form_fields.__getitem__(len(zip_code_form_fields) - 1).send_keys("10038")
        get_pricing_buttons = self.driver.find_elements_by_xpath("//button[text()='Get pricing']")
        get_pricing_buttons.__getitem__(len(get_pricing_buttons) - 1).click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
