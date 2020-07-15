"""Scrape a defined set of product web pages from the Walmart web site"""

import re
import logging
import os
import sys
import argparse

import pandas as pd
import requests

logging.basicConfig(level=logging.WARN)
_logger = logging.getLogger(__name__)

def read_product_table_from_file(input_file_str_or_buffer) -> pd.DataFrame:
    return pd.read_csv(input_file_str_or_buffer,
                       header=None,
                       names=['product_key', 'url'])
                      
def write_product_table_to_file(output_file_str_or_buffer, product_pdf: pd.DataFrame) -> None:
    (product_pdf.sort_values(['oos_flag', 'product_key'], ascending=[False, True])
                .to_csv(output_file_str_or_buffer, index=False)) 

def scrape_web_page_text(url: str) -> str:
    page = requests.get(url)
    return page.text

def check_web_page_text_for_in_stock_indicator(web_page_text: str) -> bool:
    """Returns true if an in stock indicator is found in web page text"""
    return (True if (None != re.search(r'"availabilityStatus":"IN_STOCK"',
        web_page_text, flags=re.I)) else False)

def determine_product_in_stock_status(url: str) -> int:
    """Determines if a product is shown as in-stock on walmart.com
    
    Returns:
        An integer that depends on what we find in the scraped web text.
        0 = The item appears to be in stock
        1 = the item appears to be out of stock
        2 = The in-stock status could not be determined. It's possible
            the code is simply failing (e.g., the web scrape is failing or
            otherwise being prevented)
    """
    instock_status = 2
    try:
        page_text = scrape_web_page_text(url)
    except:
        _logger.warning(f'The web scrape for URL = {url} failed.')
    else:
        instock_status = (
            0 if check_web_page_text_for_in_stock_indicator(page_text) else 1)

    return instock_status

def main(arguments) -> None:
    """Creates new product file with OOS flag
    
    Creates a CSV file with the original product file
    columns as well as a new column that indicates whether
    the product was out of stock or not. The output file is sorted
    according to the OOS flag (0=in stock, 1=out of stock,
    2=in stock status could not be determined) and then the
    product key.
    """

    # Prepare default arguments
    module_dir = os.path.dirname(os.path.abspath(__file__))
    default_infile_path = os.path.join(module_dir,
        './../../resources/productlist.csv')
    default_outfile_path = './productListWithWalmartOOSFlags.csv'

    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="""If you're having issues, check that the product file is a CSV with
                  two columns. The first is a product key, and the second is a URL
                  for this product on the Walmart web site. This script assumes a 
                  product that is out of stock has the text 'Out of stock' show
                  up on the Walmart web site (not case sensitive)""")
    parser.add_argument('-i', '--infile',
                        default=default_infile_path,
                        type=argparse.FileType('r'),
                        help="Input file (i.e., the product file)")
    parser.add_argument('-o', '--outfile',
                        default=default_outfile_path,
                        type=argparse.FileType('w'),
                        help="Output file containing OOS indicator")

    # Parse command line arguments to the script
    args = parser.parse_args(arguments)

    # Read the product table from disk
    product_pdf = read_product_table_from_file(args.infile)

    # Append a new column to the Pandas DataFrame with the OOS flag
    # The out of stock (OOS) flag is 0 if it's determined to be in stock, 1 if it's
    # determined to be out of stock, and 2 if its instock status couldn't be determined.
    product_pdf['oos_flag'] = product_pdf.apply(
        lambda x: determine_product_in_stock_status(x.url), axis=1) 

    # Sort the product table to show out of stocks at the top, and then by ascending alphabetical order.
    # Write the sorted product table to a CSV file
    write_product_table_to_file(args.outfile, product_pdf)

    return

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
