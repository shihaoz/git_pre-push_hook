# regular expressioN
import re


def Searcher():
  return _searcher()

class _searcher:
  """
  define a searcher class that
  input: <Word>, <min_count>, <list of filename>
  output: <list of filename that contain Word at least min_count times>
  """
  call_count = 0

  def __init__(self):
    return

  def search(self, word, min_count, file_list):
    pattern = r'{0}'.format(word)
    return_list = []
    for file_name in file_list:
      ifstream = open(file_name, 'rU')
      matches = re.findall(pattern, ifstream.read())

      if len(matches) >= min_count:
        return_list.append(file_name)

    self.call_count += 1
    return return_list
