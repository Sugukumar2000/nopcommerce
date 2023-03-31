
def testprog():
    word = "Machine Learning"
    text = word.split()
    print (text)
    print("".join([i[0].upper() for i in text]))


testprog()
