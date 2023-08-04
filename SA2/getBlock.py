from web3 import Web3
import datetime

def getBlockData(blockNumber):
    apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98' #student will add this
    web3 = Web3(Web3.HTTPProvider(apiUrl))
    apiBlockData = web3.eth.get_block(blockNumber)

    blockData = {}
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()
    transactionTimeStamp = datetime.datetime.fromtimestamp(apiBlockData['timestamp'])
    readableDate = transactionTimeStamp.strftime("%Y-%m-%d %H:%M:%S")
    blockData['timestamp'] = readableDate

    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions
    allTransactions = []
    # First 10 transactions
    for transactionIndex in range(1, 11):
        transaction = {}
        transactionHash = apiBlockData['transactions'][transactionIndex]
        transaction['transactionHash'] = transactionHash.hex()
        # Fetching the transaction details
        transactionDetails = web3.eth.get_transaction(transactionHash)
        transaction['srno'] = transactionIndex
        transaction['receiver'] = transactionDetails['to']
        transaction['sender'] = transactionDetails['from']
        transactionAmount = int(transactionDetails['value']) / 10 ** 18 # Converting to ether
        transaction['amount'] = transactionAmount
        # Adding transaction to the list
        allTransactions.append(transaction)
    blockData['transactions'] = allTransactions
    return blockData

