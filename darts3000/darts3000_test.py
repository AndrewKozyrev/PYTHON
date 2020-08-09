import unittest
from darts3000 import maxScore

class Test_test_1(unittest.TestCase):
    def test_A(self):
        path = 'test-1.txt'
        with open(path, 'r') as f:
            N = int(f.readline())
            read_data = []
            while True:
                line1 = f.readline().rstrip()
                line2 = f.readline().rstrip()
                read_data.append([line1, line2])
                if not line2: break
        path = 'ans-1.txt'
        with open(path, 'r') as f:
            read_answers = []
            for line in f:
                read_answers.append(line.rstrip())
        for i in range(N):
            result = maxScore(read_data[i][0], read_data[i][1])
            self.assertEqual(result, int(read_answers[i]))
    
    def test_B(self):
        path = 'test-2.txt'
        with open(path, 'r') as f:
            N = int(f.readline())
            read_data = []
            while True:
                line1 = f.readline().rstrip()
                line2 = f.readline().rstrip()
                read_data.append([line1, line2])
                if not line2: break
        path = 'ans-2.txt'
        with open(path, 'r') as f:
            read_answers = []
            for line in f:
                read_answers.append(line.rstrip())
        for i in range(N):
            result = maxScore(read_data[i][0], read_data[i][1])
            self.assertEqual(result, int(read_answers[i]))

    def test_C(self):
        self.assertEqual(maxScore("8 -1", "20 50 -50 -30 10 30 39 -60"), 89)

if __name__ == '__main__':
    unittest.main()
