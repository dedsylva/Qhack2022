#! /usr/bin/python3

import os
import numpy as np 
import unittest
from unittest_prettify.colorize import colorize, GREEN

@colorize(color=GREEN)
class TestP101(unittest.TestCase):

  def test_p1(self):
    """ Test P1 - Order Matters [100 Points] """
    COMMON_FILEPATH = "src/Pennylane101/p1/"

    ## Opening 1.nut ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans1.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")


    ## Opening 2.nut ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans1.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")


  def test_p2(self):
    """ Test P2 - Know Your Devices [200 Points] """
    COMMON_FILEPATH = "src/Pennylane101/p2/"

    ## Opening 1.nut ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans2.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")


    ## Opening 2.nut ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans2.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")



  def test_p3(self):
    """ Test P3 - Superdense Coding [300 Points] """
    COMMON_FILEPATH = "src/Pennylane101/p3/"

    ## Opening 1.nut ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans3.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")


    ## Opening 2.nut ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = float(data.read())

    os.system(COMMON_FILEPATH+"./ans3.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = float(our.read())


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    self.assertTrue(res, our_res)
    print(f"\nexpected: {res}, got: {our_res}")



  def test_p4(self):
    """ Test P4 - Finite-Difference Gradient [400 Points] """
    COMMON_FILEPATH = "src/Pennylane101/p4/"

    ## Opening 1.nut ##
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
    print(f"\nexpected: {res}, got: {our_res}")

    ## Opening 2.nut ##
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
    print(f"\nexpected: {res}, got: {our_res}")


  def test_p5(self):
    """ Test P5 - Bitflip Error Code [500 Points] """
    COMMON_FILEPATH = "src/Pennylane101/p5/"

    ## Opening 1.nut ##
    with open(COMMON_FILEPATH+"1.out") as data:
      res = list(map(float, data.read().split(',')))

    os.system(COMMON_FILEPATH+"./ans5.py < "+COMMON_FILEPATH+"1.in > res1.txt")
    with open("res1.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res1.txt"):
      os.remove("res1.txt")
    else:
      raise FileNotFoundError("Could not delete res1.txt file")


    comparisson = np.isclose(our_res, res, atol=5e-03).all()
    self.assertTrue(comparisson, True)
    print(f"\nexpected: {res}, got: {our_res}")

    ## Opening 2.nut ##
    with open(COMMON_FILEPATH+"2.out") as data:
      res = list(map(float, data.read().split(',')))

    os.system(COMMON_FILEPATH+"./ans5.py < "+COMMON_FILEPATH+"2.in > res2.txt")
    with open("res2.txt") as our:
      our_res = list(map(float, our.read().split(','))) 


    if os.path.exists("res2.txt"):
      os.remove("res2.txt")
    else:
      raise FileNotFoundError("Could not delete res2.txt file")


    comparisson = np.isclose(our_res, res, atol=5e-03).all()
    self.assertTrue(comparisson, True)
    print(f"\nexpected: {res}, got: {our_res}")





if __name__ == '__main__':
  unittest.main(verbosity=2)
