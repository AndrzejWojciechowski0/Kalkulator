def calc_add(a, b):
 print('{} + {} ='.format(str(a), str(b)))
 return a + b

def calc_subtract(a, b):
 print('{} - {} ='.format(str(a), str(b)))
 return a - b

def calc_multiple(a, b):
 print('{} * {} ='.format(str(a), str(b)))
 return a * b

def calc_divide(a, b):
 print('{} / {} ='.format(str(a), str(b)))
 return a / b

def check_operation_name(operation):
 if operation in method_dict:
  return method_dict[operation]
 else:
  operation = input('Niepoprawne działanie, podaj jeszcze raz: dodawanie, odejmowanie, mnozenie, dzielenie :')
  check_operation_name(operation)

method_dict = {
 'dodawanie' : calc_add,
 'odejmowanie' : calc_subtract,
 'mnozenie' : calc_multiple,
 'dzielenie' : calc_divide,

}

if __name__ == "__main__":
 while True:
  print('Witam w moim kalkulatorze')
  operation = input('Podaj dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie :')
  if operation == 'exit':
   break
  operation_def = check_operation_name(operation)
  a = input('Podaj pierwsza liczbe: ')
  b = input('Podaj druga liczbe: ')
  if operation == 'dzielenie':
   if b == '0':
    print('Nie dziel przez 0')
    break
  print(operation_def(int(a), int(b)))


 







