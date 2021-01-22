from web3  import Web3
from tqdm import tqdm

w3 = Web3()

vanity = str(input('starting chars incl 0x: '))

t = tqdm()
while True:
    t.update()

    account = w3.eth.account.create()

    end = len(vanity)
    pub_key = str(account.address).lower()[0:end]

    '''
    important to check this way and not the other, if you do a check for each item of the list performance is
    super fucked
    '''
    if pub_key in vanity:
        print(f'found this account: {account.address, Web3.toHex(account.privateKey)}')
        with open('keys', 'a') as f:
            f.write(account.address + ', ' + Web3.toHex(account.privateKey) + '\n')
        break
    else:
        continue
