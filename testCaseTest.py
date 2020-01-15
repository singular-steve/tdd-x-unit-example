from testCase import TestCase
from wasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        # print(test.wasRun)
        assert(not test.wasRun)
        test.run()
        # print(test.wasRun)
        assert(test.wasRun)


TestCaseTest("testRunning").run()



