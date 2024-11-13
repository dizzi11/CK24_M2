# TODO Найдите количество книг, которое можно разместить на дискете
simbols = 25
strings = 50
pages = 100
megabites_in_disc = 1.44
simbols_in_book =  simbols * strings * pages
bites_in_book = 4 * simbols_in_book
kilobites_in_book = bites_in_book // 1024
kilobites_in_disc = megabites_in_disc * 1024
books_is_disc = round(kilobites_in_disc / kilobites_in_book)
print("Количество книг, помещающихся на дискету:", books_is_disc)
