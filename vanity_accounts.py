from web3 import Web3
from tqdm import tqdm

w3 = Web3()

vanity = str( input( 'starting chars incl 0x: ' ) )
w3.eth.account.enable_unaudited_hdwallet_features()

t = tqdm()
while True:
    t.update()

    account = w3.eth.account.create_with_mnemonic()

    end = len( vanity )
    pub_key = str( account[0].address ).lower()[0:end]

    '''
    important to check this way and not the other, if you do a check for each item of the list performance is
    super fucked
    '''
    if pub_key in vanity:
        result = f' found this account: {account[0].address, account[1]}'
        print( result )

        with open( 'keys', 'a' ) as f:
            f.write( result )
        break
    else:
        continue
