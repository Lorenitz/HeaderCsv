
from os import walk,path

def export_headers_of(filename):
    print('Parsing ' + filename)

    with open(filename, 'r') as csv_file:
    
        header = next(csv_file)

        columns = separate_header(header)
        output_filename=filename.replace(".csv"," header.txt")
        print('Writing ' + output_filename)
        with open(output_filename, 'w') as header_file:
            for column in columns: 
                header_file.write(column+'\n')
            

            header_file.close()    
        
        csv_file.close()


def separate_header(header):
    if "|" in header:
        return header.split("|")
    if ";" in header:
        return header.split(";")    
    return header.split(",")

print('Reading directory...')

dir_name = path.dirname(path.realpath(__file__))
dir = walk(dir_name)
file_list=next(dir)[2]

for file in file_list:
    if ".csv" in file:
        export_headers_of(file) 
