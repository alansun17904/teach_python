import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .context import box


def test_simple_box():
    correct_box = '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +'

    assert box.Box.simple_box() == correct_box


def test_complex_box():
    correct_box = '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +'
    assert box.Box.complex_box() == correct_box


def test_crazy_box():
    zero_box = ''
    assert box.Box.crazy_box(0) == zero_box

    one_box = '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +'
    assert box.Box.crazy_box(1) == one_box

    two_box = '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +'
    assert box.Box.crazy_box(2) == two_box

    three_box = '+ - - - - + - - - - +' \
                '|         |         |' \
                '|         |         |' \
                '+ - - - - + - - - - +' \
                '|         |         |' \
                '|         |         |' \
                '+ - - - - + - - - - +' \
                '|         |         |' \
                '|         |         |' \
                '+ - - - - + - - - - +'
    assert box.Box.crazy_box(3) == three_box

    four_box = '+ - - - - + - - - - +' \
               '|         |         |' \
               '|         |         |' \
               '+ - - - - + - - - - +' \
               '|         |         |' \
               '|         |         |' \
               '+ - - - - + - - - - +' \
               '|         |         |' \
               '|         |         |' \
               '+ - - - - + - - - - +' \
               '|         |         |' \
               '|         |         |' \
               '+ - - - - + - - - - +'
    assert box.Box.crazy_box(4) == four_box
