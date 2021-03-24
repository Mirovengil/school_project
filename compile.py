SEP = "<~sep~>"
OPEN = "<~"
CLOSE = "~>"
NAME = "<~name~>"
def rdf(string):
    return string.replace('\n', '')

def to_nav_ref(string):
    string = string.split(SEP)
    filename = "./" + string[0] + ".html"
    text = string[1] 
    return '''<a href="''' + filename + '''" class = "readdr">''' + text + "</a>\n"

def generate_nav(f):
    f = open(f, 'r')
    nav_menu = ""
    nav_menu = '''<nav class = "nav" id = "menu">\n'''
    nav_menu = nav_menu + '''<p class = "navpar">Навигация</p>\n'''
    for i in f:
        nav_menu = nav_menu + to_nav_ref(rdf(i))
    nav_menu = nav_menu + '''</nav>\n'''
    f.close()
    return nav_menu

def file_to_str(name):
    f = open('./template/' + name, 'r')
    rez = ""
    for i in f:
        rez = rez + i
    f.close()
    return rez

def build_page(string):
    rez = ""
    string = rdf(string).split(SEP)
    filename = string[0]
    name = string[1] 
    temp = open('./template/any_page.txt', 'r')
    for i in temp:
        i = rdf(i)
        i = i.replace('article', filename)
        i = i.replace(OPEN, "")
        i = i.replace(CLOSE, "")
        rez = rez + file_to_str(i + ".txt")
    temp.close()
    rez.replace(NAME, name)
    temp = open('./' + filename + '.html', 'w')
    print(rez, file = temp, end = "")
    temp.close()
    

f = open('./template/nav.txt', 'w')
print(generate_nav("makefile.txt"), file = f, end = "")
f.close()
f = open('./makefile.txt', 'r')
for i in f:
    build_page(i)
f.close()
print("Скомпилировано!")
