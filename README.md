# lifetimebrands-productscrape
Scrape item information for lifetime brands products on Walmart web site

Creates a CSV file with the original product file columns as well as a new
column that indicates whether the product was out of stock or not. The output
file is sorted according to the OOS flag (0=in stock, 1=out of stock, 2=in
stock status could not be determined) and then the product key.

## Set up local environment
- Install python 3
- Navigate to root folder of the repository
- Execute `pip install -r requirements.txt`

## Run tests
- Navigate to root folder of the repository
- Execute `pytest`

## Update product file:
- Update the default input file in location /src/python/resources/productlist.csv
  or create a new file and point to it using the runner.py input argument -i

The product file is assumed to be a two column CSV file with no header row.
Column 1: A product key. This value is only used to identify a product.
Column 2: A URL to a Walmart web site product page. This should work when you paste
          it into your browser.

## Learn how to run script:
- Execute python [path-to-script]/runner.py -h

## Run script
- Execute python [path-to-script]/runner.py [options]
