from my_framework.templator import render

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))

class News:
    def __call__(self, request):
        return '200 OK', render('news.html', date=request.get('date', None))

class Timetable:
    def __call__(self, request):
        return '200 OK', render('timetable.html', date=request.get('date', None))

class Contacts:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))
