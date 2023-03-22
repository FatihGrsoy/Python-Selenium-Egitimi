from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Cases:    
    
    def userName_and_password_empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)            
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        emptyErrorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = emptyErrorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU : {testResult}")
        sleep(2)      
           
    
    def just_password_empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("Fatih")
        passwordInput.send_keys()
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        emptyErrorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = emptyErrorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU : {testResult}")
        sleep(2)

    def locked_out_users(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        emptyErrorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = emptyErrorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU : {testResult}")
        sleep(2)

    def users(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)            
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        productsPrint = len(products)
        print(f"Bu sayfada {productsPrint} adet ürün bulunmaktadır.")        
        sleep(2)

    def remove_error_message(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)            
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()      
        
        sleep(2)
        errorBtn = driver.find_element(By.CLASS_NAME, "error-button")
        sleep(2)
        errorBtn.click()
        sleep(2)
        removeErrorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button/svg/path")
        sleep(2)     
 
    
     

        
        



    
       
        


testClass = Test_Cases()
testClass.userName_and_password_empty()
testClass.just_password_empty()
testClass.locked_out_users()
testClass.users()
testClass.remove_error_message()

        
        



