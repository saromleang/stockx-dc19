# stockx-dc19
[StockX Data Challenge 2019 - Lunar Hype 3rd Place](https://stockx.com/news/2019-data-contest-winner/)

## StockX-Data-Contest-2019-3.xlsx
Contains a slightly modified Excel sheet of the original data from StockX.  I added a couple of new columns that were caculated from the existing data:
  *  Days Since (days since the release for the particular sale - this column never got utilized)
  *  Profit (self-explanatory)

## StockX-Data-Contest-2019-3.csv
Contains a CSV export of the Excel data.  The CSV file will be post-processed by the Python script **process-moon-shift.py**

## process-moon-shift.py
  *  [Setup the definition of the moonphases](https://github.com/saromleang/stockx-dc19/blob/master/process-moon-shift.py#L75-L86)
  *  [Setup geolocation for moonphase calculations: StockX headquarter](https://github.com/saromleang/stockx-dc19/blob/master/process-moon-shift.py#L89)
  *  [For each row determine the moonphase and generate CSV](https://github.com/saromleang/stockx-dc19/blob/master/process-moon-shift.py#L94-L107)
  *  [Break down info by states and generate CSV](https://github.com/saromleang/stockx-dc19/blob/master/process-moon-shift.py#L109-L129)
  *  [Accumulate data along moonphase and generate CSV](https://github.com/saromleang/stockx-dc19/blob/master/process-moon-shift.py#L131-L150)
  *  [CSVs were import into Tableau](https://github.com/saromleang/stockx-dc19/blob/master/Moonphase.twb)
  *  [Generated dashboard](https://github.com/saromleang/stockx-dc19/blob/master/Dashboard%201.png)

![alt text](https://github.com/saromleang/stockx-dc19/blob/master/Dashboard%201.png)
