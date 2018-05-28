#!/usr/bin/python
# to make the file executable by python

import base64

class CredentialForBearer(object):

    def __init__(self, key, secret): # constructor
        self.key = key
        self.secret = secret

    def get_credential(self):
        decoded_credential = self.get_decoded_credential()
        encoded_credential = self.encode_credential(decoded_credential)
	return encoded_credential
        
    def get_decoded_credential(self):
        return self.key + ":" + self.secret

    def encode_credential(self, string):
        return base64.b64encode(string)
        
if __name__ == "__main__": # if it's executed from console __name__ = true
    bearer = CredentialForBearer("xvz1evFS4wEEPTGEFPHBog", "L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg")
    assert bearer.get_credential() == "eHZ6MWV2RlM0d0VFUFRHRUZQSEJvZzpMOHFxOVBaeVJnNmllS0dFS2hab2xHQzB2SldMdzhpRUo4OERSZHlPZw=="

