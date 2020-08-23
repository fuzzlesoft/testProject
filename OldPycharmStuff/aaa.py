import yfinance as yf
import scipy.optimize

###################################################################################
#############################where the classes hangout#############################
class Equity():
    def __init__(self,ticker):
        self.ticker=yf.Ticker(ticker)
        self.ticker_hist=self.ticker.history(period="1y")
        self.ticker_open=[x for x in self.ticker_hist["Open"]]
        self.ticker_closed=[x for x in self.ticker_hist["Close"]]
        self.ticker_volume=[x for x in self.ticker_hist["Volume"]]
        #self.ticker_date=[x for x in self.ticker_hist["Date"]]
        #self.ticker_actions=self.ticker_actions() #i don't know if this one is right
        #ok so since I don't need to do analysis here year... these aren't actually relevent
        """
        i just need to build something that simulates trading, I don't need the actual data analysis
        yet
        """

        '''
        self.meanOpen=self.ticker_open.mean()
        self.meanClosed=self.ticker_closed.mean()
        self.varOpen=self.ticker_open.var()
        self.varClosed=self.ticker_closed.var()
        self.meanVolume=self.ticker_volume.mean()
        self.varVolume=self.ticker_volume.var()
        '''
class account():
    #account really just has the money and the function to change the value of the account
    def __init__(self,startingMoney):
        self.money=startingMoney
    def changeMoney(self,change):
        self.money=self.money+change


class strategy():
    #equity list is a list of equity objects with return histories and volumes


    def __init__(self, account, equity_list):
        self.strategyList=[]
        self.account=account
        for item in equity_list:
            tempStock=Equity(item)
            self.strategyList.append(tempStock)

    def testStrategySPY(self):
        stocklistLen=0
        for stockS in self.strategyList:
            stocklistLen=len(stockS.ticker_open)
        for stockS in self.strategyList:
            stocklistLen2=len(stockS.ticker_open)
            if stocklistLen!=stocklistLen2:
                print("lenghts arent the same")
            else:
                for day in range(len(stocklistLen)):
                    #short spy from the day
                    #long spy from the night
                    None


        None


##################################################################################

equity_list=[]#where i store class instances of the equities
#interested_tickers=["SPY", "SPXL","TLT"] #list of stocks I want to compare
test_tickers=["SPY", "SPXL"]

"""
for item in interested_tickers:
    cls=Equity(item)
    equity_list.append(cls)
"""
accountA=account(1)

testStrat=strategy(accountA,test_tickers)
testStrat.testStrategySPY()