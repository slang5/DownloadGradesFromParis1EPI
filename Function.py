from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def ConnectionAndDownload(IdParis1, PasswordParis1,Filière_inscription):

    username = IdParis1
    password = PasswordParis1
    
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Edge()
    driver.get("https://cas.univ-paris1.fr/cas/login?service=https%3A%2F%2Fidp.univ-paris1.fr%2Fidp%2FAuthn%2FExternal%3Fconversation%3De1s1&entityId=https%3A%2F%2Fcours.univ-paris1.fr")
    
    actions = ActionChains(driver)
    actions.move_by_offset(10, 20).perform() 
    time.sleep(2)

    username_field = driver.find_element(By.ID,"username")
    password_field = driver.find_element(By.ID,"password")
    username_field.send_keys(f"{username}")
    password_field.send_keys(f"{password}")
    
    login_button = driver.find_element(By.NAME,"submitBtn")
    login_button.click()

    driver.get("https://ent.univ-paris1.fr/dossier-etu/#!notesView")
    driver.execute_script("document.body.style.zoom='100%'")
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "v-table-table"))
        )
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{Filière_inscription}']/ancestor::div[contains(@class, 'v-button')]"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()
    
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


    try:
        dialogue = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'v-window') and contains(@role, 'dialog')]"))
        )
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'v-window') and contains(@role, 'dialog')]//div[contains(@class, 'v-button') and contains(@class, 'red-button-icon') and contains(@role, 'button') and contains(@tabindex, '0')]"))
        )
        driver.execute_script("arguments[0].click();", button)
    
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    time.sleep(5)
    driver.quit()
    return 'OURNA'

def get_latest_downloaded_file(folder):
        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files[0]

def Sendmail(To, fromMail, fromPassword):

    user_home = os.path.expanduser('~')
    downloads_path = os.path.join(user_home, 'Downloads')

    folderdownload = downloads_path
    latest_file = get_latest_downloaded_file(folderdownload)
    
    fromaddr = fromMail
    password = fromPassword
    toaddr = To
    subject = "Reporting Notes Université"
    body = "Veuillez trouver ci-joint le document PDF téléchargé."
    
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain')) 
    
    filename = os.path.basename(latest_file)
    filepath = os.path.join(folderdownload, filename)
    attachment = open(filepath, "rb")

    part = MIMEBase('application', 'pdf')
    part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    filename = "Notes S2 UNIV.pdf"
    part.add_header(
        'Content-Disposition',
        f'attachment; filename="{filename}"'
    )
    
    msg.attach(part)
    attachment.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
  
    time.sleep(3)
    server.quit()
    os.remove(filepath)
    return 'OURNA'

def Complet(IdParis1, PasswordParis1,Filière_inscription,To, fromMail, fromPassword):
    ConnectionAndDownload(IdParis1, PasswordParis1,Filière_inscription)
    Sendmail(To, fromMail, fromPassword)
    return 'OURNA'
