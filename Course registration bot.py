from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
import threading

# ===== CONFIG =====
ROLL_NUMBER = "MAIL / ROLL NUM"
PASSWORD = "PASSWORD"
TARGET_SUBJECT_CODES = ["SUBJECT CODE"]
REFRESH_INTERVAL = 0  # seconds
ALARM_DURATION = 5  # seconds
DRIVER_PATH = r"DRIVER PATH"

def background_alarm(duration=ALARM_DURATION):
    def ring():
        end_time = time.time() + duration
        while time.time() < end_time:
            winsound.Beep(2000, 300)
            winsound.Beep(2500, 300)
    threading.Thread(target=ring, daemon=True).start()

def start_bot():
    # ===== SETUP DRIVER =====
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument('--ignore-certificate-errors')
    service = Service(DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        # ===== LOGIN FUNCTION =====
        def login():
            print("🔐 Logging in...")
            driver.get("https://reg.exam.dtu.ac.in/student/login")

            roll_field = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//input[@placeholder and contains(@placeholder, "Eg- 23/MC/09")]')))
            pass_field = driver.find_element(By.XPATH, '//input[@type="password"]')
            login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')

            roll_field.send_keys(ROLL_NUMBER)
            pass_field.send_keys(PASSWORD)
            login_btn.click()

            print("🚀 Navigating directly to course registration page...")
            driver.get("REG PAGE URL")

        login()

        wait.until(lambda d: any(
            d.find_elements(By.XPATH, f"//td[contains(text(),'{code}')]") for code in TARGET_SUBJECT_CODES))
        print("✅ Course registration page detected. Watching subjects...")

        registered = set()

        while True:
            time.sleep(REFRESH_INTERVAL)
            driver.refresh()

            # 🛑 Check for logout (login page visible again)
            if driver.find_elements(By.XPATH, '//input[@type="password"]'):
                raise Exception("🔁 Logged out detected — restarting bot")

            for code in TARGET_SUBJECT_CODES:
                if code in registered:
                    continue

                try:
                    subject_row = driver.find_element(By.XPATH, f"//td[contains(text(),'{code}')]/..")
                    cells = subject_row.find_elements(By.TAG_NAME, "td")
                    available_seats = int(cells[4].text.strip())

                    print(f"💺 {code}: {available_seats} seats")

                    if available_seats > 0:
                        register_button = cells[5].find_element(By.XPATH, ".//form/button[contains(text(),'Register')]")

                        driver.execute_script("arguments[0].scrollIntoView(true);", register_button)
                        driver.execute_script("arguments[0].click();", register_button)

                        time.sleep(5)

                        updated_row = driver.find_element(By.XPATH, f"//td[contains(text(),'{code}')]/..")
                        bg_color = updated_row.value_of_css_property("background-color")

                        if "rgba(15, 242, 136" in bg_color:
                            print(f"✅ Registered for {code}")
                            background_alarm()
                            registered.add(code)
                        else:
                            print(f"❌ Register clicked but not confirmed for {code}")

                except Exception as e:
                    print(f"⚠️ {code}: Error - {e}")

            if len(registered) == len(TARGET_SUBJECT_CODES):
                print("🎯 All subjects registered.")
                break

    except Exception as e:
        print(f"❌ Script crashed or logged out: {e}")
        background_alarm()
        driver.quit()
        print("🔁 Restarting script...\n")
        start_bot()  # 🔁 Recursively restart the whole bot

    finally:
        try:
            driver.quit()
        except:
            pass
        print("🚪 Driver closed.")

# ===== RUN SCRIPT =====
start_bot()
