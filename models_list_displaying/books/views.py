from django.shortcuts import render
from django.urls import reverse
from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {}
    pub_dates = set()
    if pub_date:
        for book in books:
            pub_dates.add(book.pub_date)
        dates_sort = sorted(pub_dates)
        for el in dates_sort:
            if pub_date < el:
                next_page = el
                context.setdefault('next_page', f'{reverse(books_view)}/{next_page}/')
                context.setdefault('next_page_pag', f'{next_page}')
                break
        for el in reversed(dates_sort):
            if pub_date > el:
                prev_page = el
                context.setdefault('prev_page', f'{reverse(books_view)}/{prev_page}/')
                context.setdefault('prev_page_pag', f'{prev_page}')
                break
        books = filter(lambda book: book.pub_date == pub_date, books)
    books = list(books)
    context.setdefault('books', books)
    return render(request, template, context)
