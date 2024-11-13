# TODO Найдите количество книг, которое можно разместить на дискете
obyom_disk = 1.44 # в Мб
stranic = 100
strok = 50
symbols = 25
symbols1 = 4 # в байтах
ves_obyom_dickety = obyom_disk * 1024 * 1024
ves_obyom_knigi = stranic * strok * symbols * symbols1
kolvo_knig = ves_obyom_dickety / ves_obyom_knigi
print("Количество книг, помещающихся на дискету:", round(kolvo_knig))
