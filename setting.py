'''

MODULE :

1. web3_checker
2. debank checker
3. exchange withdraw : вывод с биржи
4. okx withdraw
5. transfer
6. 1inch_swap
7. orbiter finance
8. woofi_bridge
9. woofi_swap

'''

# ========================
MODULE = 1 # выбираем модуль от 1 до 9
# ========================

IS_SLEEP        = True # True / False. True если нужно поставить sleep между кошельками
# от скольки до скольки спим между кошельками (секунды) :
SLEEP_FROM      = 50 
SLEEP_TO        = 100

# нужно ли рандомизировать (перемешивать) кошельки. True = да. False = нет
RANDOM_WALLETS  = False # True / False

RETRY = 0 # кол-во попыток при ошибках / фейлах

# настройка отправки результатов в тг бота
TG_BOT_SEND = True # True / False. Если True, тогда будет отправлять результаты
TG_TOKEN    = '' # токен от тг-бота
TG_ID       = 0 # id твоего телеграмма

# апи ключи от бирж. если биржей не пользуешься, можно не вставлять
CEX_KEYS = {
    'binance'   : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'mexc'      : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'kucoin'    : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password'},
    'huobi'     : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'bybit'     : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'okx'       : {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password'},
}

def value_web3_checker():

    '''
    чекер монет через web3
    chains : ethereum | optimism | bsc | polygon | arbitrum | avalanche | fantom | nova | zksync
    '''

    datas = {
        'bsc': [
            '', # BNB
            '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d', # USDC
            '0x55d398326f99059ff775485246999027b3197955', # USDT
            ],
        'arbitrum': [
            '', # ETH
            '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', # USDT
            '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8', # USDC
            ],
        'optimism': [
            '', # ETH
            '0x7f5c764cbc14f9669b88837ca1490cca17c31607', # USDC
            # '0x4200000000000000000000000000000000000042', # OP
            '0x94b008aa00579c1307b0ef2c499ad98a8ce58e58', # USDT
            ],
        # 'polygon': [
        #     '', # MATIC
        #     ],
        # 'avalanche': [
        #     '', # AVAX
        #     ],
        # 'ethereum': [
        #     '', # ETH
        #     '0xdac17f958d2ee523a2206206994597c13d831ec7', # USDT
        #     ],
        # 'zksync': [
        #     '', # ETH
        #     ],
        # 'nova': [
        #     '', # ETH
        #     ],
        # 'fantom': [
        #     '', # FTM
        #     ],
    }

    min_balance = {
        'chain'     : 'arbitrum',
        'coin'      : 'ETH',
        'amount'    : 0.005 # если баланс меньше этого числа, кошелек будет выделен
    }
    
    file_name   = 'web3_balances' # имя файла в который будем сохранять данные. создается сам
    
    return datas, min_balance, file_name

def value_debank():

    '''
    чекер баланса через debank, смотрит все сети, протоколы и нфт
    '''

    # какие модули включены. если какой-то модуль не нужен, закомментируй (#) его. модуль nft самый долгий, по ненадобности лучше его отключать
    modules = [
        'token', # смотрит монеты
        # 'nft', # смотрит нфт
        # 'protocol' # смотрит протоколы
    ]

    # в каких сетях смотрим нфт. если какая-то сеть не нужна, закомментируй (#) ее
    nft_chains = [
        'op', 
        # 'eth', 
        'arb', 
        # 'matic', 
        # 'bsc'
        ]

    check_min_value     = 0 # $. если баланс монеты / протокола будет меньше этого числа, монета / протокол не будут записаны в файл
    check_chain         = '' # в какой сети ищем монету (отдельно выделит ее баланс)
    check_coin          = '' # какую монету ищем (отдельно выделит ее баланс)

    
    file_name = 'debank' # имя файла в который будем сохранять данные. создается сам
    
    return file_name, check_min_value, check_chain, check_coin, modules, nft_chains


def value_exchange():

    '''
    withdraw coins from exchange.
    exchanges : binance | bybit | kucoin | mexc | huobi

    chains : 
    - binance   : ETH | BEP20 | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT
    - bybit     : ...
    - kucoin    : ...
    - mexc      : ...
    - huobi     : ...
    '''

    exchange    = 'binance' # запиши сюда биржу

    chain       = 'BEP20' # в какой сети выводим
    symbol      = 'USDT'  # какой токен выводим

    amount_from = 13 # от какого кол-ва монет выводим
    amount_to   = 20 # до какого кол-ва монет выводим


    return exchange, chain, symbol, amount_from, amount_to

def value_okx():

    '''
    выводит только с funding, есть вывод с суб-аккаунтов

    OKX
    BSC
    ERC20
    TRC20
    Polygon
    Avalanche C-Chain
    Avalanche X-Chain
    Arbitrum one
    Optimism
    Fantom
    '''

    chain       = 'Arbitrum one' # с какой сети выводить
    symbol      = 'ETH' # какую монету выводить

    amount_from = 0.1 # выводим от
    amount_to   = 0.2 # выводим до

    FEE         = 0.0001 # комиссия на вывод
    SUB_ACC     = True # True / False. True если нужно выводить с суб-аккаунтов

    API_KEY     = CEX_KEYS['okx']['api_key']
    API_SECRET  = CEX_KEYS['okx']['api_secret']
    PASSWORD    = CEX_KEYS['okx']['password']

    return chain, symbol, amount_from, amount_to, API_KEY, API_SECRET, PASSWORD, FEE, SUB_ACC

def value_transfer():

    '''
    вывод (трансфер) монет с кошельков
    chains : ethereum | optimism | bsc | polygon | arbitrum | avalanche | fantom | nova | zksync
    '''

    chain                = 'arbitrum'   # в какой сети выводить
    token_address        = ''           # пусто если нативный токен сети

    amount_from          = 0.007            # от какого кол-ва монет делаем трансфер
    amount_to            = 0.007            # до какого кол-ва монет делаем трансфер  

    transfer_all_balance = True        # True / False. если True, тогда выводим весь баланс
    min_amount_transfer  = 0.0005            # если баланс будет меньше этого числа, выводить не будет
    keep_value_from      = 0.001            # от скольки монет оставляем на кошельке (работает только при : transfer_all_balance = True)
    keep_value_to        = 0.0015            # до скольки монет оставляем на кошельке (работает только при : transfer_all_balance = True)
    
    return chain, amount_from, amount_to, transfer_all_balance, min_amount_transfer, keep_value_from, keep_value_to, token_address

def value_1inch_swap():

    '''
    свапы на 1inch
    chains : ethereum | optimism | bsc | polygon | arbitrum | avalanche | fantom | zksync
    '''

    chain               = 'avalanche' # в какой сети свапаем
    from_token_address  = '' # пусто если нативный токен сети
    to_token_address    = '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E' # пусто если нативный токен сети

    amount_from         = 0.001    # от какого кол-ва монет свапаем
    amount_to           = 0.002    # до какого кол-ва монет свапаем

    swap_all_balance    = False      # True / False. если True, тогда свапаем весь баланс
    min_amount_swap     = 0         # если баланс будет меньше этого числа, свапать не будет
    keep_value_from     = 0         # от скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)
    keep_value_to       = 0         # до скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)

    slippage = 3 # слиппейдж, дефолт от 1 до 3

    divider_zksync = 4 # на сколько делим gasLimit в zksync : советую ставить 3-4. исполняется только на zksync

    return chain, swap_all_balance, min_amount_swap, keep_value_from, keep_value_to, amount_from, amount_to, from_token_address, to_token_address, slippage, divider_zksync

def value_orbiter():

    '''
    бридж нативных токенов через https://www.orbiter.finance/
    chains : zksync | polygon | ethereum | bsc | arbitrum | optimism | polygon_zkevm | nova | starknet
    минимальный бридж : 0.005
    '''

    from_chain          = 'arbitrum'    # с какой сети 
    to_chain            = 'bsc'      # в какую сеть 

    amount_from         = 0.006 # от какого кол-ва монет делаем бридж
    amount_to           = 0.0065 # до какого кол-ва монет делаем бридж

    bridge_all_balance  = True         # True / False. если True, тогда бриджим весь баланс
    min_amount_bridge   = 0          # если баланс будет меньше этого числа, выводить не будет
    keep_value_from     = 0.001             # от скольки монет оставляем на кошельке (работает только при : bridge_all_balance = True)
    keep_value_to       = 0.002             # до скольки монет оставляем на кошельке (работает только при : bridge_all_balance = True)

    return from_chain, to_chain, bridge_all_balance, amount_from, amount_to, min_amount_bridge, keep_value_from, keep_value_to

def value_woofi_bridge():

    '''
    бридж на https://fi.woo.org/ (бриджи идут через layerzero)
    chains : avalanche | polygon | ethereum | bsc | arbitrum | optimism | fantom
    '''
    
    from_chain          = 'arbitrum'
    to_chain            = 'polygon'  

    from_token          = '' # пусто если нативный токен сети
    to_token            = '' # пусто если нативный токен сети

    amount_from         = 0.0001       # от какого кол-ва from_token свапаем
    amount_to           = 0.0001       # до какого кол-ва from_token свапаем

    swap_all_balance    = False         # True / False. если True, тогда свапаем весь баланс
    min_amount_swap     = 0             # если баланс будет меньше этого числа, свапать не будет
    keep_value_from     = 0          # от скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)
    keep_value_to       = 0           # до скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)

    
    return from_chain, to_chain, from_token, to_token, swap_all_balance, amount_from, amount_to, min_amount_swap, keep_value_from, keep_value_to

def value_woofi_swap():

    '''
    свап на https://fi.woo.org/ 
    chains : avalanche | polygon | ethereum | bsc | arbitrum | optimism | fantom
    '''
    
    chain = 'bsc'

    from_token          = '' # пусто если нативный токен сети
    to_token            = '' # пусто если нативный токен сети

    amount_from         = 0.0001       # от какого кол-ва from_token свапаем
    amount_to           = 0.0001       # до какого кол-ва from_token свапаем

    swap_all_balance    = False         # True / False. если True, тогда свапаем весь баланс
    min_amount_swap     = 0             # если баланс будет меньше этого числа, свапать не будет
    keep_value_from     = 0          # от скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)
    keep_value_to       = 0           # до скольки монет оставляем на кошельке (работает только при : swap_all_balance = True)

    
    return chain, from_token, to_token, swap_all_balance, amount_from, amount_to, min_amount_swap, keep_value_from, keep_value_to



