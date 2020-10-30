from zeep import Client
from datetime import date
import sys

client = Client('http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?wsdl')
result = client.service.GetCursOnDate(date.today())

for item in result._value_1._value_1:
    if item['ValuteCursOnDate']['VchCode'] == 'USD':
        curs = float(item['ValuteCursOnDate']['Vcurs'])
        print("Текущий курс доллара США: {}".format(curs))

if len(sys.argv) > 1:
    dollarsCount = float(sys.argv[1])
    print("На входе ${}".format(dollarsCount))
    amount = dollarsCount*curs
    
else:
    dollarsCount = float(input("Введите количество долларов: "))
    amount = dollarsCount * curs
print("На выходе {} руб.".format(amount))