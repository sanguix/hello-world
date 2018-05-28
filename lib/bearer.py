#!/usr/bin/python
# to make the file executable by python

import base64

class Bearer(object):

    def __init__(self, key, secret): # constructor
        self.key = key
        self.secret = secret

    def get_token(self):
        decoded_token = self.get_decoded_token()
        encoded_token = self.encode_token(decoded_token)
	return encoded_token
        
    def get_decoded_token(self):
        return self.key + ":" + self.secret

    def encode_token(self, string):
        return base64.b64encode(string)
        
if __name__ == "__main__": # if it's executed from console __name__ = true
    bearer = Bearer("xvz1evFS4wEEPTGEFPHBog", "L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg")
    assert bearer.get_token() == "eHZ6MWV2RlM0d0VFUFRHRUZQSEJvZzpMOHFxOVBaeVJnNmllS0dFS2hab2xHQzB2SldMdzhpRUo4OERSZHlPZw=="

