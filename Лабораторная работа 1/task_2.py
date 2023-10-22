#Расчет количества книг на дискете
disket_Mb = 1.44
symbol_by = 4
by_Mb = 1024 * 1024
book = {
    "Страницы": 100,
    "Строки": 50,
    "Символы": 25
}
symbook = book["Страницы"] * book["Строки"] * book["Символы"]
membook = symbook * symbol_by
books = disket_Mb * by_Mb // membook
print(round(books))
