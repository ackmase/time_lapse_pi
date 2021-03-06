"""Reformats jpg filenames for use with the avconv tool.

The avconv tool requires files to follow a strict pattern: files needs to be
in order without any skipped values and padded to the left with 0s. This module
updates jpgs that are named with datetime values, orders them, and renames them.
"""

import os
import sys


def SortKey(filename):
  """Sort key for natural sorting based on timestamp.
  
  Assumes that the filename is just a timestamp generated by datetime and that
  the file has a .jpg extension.
  
  Args:
    item: string, a jpg name where the file name is a timestamp generated by
      datetime.
  
  Returns:
    Integer representation of the filename.
  """
  chars_to_replace = ['-', ':', '.jpg']
  for char in chars_to_replace:
    filename = filename.replace(char, '')
  return int(filename)


def main():
  assert len(sys.argv) == 2, 'Usage: format_filenames.py /path/to/directory/'
  
  directory = sys.argv[1]
  results = os.popen('ls %s' % directory)
  old_filenames = [row.strip('\n') for row in results]
  ordered_old_filenames = sorted(old_filenames, key=SortKey)

  # Rename each file using the new naming schema.
  for index in range(len(ordered_old_filenames)):
    old_file_path = os.path.join(directory, ordered_old_filenames[index])
    new_file_path = os.path.join(directory, '%04d.jpg' % (index + 1))
    os.popen('mv %s %s' % (old_file_path, new_file_path)) 


if __name__ == '__main__':
  main()
