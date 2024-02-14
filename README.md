# kata09_checkout
It is a python project for kata09 checkout practice

http://codekata.com/kata/kata09-back-to-the-checkout/

## How to use
Keep the `prices.csv` file and update with your own prices row for test purpose.     
When checkout is ready, type in your item to checkout. type in 'q' to end the checkout.      

```sh
export CSV_FILE_PATH=/path/to/your/test_file.csv
python3 mypackage/main.py
```

## How to run the test     
Run all the testcases under the test folder    

```sh
export MODULE_PATH=/path/to/your/mypackage/folder
python3 -m unittest discover -v -s test
```

## To improve
  