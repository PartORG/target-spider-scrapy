# target-spider-scrapy
Spider for parcing product information from target.com website made in Python/Scrapy

## RUN:
In order to run open commandline in a directory where Spider is:
__cd <directory of spider>/__

Next, run next command:
__scrapy crawl TargetSpider  -a start_url="<PRODUCT URL FROM TARGET.COM>"__

If you want to save result in a file (JSON for example), write next command:
__scrapy crawl TargetSpider  -a start_url="<PRODUCT URL FROM TARGET.COM> -o <FILE_NAME>.json"__


## RESULT:
As a result you will see something similar in cmd window:
<(scrapy) D:\Python_Scripts\Scrapy\targetParse>scrapy crawl TargetSpider  -a start_url="https://www.target.com/p/disposable-red-plastic-cups-18oz-72ct-up-up-8482/-/A-14736272"
RESULT:
{
        'url': https://www.target.com/p/disposable-red-plastic-cups-18oz-72ct-up-up-8482/-/A-14736272,
        'title':Disposable Red Plastic Cups - 18oz - Up&Up™,
        'price':5.49,
        'currency':USD,
        'description':Keep your party essentials well stocked with this Pack of Disposable Red Plastic Cups from up & up™. This pack of disposable plastic cups is a must-have for any gathering, no matter what cold beverage you're serving. Each of these 18-ounce plastic cups are disposable, making post-party cleanups a breeze, and they're great for anything from water to soda to lemonade — no matter the occasion. ,
        'tcin':14736272,
        'upc':041594267714,
        'specs':
{           'Capacity (Volume)': ' 18.0 ounces',
            'Dimensions (Overall)': ' 4.73 Inches (H) x 3.88 Inches (W)',
            'Features': ' Unprinted',
            'Food or drink type held': ' Cold Beverages',
            'Includes': ' Cups',
            'Item Number (DPCI)': '253-05-0300',
            'Material': ' Polystyrene',
            'Package Quantity': ' 72',
            'Pattern': ' Solid, No Pattern Applied'}
}>
