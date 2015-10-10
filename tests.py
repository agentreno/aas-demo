import app
import unittest

class AppTestCase(unittest.TestCase):
   def setUp(self):
      self.app = app.app.test_client()

   def test_index(self):
      resp = self.app.get('/')
      assert resp.status_code == 200
      assert "form" in resp.data.decode('utf-8')

   def test_submission(self):
      resp = self.app.post('/sendmsg', data={'msg':'hello'}, 
         follow_redirects=True)
      assert "hello" in resp.data.decode('utf-8')

if __name__ == "__main__":
   unittest.main()
