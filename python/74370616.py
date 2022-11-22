# You cannot run shell commands from a python script.
# This is the right way to do it. You can also use the subprocess module to do it.

import os

# In Windows
os.system("py -m pip install boto3")

#

# Although, it's not recommended installing packages inside your code.
# You can use a requirements.txt file. Then you just need to run this command once in your terminal:
# pip install -r requirements.txt


# https://learnpython.com/blog/python-requirements-file/
