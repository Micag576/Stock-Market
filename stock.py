class Stock:
    def __init__(self, name,ticker,sector,orginalPrice,numOfShares):
        self.name = name
        self.ticker = ticker
        self.sector = sector
        self.orginalPrice = orginalPrice
        self.numOfShares = numOfShares
        self.currentPrice = orginalPrice
        


    def updatePrice(self,updatedValue):
        self.currentPrice = updatedValue
        
