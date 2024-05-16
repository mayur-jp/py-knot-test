import requests
from typing import List, Dict, Optional

from common.structure import Cookie, CustomHeaders
from common.constant import MISSING_NECESSARY_COOKIES_ERROR

class API:
    def __init__(self):
        # Initialize API instance and set default configurations
        self.session = requests.Session() # Initialize session
        self.cookies = []
        self.default_headers = {}

    def interceptors_request(self, config: Dict[str, any]) -> Dict[str, any]:
        # Interceptor to modify request configuration
        if self.cookies:
            # Set cookies in request headers
            config['headers']['Cookie'] = ';'.join([f"{cookie['name']}={cookie['value']}" for cookie in self.cookies])
        return config

    def interceptors_response(self, response: requests.Response) -> requests.Response:
        # Interceptor to modify response
        for cookieJar in response.cookies:
            cookie = Cookie(
                name=cookieJar.name,
                value=cookieJar.value,
                domain=cookieJar.domain,
                path=cookieJar.path,
                expires=cookieJar.expires,
                secure=cookieJar.secure
            )
            self.cookies.append(cookie.__dict__) # Append cookie in cookies list
        return response

    def interceptors_error(self, error: requests.RequestException) -> requests.RequestException:
        # Interceptor to modify error
        return error

    def set_default_headers(self, headers: CustomHeaders) -> None:
        # Set default headers
        self.default_headers = headers

    def import_cookies(self, cookies: List[Cookie], necessary_cookies: List[str] = []) -> None:
        # Import cookies in API instance
        self.cookies = cookies # Set cookies
        if necessary_cookies:
            # If necessary cookies are provided, check if all necessary cookies are present
            self.check_necessary_cookies(necessary_cookies)

    def check_necessary_cookies(self, necessary_cookies: List[str]) -> None:
        # Check necessary cookies
        print('\nchecking necessary cookies...')
        missing_cookies = [cookie for cookie in necessary_cookies if not self.get_cookie(cookie)] # Get missing cookies
        if missing_cookies:
            # If missing cookies are found, log the error and raise ValueError
            print(MISSING_NECESSARY_COOKIES_ERROR + ": ", missing_cookies)
            raise ValueError(MISSING_NECESSARY_COOKIES_ERROR)
        print('necessary cookies are present\n')

    def get_cookie(self, name: str) -> Optional[Cookie]:
        # Get cookie by name
        return next((cookie for cookie in self.cookies if cookie["name"] == name), None)

    def fetch(self, url: str, config: Dict[str, any] = {'method': 'get', 'data': {}, 'headers': {}}) -> requests.Response:
        # Fetch API
        config = self.interceptors_request(config) # Call request interceptor
        headers = {**self.default_headers, **config['headers']} # Merge default headers and request headers
        try:
            response = self.session.request(method=config['method'], url=url, data=config['data'], headers=headers) # Make request
            response.raise_for_status() # Raise error if response status code is not 200
            return self.interceptors_response(response) # Call response interceptor and return response
        except requests.RequestException as e:
            # If request failed, call error interceptor and raise error
            raise self.interceptors_error(e)
