from web3  import Web3
from tqdm import tqdm

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()
# fill your list with possible vanity words, do or do not include the 0x
vanity = ['0xb00b135']

# this is just timer
t = tqdm()

while True:
    # update
    t.update()

    # w3 creates account
    account = w3.eth.account.create_with_mnemonic(num_words=12)

    # tell it where you want the vanity part to be
    pub_key = str(account[0].address).lower()[0:9]

    '''
    important to check this way and not the other, if you do a check for each item of the list performance is
    super fucked
    '''

    if pub_key in vanity[0]:
        print(f'found this account: {pub_key, account[1]}')
        break
    else:
        continue