from classes.merchant import MERCHANT
from common.function import print_table
import asyncio
from classes.api import API

async def main():
    # main function to run the merchant class
    try:
        print('\nmerchant class executing...')
        merchant = MERCHANT()  # Initialize merchant instance with cookies and configure default headers for API

        await merchant.verify_user() # Authenticate user
        print('USER DETAILS TABLE')
        print_table(merchant.user.__dict__, is_dict=True)

        await merchant.get_subscription() # Get subscription details
        print('SUBSCRIPTION DETAILS TABLE')
        print_table(merchant.subscription.__dict__, is_dict=True)

        await merchant.get_transaction() # Get transaction details
        if merchant.transactions:
            print('TRANSACTION DETAILS TABLE')
            print_table([transaction.__dict__ for transaction in merchant.transactions])
        else:
            print('No transaction found')

        print('\nmerchant class executed successfully\n\n')
    except Exception as error:
        print('error:', error)

asyncio.run(main())
