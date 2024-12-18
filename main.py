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
    print("{0:20s}{1:10s}{2:25s}{3:25s}{4:6s}{5:10s}".format("Name of Stock","Ticker","Industry","Price","QTY","Gain/Loss"))
    count = 1
    for stock in portfolio:
        #implement the gain/loss algorithim
        print(f"{count}, {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{25}}${stock.currentPrice:{8}}{stock.numOfShares:{6}}")
        count+=1

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
        pass 
    elif choice == "4":
        viewPortfolio()
    elif choice == "5":
        status = False
print("Thanks for using my stock portfolio program. Have a nice day!")