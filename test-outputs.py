import filecmp
class TestGroovyTemplates:
    def testGroovySuccess(self):
        f1 = "templates/resources/sample-groovy-new.result"
        f2 = "success-email.result"
        # shallow comparison
        result = filecmp.cmp(f1, f2)
        print(result)
        # deep comparison
        result = filecmp.cmp(f1, f2, shallow=False)
        print(result)   
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
self