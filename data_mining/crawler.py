import time
import os
from data_mining import vars
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = (
        "POST",
        '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {'behavior': 'allow','downloadPath': download_dir}
        }
    browser.execute("send_command", params)

def build_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
            "download.default_directory": vars.download,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--headless=True')
    return chrome_options

def extract_data():
    # remove old files from /downloads folder
    if os.path.exists(vars.adult_data):
        os.remove(vars.adult_data)
    if os.path.exists(vars.adult_test):
        os.remove(vars.adult_test)
    if os.path.exists(vars.adult_data_test):
        os.remove(vars.adult_data_test)
    # build options
    chrome_options = build_chrome_options()
    # initialize webdriver
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=vars.chromedriver_path)
    # set download folder
    enable_download_headless(driver, vars.download)
    # navigate to url and downloads files
    driver.get(vars.url_download_data)
    driver.get(vars.url_download_test)
    time.sleep(vars.TIMEOUT)
    driver.close
    driver.quit
