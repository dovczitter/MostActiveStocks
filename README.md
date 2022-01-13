# MostActiveStocks
Presents various sources of current most active stocks, python demo, windows local host server.
Only one source file, 'mostactivestocks.py'.
Impliments 'webdriver', copy 'distexe/chromedriver.exe' in the running path.
MostActiveStocks_dist.zip package was created by 'python setup.py py2exe',
see setup.py for the included files.
The dist.zip contains a complete package, extract the 'dist' folder, run 'mostactivestocks.exe' in the
extracted folder. starts up a server listening on localhost:8080.

dist\mostactivestocks.exe
Server started localhost:8080

Browse to 'http://localhost:8080/mostactivestocks', read the notes for the how to.
The top line is a series of links which generate the presented tables, sourced for the 'ReutersMostActive'
website, added value is the per market symbol link to its 'Yahoo Finance' website, browser back arrow.
