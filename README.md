# Data Extraction Script in Python

Script that applies techniques to retrieve transaction data from an account using your own cookies. The focus of this script is to scrape the data to understand how transaction data can be accessed and retrieved using cookies taken from a website in a simulated and controlled environment.

**Merchant:** [Grammarly](https://www.grammarly.com)

## Requirement

[Chrome](https://www.google.com/chrome)

[StorageAce Extension](https://chromewebstore.google.com/detail/storageace/cpbgcbmddckpmhfbdckeolkkhkjjmplo)

[Python](https://www.python.org/downloads/) >= 3.9

## Installation

Clone the project

```bash
  git clone https://github.com/mayur-jp/py-knot-test.git
```

Go to the project directory

```bash
  cd py-knot-test
```

Create virtual environment

```bash
  python -m venv venv
```

Activate virtual environment

```bash
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Run Script

Steps to run the script

1. Login into [Grammarly](https://www.grammarly.com/signin) with any sigin-option

2. You will be redirected to https://app.grammarly.com/, and you must copy all cookies using [StorageAce](https://chromewebstore.google.com/detail/storageace/cpbgcbmddckpmhfbdckeolkkhkjjmplo) Chrome Extension.
   ![storageace](public/storageace.png?raw=true "StorageAce")

3. Create a file named `cookies.json` inside the `root` folder and paste the copied cookies from StorageAce into it.

4. Now run the script,

```bash
  python main.py
```

## Screenshots

![successOutput](public/successOutput.png?raw=true "Success Output")

## 🛠 Skills/Tech Stack

Python, Rest API

## Features

- Fetch and Store User Details from the Merchant
- Fetch and Store Subscription Details from the Merchant
- Fetch and Store Transaction Details from the Merchant

## Authors

- [@mayur-jp](https://github.com/mayur-jp)

## File Structure

```
|-- .gitignore
|-- README.md
|-- classes           // contains classes
|   |-- api.py
|   |-- merchant.py
|-- common
|   |-- constant.py   // all constant variable
|   |-- function.py   // all common functions exist here
|   |-- structure.py  // all common structures
|-- cookies.json      // insert your cookies in this file
|-- main.py           // main function is excecuted from here
|-- public            // contains files which can be shown to public
|-- requirements.txt  // libraries used for this script
```

## Errors

**MISSING_NECESSARY_COOKIES_ERROR:** If necessary cookies are missing at that time, this error will be thrown

**MERCHANT_CONFIG_ERROR:** If there is an error while Configuring the merchant at that time, this error will be thrown.

**UNAUTHORIZED_ERROR:** When Verifying the User, if 401: UNAUTHORIZED ERROR comes from the merchant at that time, this error will be thrown.

**VERIFY_USER_ERROR:** When Verifying the User, if any other error comes other than UNAUTHORIZED ERROR from the merchant at that time, this error will be thrown.

**SUBSCRIPTION_ERROR:** If there is an error while fetching a Subscription from the merchant at that time, this error will be thrown.

**TRANSACTION_ERROR:** If there is an error while fetching a Transactions from the merchant at that time, this error will be thrown.

## Aproach

This script, designed to extract data about user information, subscriptions, and transactions from Grammarly, is built using node typescript technology. You can see the installed libraries inside requirement.txt; this script will only run on python version 3.9 and above.

You can run the script by python main.py, which is the main file of this script. 

Now, let's talk about the primary approach. The async main function will be executed when the project is run. Let's break down the main function.

1. **(merchant constructor)** Merchant Class Instance is created at the beginning of the main function. It will import cookies from cookies.json, verify necessary cookies for user authentication, and set default headers for future api calls.

2. **(verify_user)** Now that all default configurations are set, the verify user method is called in the main function; it will call merchant api to fetch user details using cookies and update cookies, which were imported at first. After that, it will extract the necessary information from the response and store it in the merchant class instance.

3. **(get_subscription)** Now that all prerequisites are done, it will fetch subscription details API, extract the necessary information, and store subscription details in the merchant class instance.

4. **(get_transaction)** Similar to (getSubscription), it will fetch transactions api and store necessary information in the merchant class instance

All the above 4 points describe each method in the Merchant Class.