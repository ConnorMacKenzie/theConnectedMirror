import weatherClient, unittest

class TestInitClient(unittest.TestCase):

    def setUp(self):
        self.localname = 'loclahost'
        self.remotename = self.localname
        self.localport = 22
        self.remoteport = 23
        self.wc = weatherClient.client()

    def tearDown(self):
        self.wc.closeConnection()

    def test_initialize(self):
        tester = self.wc.initialize("localhost", 22, "localhost", 23)
        assert tester is not None, "Not connecting to local socket"

class TestSendData(unittest.TestCase):

    def setUp(self):
        self.localname = 'loclahost'
        self.remotename = self.localname
        self.localport = 22
        self.remoteport = 23
        self.wc = weatherClient.client()
        self.wc.initialize("localhost", 22, "localhost", 23)

    def tearDown(self):
        self.wc.closeConnection()

    def test_pullRequest(self):
        requestBytes = self.wc.pullRequest('Request')
        assert requestBytes is not 0, "Nothing was sent"

class TestStartListening(unittest.TestCase):

    def setUp(self):
        self.localname = 'loclahost'
        self.remotename = self.localname
        self.localport = 22
        self.remoteport = 23
        self.wc = weatherClient.client()
        self.wc.initialize("localhost", 22, "localhost", 23)
        self.wc.pullRequest('Request')

    def tearDown(self):
        self.wc.closeConnection()

    def test_startListening(self):
        assert len(self.wc.startListening()) is not 0, "Nothing was returned"


if __name__ == "__main__":
    unittest.main()
