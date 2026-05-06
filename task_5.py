#Задание 5



class TestCase:
    
#Напиши класс TestCase. Он должен содержать конструктор и методы.
#В конструкторе инициализируются поля:
#steps — шаги тест-кейса, в качестве параметра принимает пустой словарь;
#result — ожидаемый результат выполнения тест-кейса, принимает None в качестве параметра. 

    def __init__(self,steps={},result=None):
        self.steps = steps
        self.result = result
        

    
 #Метод set_step — добавляет в словарь steps шаг тест-кейса. Принимает два параметра: step_number и step_text. Ключ — это step_number(номер шага), а значение — step_text (текстовое описание шага).
   
    def set_step(self,step_number,step_text):
        self.steps[step_number] = step_text

#Метод delete_step — удаляет шаг из steps по ключу step_number, который передали в метод.
    def delete_step(self, step_number):
        del self.steps[step_number]

#Метод set_result — устанавливает ожидаемый результат. Он помещает его в атрибут result по параметру result, который передали методу.

    def set_result(self, result):
        self.result = result

#Метод get_test_case — печатает информацию о составе тест-кейса в формате {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}.
    def get_test_case(self):

        print("'Шаги': {") 
        for self.steps_number, self.steps_text in self.steps.items():
            print('       ',int(self.steps_number), ':', self.steps_text)
        print('},') 
        print("'Ожидаемый результат': ", "'",self.result,"'")

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()
print('')
test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 

        #for self.steps.number, self.steps.text in self.steps.items():
            #print(self.steps.number + ':'+ self.steps.text) 

#print(self.steps)


        #for number, text in self.steps.items():
            #print('Шаги: {'+ int(number) + ':'+ str(text)+'},' + 'Ожидаемый результат: ', self.result)

#Пример вывода метода get_test_case:

#{
    #'Шаги': {
     #       1: 'Перейти на сайт', 
      #      2: 'Перейти в раздел Товары', 
       #     3: 'Нажать кнопку «В корзину» у первого товара'
    #}, 
    #'Ожидаемый результат': 'Товар окажется в корзине'
#} 
