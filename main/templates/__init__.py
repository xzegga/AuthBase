import os


def get_template(template):

  dirpath = os.path.dirname(os.path.realpath(__file__))
  template_path = '%s\\%s.html' % (dirpath, template.replace('/', '\\'))

  with open(template_path) as fh:
    return fh.read()