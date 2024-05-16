from typing import Optional, Dict

# Merchant Type Classes
class Transaction:
    # Transaction class to store transaction details
    def __init__(
        self,
        invoiceId: str,
        description: Optional[str], # None for no description
        date: str,
        amount: int, # 0 for free subscription
        amountInCurrency: int,
        currency: str,
        status: str,
        refundDate: Optional[str], # None for no refund
        settledDate: Optional[str] # None for not settled
    ):
        self.invoiceId = invoiceId
        self.description = description
        self.date = date
        self.amount = amount
        self.amountInCurrency = amountInCurrency
        self.currency = currency
        self.status = status
        self.refundDate = refundDate
        self.settledDate = settledDate

class Subscription:
    # Subscription class to store subscription details
    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str],
        amount: int, # 0 for free subscription
        amountInCurrency: int, # 0 for free subscription
        currency: Optional[str], # None for free subscription
        status: Optional[str], # None for free subscription
        isTrial: bool, # True if subscription is a trial
        durationInMonths: Optional[int] # None for free subscription
    ):
        self.id = id
        self.name = name
        self.description = description
        self.amount = amount
        self.amountInCurrency = amountInCurrency
        self.currency = currency
        self.status = status
        self.isTrial = isTrial
        self.durationInMonths = durationInMonths

class User:
    # User class to store user details
    def __init__(
        self,
        id: str,
        email: str,
        name: str,
        isVerified: bool, # True if user is verified
        isFree: bool, # True if user is using free subscription
        loginType: Optional[str] = None, # None for no login type
        isDisabled: Optional[bool] = None, #True if user account is disabled
    ):
        self.id = id
        self.email = email
        self.name = name
        self.isVerified = isVerified
        self.loginType = loginType
        self.isDisabled = isDisabled
        self.isFree = isFree

# API Type Classes
class Cookie:
    # Cookie class to store cookie details
    def __init__(
        self,
        name: str,
        value: str,
        domain: Optional[str] = None,
        path: Optional[str] = None,
        expires: Optional[str] = None,
        expirationDate: Optional[int] = None, # some cookies extractor use expirationDate instead of expires
        secure: Optional[bool] = None
    ):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.expires = expires
        self.expirationDate = expirationDate
        self.secure = secure

CustomHeaders = Dict[str, str]
