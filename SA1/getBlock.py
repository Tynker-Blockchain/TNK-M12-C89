from web3 import Web3

def getBlockData(blockNumber):
    # API setup
    apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98' #student will add this
    web3 = Web3(Web3.HTTPProvider(apiUrl))
    # Fetching the block data from API
    apiBlockData = web3.eth.get_block(blockNumber)
    blockData = {}
    # Storing basic details of block
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()

    # Storing number of transaction details
    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions
  
    return blockData

