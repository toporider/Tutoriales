"""Lista de argumentos y lista de 
    argumentos de palabras claves
    (keywords)"""

def testArgLists_1(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs

testArgLists_1('aaa', 'bbb', arg1='ccc', arg2 ='ddd')

def testArgLists_2(arg0, *args, **kwargs):
    print 'arg0:" %s"'  %arg0
    print 'args:', args
    print 'kwargs:', kwargs

def test():
    testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')
    print '=' * 40
    testArgLists_2('Primer argumento', 'aaa', 'bbb', arg1='ccc', ag2='ddd')

test()
