# MostActiveStocks
- Presents various sources of current most active Reuters stocks, python demo.
- Implements selenium headless Chrome driver as a windows cmd server. 
- Only one source file, 'mostactivestocks.py', no css files due to webdriver_manager.chrome restriction.
- To run windows cmd server, unzip the exe\dist.zip package, created by 'python setup.py py2exe', see setup.py for the included files.
- Run 'mostactivestocks.exe' at a cmd prompt, starts the server listening on localhost:8080, use -host and -port switches to override.
- Client browser to 'http://localhost:8080/mostactivestocks', read the notes for the how to.
- The top line is a series of links which generate the presented tables, sourced for the 'ReutersMostActive'
website, added value is the per market symbol link to its 'Yahoo Finance' website, browser back arrow.
- SYMBOL field queries any stock to "Yahoo Finance",  
- Investing.com link provides more realtme updates, news etc.

========= Notes =========

Links : `Nyse | Amex | Nasdaq | NasdaqPost | Ftse` query Reuters for the `Most Active Companies` info.
ReutersMostActives to view data source, note the mid page `INDEX` list.
NYSE Most Actives -> HOME, Nyse default.
AMEX Most Actives -> Amex
NASDAQ Most Actives -> both Nasdaq and NasdaqPost
FTSE Most Actives -> Ftse
For more Reuters data, use ReutersMostActives, then INDEX to `Price Gainers (%)`,`Price Losers (%)`,`Dollar Gainers`, `Dollar Losers`
Investing.com to view other most active USA and international stocks. Tab to 'Markets->Stocks->Most Active'
Each Symbol element links to its "Yahoo Finance" site providing complete symbol data, browser back arrow gets back to here.
Note lower lefthand browser window shows the url.
Nasdaq and NasdaqPost both result in the same table data, NasdaqPost links to the native Nasdaq site for more direct info, again back arrow to return here.
SYMBOL textbox provides any symbol query to "Yahoo Finance".
[Extensions may not be vaild on "Yahoo Finance"] Example, Nyse base symbol JCP.N enter `JCP`, include the `.L` extension for London, ie `LLOY.L`
[Version: 1.2]
