from bs4 import BeautifulSoup

#reading the data inside the xml file to a variable under the name data
with open('../dataset/SalesTransactions.xml', 'r') as f:
    data = f.read()

#passing the stored data inside the beatifulsoup parder
bs_data = BeautifulSoup(data, 'lxml')

#Finding all instances of tag
UelSample = bs_data.find_all('UelSample')
print(UelSample)