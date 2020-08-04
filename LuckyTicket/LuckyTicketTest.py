import unittest
from LuckyTicket import nextTicket

class LuckyTicketTest(unittest.TestCase):

    def test_lucky_tickets(self):
        self.assertEqual(nextTicket(121), 132)
        self.assertEqual(nextTicket(148326491), 148326497)
        self.assertEqual(nextTicket(909090), 910206)
        
        

if __name__ == '__main__':
    unittest.main()