SEP = "<~key~>"
SEP2 = "<~page~>"
OPEN = "<~"
CLOSE = "~>"
NAME = "<~name~>"
TAB = "<~tab~>"

PYSTART = "<~py~>"
PYEND = "<~/py~>"
CSTART = "<~c~>"
CEND = "<~/c~>"
PASTART = "<~pa~>"
PAEND = "<~/pa~>"

def rdf(string):
    return string.replace('\n', '')

def to_nav_ref(string):
    string = string.split(SEP)
    if len(string) < 2:
        return ""
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
    nav_menu = nav_menu + '''</nav>\n<h1><~name~></h1>\n'''
    f.close()
    return nav_menu

def file_to_str(name):
    f = open('./template/' + name, 'r')
    rez = ""
    for i in f:
        i = i.replace(PYSTART, '''<p class = "lang">Python</p><pre><code class = "Python">''')
        i = i.replace(PASTART, '''<p class = "lang">Pascal</p><pre><code>''')
        i = i.replace(CSTART, '''<p class = "lang">C++</p><pre><code class = "C++">''')
        i = i.replace(PYEND, '''</code></pre>''')
        i = i.replace(CEND, '''</code></pre>''')
        i = i.replace(PAEND, '''</code></pre>''')
        rez = rez + i
    f.close()
    return rez

def build_page(string):
    rez = ""
    string = rdf(string).replace(SEP2, SEP).split(SEP)
    filename = string[0]
    name = string[1] 
    temp = open('./template/std/any_page.txt', 'r')
    for i in temp:
        i = rdf(i)
        i = i.replace('article', filename)
        i = i.replace(OPEN, "")
        i = i.replace(CLOSE, "")
        rez = rez + file_to_str(i + ".txt")
    temp.close()
    rez = rez.replace(NAME, name)
    rez = rez.replace(TAB, "&#160;&#160;&#160;&#160;")
    temp = open('./' + filename + '.html', 'w')
    print(rez, file = temp, end = "")
    temp.close()
    

f = open('./template/std/nav.txt', 'w')  
print(generate_nav("makefile.txt"), file = f, end = "")
f.close()
f = open('./makefile.txt', 'r')
for i in f:
    build_page(i)
f.close()
print("Скомпилировано!")
