books=['the mind','history','power of money']
class lib:
    def request_book(self):
        for x in books:
            print(x)
        req=input('enter book name')
        return req
    def lending_book(self):
        if y in books:
            print('the book is available and take it')
        else:
            print('the book is not available')
l1=lib()
catcher=l1.request_book()
print(catcher)
l1.lending_book(catcher)
