import python_day24
python_day24.login_info("Test Started")
python_day24.log_error("Element not found")

print(python_day24.max_retries)
from python_day24 import login_info #specific function import
login_info("Test Started")

from python_day24 import max_retries, login_info
login_info("Test Started")
print(max_retries)
print(max_retries*3)

import python_day24 as logger
logger.log_error()
print(max_retries)
print(max_retries*3)
