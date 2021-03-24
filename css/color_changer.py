#Навигационной менюшки
nav_color = "07575b"

#Ссылки в менюшке навигации
readdr_color = "66a5ad"

#Ссылки в менюшке навигации, когда на неё навели курсор
readdr_hover_color = "003b46"

#Буквы "i" в названии сайта
fake_letter_color = "ff7f50"

#Фона сайта
main_color = "c4dfe6"

#Плашки в верху сайта
header_color = "66a5ad"

#Надписи о правах
copyright_color = "66a5ad"

#Цвета текста на навигации после наведения
readdr_new_color = "c4dfe6"

def replace_colors_to_values(string):
    string = string.replace("nav_color", "#" + nav_color)
    string = string.replace("readdr_color", "#" + readdr_color)
    string = string.replace("readdr_hover_color", "#" + readdr_hover_color)
    string = string.replace("fake_letter_color", "#" + fake_letter_color)
    string = string.replace("main_color", "#" + main_color)
    string = string.replace("header_color", "#" + header_color)
    string = string.replace("copyright_color", "#" + copyright_color)
    string = string.replace("readdr_new_color", "#" + readdr_new_color)
    return string


def main(name):
    stdin = open("./css/" + name + "_template" + ".txt", 'r')
    stdout = open("./css/" + name + ".css", 'w')

    for i in stdin:
        print(replace_colors_to_values(i), file = stdout, end = "")

    stdin.close()
    stdout.close()

main("style_1000_inf")
main("style_600_1000")
