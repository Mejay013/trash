
alf = ('а','б','в','г','д','е','ж','з',
'и','й','к','л','м','н','о','п','р','с',
'т','у','ф','х','ц','ч','ш','щ','ъ','ы',
'ь','э','ю','я')

alf_matrx =[['а','б','в','г','д','е'],
            ['ж','з','и','й','к','л'],
            ['м','н','о','п','р','с'],
            ['т','у','ф','х','ц','ч'],
            ['ш','щ','ъ','ы','ь','э'],
            ['ю','я']]   

coding_dict = { 'атбаш' : 'atbash' , 'квадрат_полибия' : 'polybius_square', 'цезарь' : 'сaesar' , 'продвинутый_цезарь' : 'caesar_pr' }

encoding_list = list()


symbol_encode = { '-' : 'тире',
                  ',' : 'зпт',
                  '.' : 'тчк'}

def multiple_replace(some_text, symbol_encode,oper):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in symbol_encode.items():
        # меняем все target_str на подставляемое
        if oper == 'e':
            some_text = some_text.replace(i, j)
        else:
            some_text = some_text.replace(j,i)
    return some_text

def atbash_encode(text):
    for i in text:
        if i == ' ':
            encoding_list.append(' ')
        else:
            a = int(alf.index(i))
            encoding_list.append(alf[-(a+1)])
    full_data = ''.join(encoding_list)
    print(full_data)

def atbash_decode(text):
    for i in text:
        if i == ' ':
            encoding_list.append(' ')
        else:
            a = int(alf.index(i))
            encoding_list.append(alf[-(a+1)])
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data)

def polybius_square_encode(text):
    new_text = list(text)
    for var in new_text:
        for i in alf_matrx:
            for x in i:
                if x == var:
                    line = alf_matrx.index(i) + 1
                    column = i.index(x) + 1
                    some_str = f"{line}{column}"
                    encoding_list.append(some_str)
                elif x == ' ':
                    encoding_list.append(' ')
                else:
                    continue
    
    full_data = ' '.join(encoding_list)
    print(full_data)

def polybius_square_decode(text):
    
    new_text = text.split(' ')
    print (new_text)
    for var in new_text:
        line = int(var[0]) - 1
        column = int(var[1]) - 1
        symbol = alf_matrx[line][column]
        encoding_list.append(symbol)
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data) 

def сaesar_encode(text):
    new_text = list(text)
    print(new_text)
    for i in new_text:
        if i == ' ':
            encoding_list.append(' ')
        elif alf.index(i) == 29:
            encoding_list.append(alf[0])
        elif alf.index(i) == 30:
            encoding_list.append(alf[1])
        elif alf.index(i) == 31:
            encoding_list.append(alf[2])
        elif alf.index(i) < 29:
            symbol = alf.index(i)+3
            encoding_list.append(alf[symbol])
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data)

def сaesar_decode(text):
    new_text = list(text)
    print(new_text)
    for i in new_text:
        if i == ' ':
            encoding_list.append(' ')
        elif alf.index(i) == 2:
            encoding_list.append(alf[31])
        elif alf.index(i) == 1:
            encoding_list.append(alf[30])
        elif alf.index(i) == 0:
            encoding_list.append(alf[29])
        elif alf.index(i) > 2:
            symbol = alf.index(i)-3
            encoding_list.append(alf[symbol])
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data) 

def caesar_pr_encode(text):
    rot = int(input('Введите сдвиг: '))
    new_text = list(text)
    print(new_text)
    for i in new_text:
        if i == ' ':
            encoding_list.append(' ')
        elif alf.index(i) < (31-rot):
            symbol = alf.index(i)+rot
            encoding_list.append(alf[symbol])
        elif alf.index(i) >= (31-rot):
            symbol = 30-(31-rot)
            encoding_list.append(alf[symbol])
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data)

def caesar_pr_decode(text,rot):
    new_text = list(text)
    for i in new_text:
        if i == ' ':
            encoding_list.append(' ')
        elif alf.index(i) >= (0 + rot):
            symbol = alf.index(i)-rot
        elif alf.index(i) < (0 + rot):
            symbol = 32-(rot - alf.index(i))
        encoding_list.append(alf[symbol])
    full_data = ''.join(encoding_list)
    full_data = multiple_replace(full_data,symbol_encode,'d')
    print(full_data)




process = input(" Операция кодирование/расшифровка: (E/D) ")

coding_type = input("Выберите тип кодирования: (АТБАШ / Квадрат полибия / Цезарь / Продвинутый цезарь ) ").replace(' ','_').lower()

some_txt = input('Введите текст: ').lower()

text = multiple_replace(some_txt,symbol_encode,'e')
if (process.lower() == "e"):
    syf = "_encode(text)"
    if coding_type in coding_dict:
        a = coding_dict[coding_type] + syf
        exec(a)
else:
    syf = "_decode(text)"
    if coding_type in coding_dict:
        a = coding_dict[coding_type] + syf
        if a == 'caesar_pr_decode(text)':
            for rot in range(1,32):
                print('Сдвиг = '+ str(rot))
                caesar_pr_decode(text,rot)
                encoding_list.clear()
        else:
            exec(a)


