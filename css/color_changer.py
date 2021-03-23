#Навигационной менюшки
nav_color = "f7e677"

#Ссылки в менюшке навигации
readdr_color = "00a8f5"

#Ссылки в менюшке навигации, когда на неё навели курсор
readdr_hover_color = "00a8f5"

#Буквы "i" в названии сайта
fake_letter_color = "00a8f5"

#Фона сайта
main_color = "bcfab6"

def replace_colors_to_values(string):
    string.replace("nav_color", "#" + nav_color)
    string.replace("readdr_color", "#" + readdr_color)
    string.replace("readdr_hover_color", "#" + readdr_hover_color)
    string.replace("fake_letter_color", "#" + fake_letter_color)
    string.replace("main_color", "#" + main_color)
    return string

stdin = open("./style_template_for_experiment.txt", 'r')
stdout = open("./style.css", 'w')

for i in stdin:
    print(replace_colors_to_values(i), file = stdout)

stdin.close()
stdout.close()
