import filecmp
class TestGroovyTemplates:
    def testGroovySuccess(self):
        f1 = open("templates/resources/sample-groovy-new.result")
        f2 = open("success-email.result")
        i = 0
        for line1 in f1:
            i += 1
            for line2 in f2:           
                if line1 == line2:  
                    print("Line ", i, ": IDENTICAL")       
                else:
                    print("Line ", i, ":")
                    print("\tFile 1:", line1, end='')
                    print("\tFile 2:", line2, end='')
                break
        
        # closing files
        f1.close()                                       
        f2.close()    
    def testGroovyFailure(self):
        f1 = "templates/resources/sample-groovy-new-fail.result"
        f2 = "failure-email.result"
        # shallow comparison
        result = filecmp.cmp(f1, f2)
        print(result)
        # deep comparison
        result = filecmp.cmp(f1, f2, shallow=False)
        print(result)      




if __name__ == '__main__':
    test = TestGroovyTemplates()
    test.testGroovySuccess()
    test.testGroovyFailure()
 