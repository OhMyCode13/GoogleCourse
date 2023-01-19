import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""
  # Call the function to create the file
    create_file(filename)
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in csv_reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


def contents_of_file_no_dict(filename):
    return_string = ""
    create_file(filename)
    # Open the file
    with open(filename) as csv_file:
        rows = csv.reader(csv_file)
        header=[]
        header = next(csv_file)
        for row in rows:
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(row[0], row[1], row[2])
    return return_string

# print(contents_of_file("flowers.csv"))
print(contents_of_file_no_dict("flowers.csv"))