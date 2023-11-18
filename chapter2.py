class test():
    def __init__(self, sqlParam, ):
        self.sqlParam = sqlParam
        self.host = sqlParam[0]
        self.database = sqlParam[1]
        self.user = sqlParam[2]
        self.password = sqlParam[3]
        self.fine = True


if __name__ == "__main__":
    import sys
    sqlParam = ('localhost', 'jovenschema', 'root', 'Acoje1985 **')
    print('x')