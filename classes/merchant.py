import json
from .api import API
from common.constant import (
    GET_SUBSCRIPTION_API,
    GET_TRANSACTION_API,
    GET_USER_API,
    MERCHANT_CONFIG_ERROR,
    NECESSARY_COOKIES,
    ORIGIN_HEADER_URL,
    SUBSCRIPTION_ERROR,
    TRANSACTION_ERROR,
    UNAUTHORIZED_ERROR,
    VERIFY_USER_ERROR
)
from common.structure import Subscription, Transaction, User

class MERCHANT:
    def __init__(self):
        self.api = API()  # Initialize API instance
        self.transactions = []
        self.subscription = None
        self.user = None

        # Import cookies and set default configurations
        print('\nimporting cookies and setting default configurations...')
        try:
            with open("cookies.json", "r") as file:
                # Load cookies from file
                cookies = json.load(file)
                self.api.import_cookies(cookies, NECESSARY_COOKIES) # Import cookies in API instance

                # Set default headers which will be used in every request and required for the API
                self.api.set_default_headers({
                    'x-csrf-token': (self.api.get_cookie('csrf-token') or {}).get('value', ''),
                    'origin': ORIGIN_HEADER_URL
                })
                print("cookies imported and default configurations set up completed\n")
        except Exception as error:
            # If cookies import and setting default configurations failed, log the error
            print('cookies import and setting default confiurations failed\n')
            print(MERCHANT_CONFIG_ERROR, error)
            raise ValueError(MERCHANT_CONFIG_ERROR)

    async def verify_user(self):
        # Authenticate user
        print('\nauthenticating...')
        try:
            # Get user details
            response = self.api.fetch(GET_USER_API)
            user_data = response.json()
            # Set user details
            self.user = User(
                id=user_data.get('id', ''),
                email=user_data.get('email', ''),
                name=user_data.get('firstName', ''),
                isVerified=user_data.get('confirmed', False),
                loginType=user_data.get('loginType', None),
                isDisabled=user_data.get('disabled', None),
                isFree=user_data.get('free', False)
            )
            print('authentication successful\n')
            return True
        except Exception as error:
            # If user is not authenticated, it will throw an error
            print('authentication failed\n')
            if error.__dict__.get('response', {}): # If error has response then get error from response
                error = error.__dict__.get('response', {}).json() # Get merchant error from response
                status_code = error.__dict__.get('response', {}).__dict__.get('status_code', '') # Get status code from response
                
                if status_code == 401: # If status code is 401 then user is unauthorized
                    print(UNAUTHORIZED_ERROR, ": ", error)
                    raise ValueError(UNAUTHORIZED_ERROR)

            print(VERIFY_USER_ERROR, ": ", error)
            raise ValueError(VERIFY_USER_ERROR)

    async def get_subscription(self):
        # Get subscription details
        print('\ngetting subscription details...')
        try:
            response = self.api.fetch(GET_SUBSCRIPTION_API)
            subscription_data = response.json()
            current_plan = subscription_data.get('currentPlan', {})  # Get current plan details
            currency_used_for_subscription = current_plan.get('priceMoney', {}).get('currency')
            status = 'active'
            if subscription_data.get('isPremium') and not subscription_data.get('currentPlan'):
                # If user is premium and has a plan then active else inactive otherwise active for free plan
                status = 'inactive'
            
            # Set subscription details
            self.subscription = Subscription(
                id=current_plan.get('id', None),
                name=current_plan.get('title', 'Free'),
                description=current_plan.get('description', None),
                amount=current_plan.get('price', 0),
                amountInCurrency=current_plan.get('priceMoney', {}).get('value', 0),
                currency=currency_used_for_subscription,
                status=status,
                isTrial=subscription_data.get('isOnTrial', False),
                durationInMonths=current_plan.get('periodMonths', None)
            )
            print('subscription details retrieved\n')
        except Exception as error:
            # If subscription details are not available or api throws error then throw error
            print('subscription details retrieval failed\n')
            if error.__dict__.get('response', {}): # If error has response then get error from response and store merchant error
                error = error.__dict__.get('response', {}).json()
            
            print(SUBSCRIPTION_ERROR, ": ", error)
            raise ValueError(SUBSCRIPTION_ERROR)

    async def get_transaction(self):
        # Get transaction details
        print('\ngetting transactions...')
        try:
            response = self.api.fetch(GET_TRANSACTION_API)
            transactions_data = response.json().get('payments', [])

            # Set transaction details
            self.transactions = [
                Transaction(
                    invoiceId=transaction.get('invoiceId', ''),
                    description=transaction.get('purpose', None),
                    date=transaction.get('created', ''),
                    amount=transaction.get('amount', 0),
                    amountInCurrency=transaction.get('amountInCurrency', 0),
                    currency=transaction.get('currency', ''),
                    status=transaction.get('status', ''),
                    refundDate=transaction.get('refunded', None),
                    settledDate=transaction.get('settled', None)
                ) for transaction in transactions_data
            ]
            print('transactions retrieved\n')
        except Exception as error:
            # If transaction details are not available or api throws error then throw error
            print('transactions retrieval failed\n')
            if error.__dict__.get('response', {}): # If error has response then get error from response and store merchant error
                error = error.__dict__.get('response', {}).json()
            
            print(TRANSACTION_ERROR, ": ", error)
            raise ValueError(TRANSACTION_ERROR)
