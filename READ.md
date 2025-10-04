# Course Registration Automation Bot

## Overview
This project is a Python-based automation bot built using **Selenium**. It automates course registration on dynamic web portals by handling login, form submissions, and data extraction. The bot reduces manual effort, saves time, and can be adapted for similar repetitive browser-based tasks.

---

## Features
- **Automated Login:** Handles portal authentication securely.
- **Form Filling & Submission:** Auto-fills and submits course registration forms.
- **Error Handling:** Detects common issues and retries operations when needed.
- **Reusable & Adaptable:** Script can be easily modified for other web automation tasks.

---

## Tech Stack
- **Language:** Python  
- **Automation Framework:** Selenium  
- **Browser Driver:** ChromeDriver / GeckoDriver  
- **Dependencies:**  
  - selenium  
  - pandas (if processing data)

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/course-registration-bot.git
    cd course-registration-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the appropriate browser driver (ChromeDriver or GeckoDriver) and place it in your system PATH.

---

## Usage

1. Open the main script (`bot.py`).
2. Update login credentials and course details if required.
3. Run the bot:
    ```bash
    python bot.py
    ```
4. The bot will log in, navigate to the registration page, and complete the registration process automatically.

---

## Screenshots

*Optional:* Include images or GIFs showing the bot in action in a `screenshots/` folder.  
Example:

![Bot Demo](screenshots/bot_demo.png)

---

## Contributions

Contributions are welcome! Possible improvements include:
- Multi-course registration support
- Email notifications on successful registration
- Logging and reporting enhancements

---

## Author

**Divyansh**  
GitHub: [https://github.com/divvyaanssh](https://github.com/divvyaanssh)  
Email: work.divyansh2610@gmail.com
