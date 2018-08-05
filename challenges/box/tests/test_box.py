from challenges.box.src.box import Box


def test_simple_box():
    correct_box = '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +' \
                  '|         |         |' \
                  '|         |         |' \
                  '+ - - - - + - - - - +'

    assert Box.simple_box() == correct_box


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
    assert Box.complex_box() == correct_box


def test_crazy_box():
    zero_box = ''
    assert Box.crazy_box(0) == zero_box

    one_box = '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +'
    assert Box.crazy_box(1) == one_box

    two_box = '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +' \
              '|         |         |' \
              '|         |         |' \
              '+ - - - - + - - - - +'
    assert Box.crazy_box(2) == two_box

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
    assert Box.crazy_box(3) == three_box

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
    assert Box.crazy_box(4) == four_box
