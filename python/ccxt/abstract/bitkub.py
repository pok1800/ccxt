from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_market = publicGetApiMarketSymbols = Entry('market', 'public', 'GET', {'cost': 1})
    public_get_ticker = publicGetApiMarketTicker = Entry('ticker', 'public', 'GET', {'cost': 1})
    public_get_order_book = publicGetApiMarketBooks = Entry('order_book', 'public', 'GET', {'cost': 1})
    public_get_trade = publicGetApiMarketTrades = Entry('trade', 'public', 'GET', {'cost': 1})
    public_get_candle = publicGetCandle = Entry('candle', 'public', 'GET', {'cost': 1})
    private_post_new_order = privatePostMarketMyOpenOrders = Entry('new_order', 'private', 'POST', {'cost': 2})
    private_post_cancel_order = privatePostApiMarketV2CancelOrder = Entry('cancel_order', 'private', 'POST', {'cost': 1})
    #private_post_withdrawal = privatePostWithdrawal = Entry('withdrawal', 'private', 'POST', {'cost': 2})
    private_get_balance = privatePostApiMarketBalances = Entry('balance', 'private', 'GET', {'cost': 1})
    #private_get_order = privateGetOrder = Entry('order', 'private', 'GET', {'cost': 1})
    #private_get_open_order = privateGetOpenOrder = Entry('open_order', 'private', 'GET', {'cost': 1})
    private_get_order_history = privatePostApiMarketMyOrderHistory = Entry('order_history', 'private', 'GET', {'cost': 1})
    #private_get_trade_history = privateGetTradeHistory = Entry('trade_history', 'private', 'GET', {'cost': 1})
    private_get_deposit_address = privatePostApiCryptoAddresses = Entry('deposit_address', 'private', 'GET', {'cost': 1})
    #private_get_transfer_payment = privateGetTransferPayment = Entry('transfer/payment', 'private', 'GET', {'cost': 1})
    #accounts_post_token = accountsPostToken = Entry('token', 'accounts', 'POST', {'cost': 1})
