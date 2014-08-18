import os

from .. import generator

# from http://getbootstrap.com/getting-started/#template
BOOTSTRAP_BASIC_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
'''


here_dir = os.path.dirname(__file__)


def test_generate_no_args():
    html = generator.generate()
    assert html == BOOTSTRAP_BASIC_TEMPLATE


def test_generate_slot():
    template_text = 'apple<!--slot="other_fruit"--> cherry<!--slot="durian"-->'
    new_text = generator.fill_slot(template_text, {'other_fruit': ' banana', 'durian': ' durian'})
    assert 'apple banana cherry durian' == new_text


def test_generate_from_file_with_slots():
    path = os.path.join(here_dir, 'test_assets/test_generate_from_file_with_slots/base.txt')
    results = generator.fill_slots_in_file(path)
    expected = open(os.path.join(here_dir, 'test_assets/test_generate_from_file_with_slots/expected.txt')).read()
    assert results == expected
