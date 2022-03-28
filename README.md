# MostActiveStocks
presents various sources of current most active stocks, python demo, windows local host server.
MostActiveStocks presents Reuters market data, most active stocks, as scraped from their website, resultant tables are per-symbol linked to Yahoo Finance website.

Currently only served by a local hosted windows python server: 'python weserver.py'
Support files:
	webserver.json : host and port configuration
	webserver.csv : market to Reuters website mapping

General useage:

`Nyse | Amex | Nasdaq | NasdaqPost | Ftse` query Reuters for the `Most Active Companies` info.
ReutersMostActives to view data source, note the mid page `INDEX` list.
NYSE Most Actives -> HOME, Nyse default
AMEX Most Actives -> Amex
NASDAQ Most Actives -> both Nasdaq and NasdaqPost
FTSE Most Actives -> Ftse
For more Reuters data, use ReutersMostActives, then INDEX to `Price Gainers (%)`,`Price Losers (%)`,`Dollar Gainers`, `Dollar Losers` 
Investing.com to view other most active USA and international stocks. See Markets->Stocks->Most Active
Each Symbol element links to its "Yahoo Finance" site providing complete symbol data, browser back arrow gets back to here.
Note lower lefthand browser window shows the url.
Nasdaq and NasdaqPost both result in the same table data, NasdaqPost links to the native Nasdaq site for more direct info, again back arrow to return here. 
SYMBOL textbox provides any symbol query to "Yahoo Finance"
Extensions may not be vaild on "Yahoo Finance"] Example, Nyse base symbol JCP.N enter `JCP`, include the `.L` extension for London, ie `LLOY.L` 
