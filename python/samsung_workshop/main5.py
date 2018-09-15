def bar(**args):
    for a in args:
        print a, args[a]

bar(name='one', age=27)
