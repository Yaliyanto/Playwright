from playwright.sync_api import Page, expect
from time import sleep
import pytest


#Login dengan username & passowrd yang tidak kosong sampai CO
def test_login(page: Page):   
    page.goto("https://saucedemo.com")
    
    page.locator('//input[@placeholder="Username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()
    
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_page_title = page.locator("//div[@class='app_logo']").text_content()
    assert inventory_page_title == 'Swag Labs'
    
    page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    inventory_deskripsi_subtitle = page.locator('[data-test="cart-desc-label"]').text_content()
    assert inventory_deskripsi_subtitle == 'Description'
    sleep(5)

    page.close()

#Login dengan username benar dan password yang kosong
def test_login_negatif_password(page: Page):   
    page.goto("https://saucedemo.com")
    
    page.locator('//input[@placeholder="Username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('')
    page.locator('[id="login-button"]').click()
    
    page.locator('[data-test="error"]').inner_text()

    galat = page.locator('[data-test="error"]').inner_text()
    
    assert galat == "Epic sadface: Password is required"


    # expect(page).to_have_title("Swag Labs")
    # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # inventory_page_title = page.locator("//div[@class='app_logo']").text_content()
    # assert inventory_page_title == 'Swag Labs'
    
    # page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    # page.locator('[data-test="shopping-cart-link"]').click()
    # inventory_deskripsi_subtitle = page.locator('[data-test="cart-desc-label"]').text_content()
    # assert inventory_deskripsi_subtitle == 'Description'
    # sleep(5)

    page.close()

# Login dengan username yang kosong
def test_login_negatif_username(page: Page):   
    page.goto("https://saucedemo.com")
    
    page.locator('//input[@placeholder="Username"]').fill('')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()
    
    page.locator('[data-test="error"]').inner_text()

    galat = page.locator('[data-test="error"]').inner_text()
    
    assert galat == "Epic sadface: Username is required"


    # expect(page).to_have_title("Swag Labs")
    # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # inventory_page_title = page.locator("//div[@class='app_logo']").text_content()
    # assert inventory_page_title == 'Swag Labs'
    
    # page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    # page.locator('[data-test="shopping-cart-link"]').click()
    # inventory_deskripsi_subtitle = page.locator('[data-test="cart-desc-label"]').text_content()
    # assert inventory_deskripsi_subtitle == 'Description'
    # sleep(5)

    page.close()





























# test = [('standar_user','','Epic sadface: Password is required'),
#         ('','secret_sauce','Epic sadface: Username is required'),]

# @pytest.mark.parametrize('username, password, error' , test)    
# def test_login_negative(page: Page,username, password, error):
#     page.goto("https://saucedemo.com")
    
#     page.locator('//input[@placeholder="Username"]').fill(username)
#     page.locator('[data-test="password"]').fill(password)
#     page.locator('[id="login-button"]').click()    
    
#     galat = page.locator('[data-test="error"]').inner_text()
    
#     assert galat == error







