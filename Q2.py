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

  return_list = []
  index = 0

  def next(self):
    if self.index > len(self.return_list) - 1:
      raise StopIteration
    ret = self.return_list[self.index]
    self.index += 1
    return ret

  def __iter__(self):
    return self

  def search(self, word, min_count, file_list):
    pattern = r'{0}'.format(word)

    for file_name in file_list:
      ifstream = open(file_name, 'rU')
      matches = re.findall(pattern, ifstream.read())

      if len(matches) >= min_count:
        self.return_list.append(file_name)

    return self
