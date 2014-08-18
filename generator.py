import os
import re

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


def generate():
    return BOOTSTRAP_BASIC_TEMPLATE


def fill_slot(template, data=None, root_dir=None):
    def repl(match):
        kind, value = match.groups()
        if kind == 'slot':
            if root_dir is not None:
                try:
                    value = open(os.path.join(root_dir, value), 'r').read()
                    return value
                except IOError as e:
                    print e
                    pass
            return '%(' + value + ')s'
        return None

    pattern = '<!--\s*(\S*)=[\"\'](\S*)[\"\']\s*-->'
    template = re.sub(pattern, repl, template)
    if data is None:
        return template
    return template % data


def fill_slots_in_file(file_path):
    #assume files are small enough to read all into memory
    template = open(file_path, 'r').read()
    return fill_slot(template, root_dir=os.path.dirname(file_path))
