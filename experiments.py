

# file = open('./test.txt')

# for item in file:
#     print(item)

# file.close()

# with open('./test.txt') as text_file:
#     for line in text_file:
#         print(line)

# class WithStatementTestClass:
#     def __init__(self):
#         print('WithStatementClass created.')

#     def __enter__(self):
#         print('__enter__ method called')
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('exc_type: ', exc_type)
#         print('exc_value: ', exc_value)
#         print('traceback: ', traceback)

#     def __repr__(self):
#         return 'This is the WithStatementTestClass object'
    
# if __name__ == '__main__':

#     try:
#         with WithStatementTestClass() as obj:
#             print('processing object: ', format(obj))
#             raise Exception('test exception')
#     except Exception as e:
#         print('there was an exception: ', e)
    
#     print('indentation block is left')


# print(__name__)

def give_message(message):
    print(message)
    # return "nothing"

class TestClass:
    method = staticmethod(give_message)

    @staticmethod
    def say_hi(greeting):
        print(greeting)
        # return 'something'
    

print(TestClass.method("hallo")) #exp hallo reality: ok
print(TestClass().method('2')) #exp 2 reality: OK
print(TestClass.say_hi("hey")) #exp hey
print(TestClass().say_hi("hello")) #exp hello