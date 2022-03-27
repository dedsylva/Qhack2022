#! /usr/bin/python3

import os
import numpy as np 
import unittest
from unittest_prettify.colorize import colorize, GREEN

@colorize(color=GREEN)
class TestALG(unittest.TestCase):

  def test_p1(self):
    """ ALG: P1 - The Deutsch-Josza Problem [100 Points] """
    COMMON_FILEPATH = "src/Algorithms/p1/"

    ## Opening 1.out ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = data.read()

    os.system(COMMON_FILEPATH+"./ans1.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = our.read().split('\n')[0]


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertEqual(res, our_res)

    ## Opening 2.out ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = data.read()

    os.system(COMMON_FILEPATH+"./ans1.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = our.read().split('\n')[0]


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertEqual(res, our_res)

  def test_p2(self):
    """ ALG: P2 - Adapting to the Topology [200 Points] """
    COMMON_FILEPATH = "src/Algorithms/p2/"

    ## Opening 1.out ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans2.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertEqual(res, our_res)

    ## Opening 2.out ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans2.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertEqual(res, our_res)


  def test_p3(self):
    """ ALG: P3 - QFT Adder [300 Points] """
    COMMON_FILEPATH = "src/Algorithms/p3/"

    ## Opening 1.out ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = list(map(float, data.read().split(',')))

    os.system(COMMON_FILEPATH+"./ans3.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertTrue(res, our_res)

    ## Opening 2.out ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = list(map(float, data.read().split(',')))


    os.system(COMMON_FILEPATH+"./ans3.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertTrue(res, our_res)


  def test_p4(self):
    """ ALG: P4 - Quantum Coding [400 Points] """
    COMMON_FILEPATH = "src/Algorithms/p4/"

    ## Opening 1.out ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = list(map(float, data.read().split(',')))

    os.system(COMMON_FILEPATH+"./ans4.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    comparisson = np.isclose(our_res, res, atol=5e-03).all()
    self.assertTrue(comparisson, True)

    ## Opening 2.out ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = list(map(float, data.read().split(',')))

    os.system(COMMON_FILEPATH+"./ans4.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    comparisson = np.isclose(our_res, res, atol=5e-03).all()
    self.assertTrue(comparisson, True)


  def test_p5(self):
    """ ALG: P5 - Deutsch-Josza Strikes Again [500 Points] """
    COMMON_FILEPATH = "src/Algorithms/p5/"

    ## Opening 1.out ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = data.read()

    os.system(COMMON_FILEPATH+"./ans5.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = our.read().split('\n')[0]


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertEqual(res, our_res)

    ## Opening 2.out ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = data.read()

    os.system(COMMON_FILEPATH+"./ans5.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = our.read().split('\n')[0]


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertEqual(res, our_res)




if __name__ == '__main__':
  unittest.main(verbosity=2)
