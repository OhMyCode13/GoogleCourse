import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,'w') as file:
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
  return(filesize)

#print(create_python_script("program.py"))

def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join(os.getcwd(), os.path.abspath('..'))

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())