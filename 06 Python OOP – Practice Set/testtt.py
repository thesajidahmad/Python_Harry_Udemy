def decorators(fun):
    def wrappers():
        print("running")
        fun()
    return wrappers

@decorators
def do_this():
    print("do this")

@decorators
def do_that():
    print("do that")

do_this()
do_that()