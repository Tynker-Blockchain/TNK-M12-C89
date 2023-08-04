import hashlib
import json
from time import time

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGensisBlock()
        currentBlock.previousHash = self.chain[-1].currentHash
        currentBlock.currentHash = currentBlock.calculateHash()
        self.chain.append(currentBlock)
    
    def createGensisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        
        previousBlockHash = previousBlock.calculateHash()        
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        return True
        
class Block:
    # SA2: Remove recieving transaction parameter
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        # SA2: Replace transaction with empty transactions list 
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp

        # SA2: Replace transaction with transactions
        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions)
        return generateHash(blockString)

    # SA2: Add transaction function that receives transaction as parameter
    def addTransaction(self, transaction):
        # SA2: Check if transaction exits
        if transaction:
            # SA2: Append the transaction to self.transactions
            self.transactions.append(transaction)
            # SA2: Calculate hash for the block and set self.currentHash
            self.currentHash = self.calculateHash()