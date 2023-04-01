from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest
from time import sleep

class Test_Sauce():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    
    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_get_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()      
        self.driver.save_screenshot(f"{self.folderPath}/test-get-login-{username}-{password}.png") 
        sleep(2)
    
   
    @pytest.mark.parametrize("username,password",[("Fatih","Gürsoy"),("abc","123"),("xyz","2")])
    def test_invalid_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMesage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png") 
        assert errorMesage.text == 'Epic sadface: Username and password do not match any user in this service'

    
    @pytest.mark.parametrize("username,password",[("", "")])
    def test_userName_and_password_empty(self,username,password):
        self.wait_for_element_visible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Username is required'      

    
    @pytest.mark.parametrize("username,password",[("Fatih","")])
    def test_just_password_empty(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Password is required'

    
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_out_users(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'
        sleep(2)
       
   
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_item_number(self, username, password):
        self.wait_for_element_visible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
       
        self.wait_for_element_visible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
       
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
       
        itemNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{password}.png")
        assert len(itemNumber) == 6
        sleep(2)
    
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_log_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        optionsBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        optionsBtn.click()
        sleep(2)
        
        logOutBtn = self.driver.find_element(By.ID, "logout_sidebar_link")
        self.driver.save_screenshot(f"{self.folderPath}/test-log-out-{username}-{password}.png")
        logOutBtn.click()
        sleep(2)
        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_select_product(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        selectPrd = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        self.driver.save_screenshot(f"{self.folderPath}/test-select-product-{username}-{password}.png")
        selectPrd.click()
        sleep(2)
        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_go_to_cart(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        selectPrd = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        selectPrd.click()
        sleep(2)   
                     
        goToCart = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        self.driver.save_screenshot(f"{self.folderPath}/test-go-to-cart-{username}-{password}.png")
        goToCart.click()
        sleep(2)
        
        



    
        

        