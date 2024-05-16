# Error Constants
MISSING_NECESSARY_COOKIES_ERROR = "MISSING_NECESSARY_COOKIES_ERROR"
MERCHANT_CONFIG_ERROR = "MERCHANT_CONFIG_ERROR"
UNAUTHORIZED_ERROR = "UNAUTHORIZED_ERROR"
VERIFY_USER_ERROR = "VERIFY_USER_ERROR"
SUBSCRIPTION_ERROR = "SUBSCRIPTION_ERROR"
TRANSACTION_ERROR = "TRANSACTION_ERROR"

# API URL Constants
GET_USER_API = "https://auth.grammarly.com/v3/user"
GET_SUBSCRIPTION_API = "https://subscription.grammarly.com/api/v2/subscription"
GET_TRANSACTION_API = "https://subscription.grammarly.com/api/v2/individual/payment-history"

# Other Constants
ORIGIN_HEADER_URL = "https://account.grammarly.com" # Origin header URL
NECESSARY_COOKIES = ["csrf-token", "grauth"] # Necessary cookies for API requests
