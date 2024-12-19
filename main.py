from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

portfolio =[]

def addStock(name,ticker,sector,numOfShares):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stock(name,ticker,sector,price,numOfShares)
    portfolio.append(newStock)

def updatePrices():
    for stock in portfolio:
        price = stock_info.get_live_price(stock.ticker)
        stock.currentPrice = round(float(price),2)
        


def viewPortfolio():
    print("{0:20s}{1:10s}{2:25s}{3:25s}{4:6s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    count = 1
    for stock in portfolio:
        gain_loss = round((stock.currentPrice - stock.orginalPrice) * stock.numOfShares,2)
        print(f"{count}, {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{25}}${stock.currentPrice:{8}}{stock.numOfShares:{18}}{gain_loss:{10}}")
        count += 1

def searchBySector(sector):
    print(f"\nSearching for stocks in the {sector} sector...")
    print("{0:20s}{1:10s}{2:25s}{3:25s}{4:6s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    count = 1
    found = False
    for stock in portfolio:
        if stock.sector.lower() == sector.lower():  # Case insensitive matching
            print(f"{count}, {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{25}}${stock.currentPrice:{8}}{stock.numOfShares:{6}}")
            count += 1
            found = True
    if not found:
        print(f"No stocks found in the {sector} sector.")

def mainMenu():
    print("Main Menu")
    print("1. Add a new stock to the portfolio")
    print("2. Update Stock Portfolio")
    print("3. Search By Sector")
    print("4. View Portfolio")
    print("5. Exit Program")

print("Welcome to My Stock Portfolio")

status = True

while(status):
    mainMenu()
    choice = input("Select from the following options")
    if choice == "1":
        name = input("Enter the Name of the Stock: ")
        ticker = input("Enter the stock ticker name: ")
        tick = yf.Ticker(ticker).info
        sector=tick['industry']
        numOfShares =  int(input("Enter number of stock shares to buy: "))
        addStock(name,ticker,sector,numOfShares)
    elif choice == "2":
        updatePrices()
        viewPortfolio()
    elif choice == "3":
        sector = input("Enter the sector to search for: ")
        searchBySector(sector)
    elif choice == "4":
        viewPortfolio()
    elif choice == "5":
        status = False
print("Thanks for using my stock portfolio program. Have a nice day!")