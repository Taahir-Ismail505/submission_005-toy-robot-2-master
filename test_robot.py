import unittest
from unittest.mock import patch
from robot import Whats_my_Name,Control_Panel,move_Forward_on_y,move_Back_on_y,turn_Right_on_x,turn_Left_on_x,sprint
from io import StringIO

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("Robot\nBruce\n"))
    def test_Name(self):
        self.assertEqual(Whats_my_Name(),"Robot")
        self.assertEqual(Whats_my_Name(),"Bruce")
  
    def test_forward(self):
        self.assertEqual(move_Forward_on_y([0,0],5,"robot",[1]),(5,0))

    def test_back(self):
        self.assertEqual(move_Back_on_y([0,0],5,"robot",[1]),(-5,0))

    def test_right(self):
        self.assertEqual(turn_Right_on_x([0,0],"robot",[0]),[1])
    
    def test_left(self):
        self.assertEqual(turn_Left_on_x([0,0],"robot",[0]),[3])
    
      
    @patch("sys.stdin", StringIO("help\nforward 5\nback 5\noff\nleft\nright\n"))
    def test_control(self):
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"help")
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"forward 5")
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"back 5") 
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"off")         
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"left")
        self.assertEqual(Control_Panel("Robot",[0,0],[1]),"right")

    def test_sprint(self):
        self.assertEqual(sprint([0,0],[1],1,"robot",[0]),1)