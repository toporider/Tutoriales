#Llamando a una funcion con argumentos
#de palabras claves (keyword)

def test_keyword_args(color_1 ='verde',
        color_2 = 'azul',
        color_3 = 'red',
        color_4 = 'marron'):
    print 'color_1: "%s"'   %color_1
    print 'color_2: "%s"'   %color_2
    print 'color_3: "%s"'   %color_3
    print 'color_4: "%s"'   %color_4

def test():
    test_keyword_args()
    print '-'*40
    test_keyword_args(color_2 ='amarillo')
    print '-' *40
    test_keyword_args(color_3 = 'naranja',
            color_4 = 'violeta')

test()

