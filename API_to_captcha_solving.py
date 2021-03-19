#  Universal API to captcha solving services

# PyPi:  https://pypi.org/project/captcha-solver/
# pip install captcha-solver

#  Service website is https://2captcha.com?from=3019071

from captcha_solver import CaptchaSolver


solver = CaptchaSolver('twocaptcha', api_key='2captcha.com API HERE')
raw_data = open('captcha.png', 'rb').read()
print(solver.solve_captcha(raw_data))

