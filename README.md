# MostActiveStocks
- Presents various sources of current most active stocks, python demo, windows local host server.
- Only one source file, 'mostactivestocks.py'.
- To run windows cmd server, unzip the exe\dist.zip package, then run 'mostactivestocks.exe' at a cmd prompt
starts up a server listening on localhost:8080, use -host and -port switches to override.
The 'exe\dist.zip' package was created by 'python setup.py py2exe', see setup.py for the included files.
Browse to 'http://localhost:8080/mostactivestocks', read the notes for the how to.
- The top line is a series of links which generate the presented tables, sourced for the 'ReutersMostActive'
website, added value is the per market symbol link to its 'Yahoo Finance' website, browser back arrow.
- 'SYMBOL' field queries "Yahoo Finance",  
- The 'Investing.com' link provides more realtme updates, news etc.

Notes:

Links : `Nyse | Amex | Nasdaq | NasdaqPost | Ftse` query Reuters for the `Most Active Companies` info.
ReutersMostActives to view data source, note the mid page `INDEX` list.
NYSE Most Actives -> Nyse
AMEX Most Actives -> Amex
NASDAQ Most Actives -> both Nasdaq and NasdaqPost
FTSE Most Actives -> Ftse
For more Reuters data, use ReutersMostActives, then INDEX to `Price Gainers (%)`,`Price Losers (%)`,`Dollar Gainers`, `Dollar Losers`
Investing.com to view other most active USA and international stocks. See Markets->Stocks->Most Active
Each Symbol element links to its "Yahoo Finance" site providing complete symbol data, browser back arrow gets back to here.
Note lower lefthand browser window shows the url.
Nasdaq and NasdaqPost both result in the same table data, NasdaqPost links to the native Nasdaq site for more direct info, again back arrow to return here.
SYMBOL textbox provides any symbol query to "Yahoo Finance".
[Extensions may not be vaild on "Yahoo Finance"] Example, Nyse base symbol JCP.N enter `JCP`, include the `.L` extension for London, ie `LLOY.L`
[Version: 1.0]
