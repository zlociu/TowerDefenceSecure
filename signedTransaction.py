from hashlib import sha256 
import json

class SignedTransaction:
    def __init__(self, transaction, sign, address):
        self.transaction = transaction
        self.sign = sign
        self.address = address

    def signedTransactionJSON(self):
        trString = json.dumps(self.__dict__, sort_keys=True)
        return trString
    
    def compute_hash(self):
        tr_string = self.signedTransactionJSON()
        return sha256(tr_string.encode()).hexdigest()

    