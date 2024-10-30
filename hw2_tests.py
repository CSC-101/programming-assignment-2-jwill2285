import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        input1 = data.Point(2,2)
        input2 = data.Point(10,10)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(expected,result)
    def test_create_rectangle_2(self):
        input1 = data.Point(3,4)
        input2 = data.Point(1,2)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(3,4),data.Point(1,2))
        self.assertEqual(expected,result)
    # Part 2
    def test_shorter_duration_than(self):
        input1 = data.Duration(4,30)
        input2 = data.Duration(5,20)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertEqual(expected,result)
    def test_shorter_duration_than_2(self):
        input1 = data.Duration(6,30)
        input2 = data.Duration(6,20)
        result = hw2.shorter_duration_than(input1,input2)
        expected = False
        self.assertEqual(expected,result)
    # Part 3
    def test_songs_shorter_than(self):
        input1 = [data.Song("AJR","Bummerland",data.Duration(3,8)),
                  data.Song("AJR","OK Overture",data.Duration(4,31))]
        input2 = data.Duration(4,20)
        result = hw2.songs_shorter_than(input1,input2)
        expected = [data.Song("AJR","Bummerland",data.Duration(3,8))]
        self.assertEqual(expected,result)
    def test_songs_shorter_than_2(self):
        input1 = [data.Song("AJR","100 Bad Days",data.Duration(3,32)),
                  data.Song("AJR","Don't Throw Out My Legos",data.Duration(4,10))]
        input2 = data.Duration(5,10)
        result = hw2.songs_shorter_than(input1,input2)
        expected = [data.Song("AJR","100 Bad Days",data.Duration(3,32)),
                  data.Song("AJR","Don't Throw Out My Legos",data.Duration(4,10))]
        self.assertEqual(expected,result)
    # Part 4
    def test_running_time(self):
        input1 = [data.Song("AJR","100 Bad Days",data.Duration(3,32)),
                  data.Song("AJR","Don't Throw Out My Legos",data.Duration(4,10)),
                  data.Song("AJR", "100 Bad Days", data.Duration(3, 32)),
                  data.Song("AJR", "Don't Throw Out My Legos", data.Duration(4, 10))]
        input2 = [0,1,1,3,2]
        result = hw2.running_time(input1,input2)
        expected = data.Duration(19,34)
        self.assertEqual(expected,result)
    def test_running_time_2(self):
        input1 = [data.Song("AJR", "100 Bad Days", data.Duration(3, 32)),
                  data.Song("AJR", "Don't Throw Out My Legos", data.Duration(4, 10)),
                  data.Song("AJR", "100 Bad Days", data.Duration(3, 32)),
                  data.Song("AJR", "Don't Throw Out My Legos", data.Duration(4, 10))]
        input2 = [0,3,3,2]
        result = hw2.running_time(input1,input2)
        expected = data.Duration(15,24)
        self.assertEqual(expected,result)
    # Part 5
    def test_validate_route(self):
        input1 = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo'],
                  ['atascadero','santa margarita'], ['atascadero','creston']]
        input2 = ['san luis obispo','santa margarita','atascadero']
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected,result)
    def test_validate_route_2(self):
        input1 = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo'],
                  ['atascadero','santa margarita'], ['atascadero','creston']]
        input2 = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(input1,input2)
        expected = False
        self.assertEqual(expected,result)
    # Part 6
    def test_longest_repetition(self):
        input1 = [1,1,1,2,2,2,2,3,3,3,3,3,4,4]
        result = hw2.longest_repetition(input1)
        expected = 7
        self.assertEqual(expected,result)
    def test_longest_repetition_2(self):
        input1 = []
        result = hw2.longest_repetition(input1)
        expected = None
        self.assertEqual(expected,result)



if __name__ == '__main__':
    unittest.main()
