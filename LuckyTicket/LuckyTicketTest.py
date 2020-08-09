import unittest
from LuckyTicket import nextTicket

class LuckyTicketTest(unittest.TestCase):

    def test_lucky_tickets(self):
        self.assertEqual(nextTicket(121), 132)
        self.assertEqual(nextTicket(148326491), 148326497)
        self.assertEqual(nextTicket(909090), 909909)
        self.assertEqual(nextTicket(9090909090909090909090), 9091020202020202555549)
        

if __name__ == '__main__':
    unittest.main()