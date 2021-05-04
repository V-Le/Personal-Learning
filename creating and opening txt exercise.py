create_txt = open('some_txt.txt', 'w') #Creating a new txt document if not using 'with open()'
create_txt.write('Writing to a new file.Second line written.Third line written.\nFourth line written.')
create_txt.close() #closing a txt if not using 'with open()'

with open('some_txt.txt', 'r') as f: #Another way of opening/creating a txt document2
    txt_data = f.read()

txt_lines = txt_data.split('.') #Splitting the text at '.'
new_txt = [x.strip() for x in txt_lines] #Stripping the txt of '\n' and list comp the new data
new_txt.pop() #removes the last element

with open('some_txt-rewritten.txt', 'w') as d: #Create and writes new data to txt
    for x in new_txt:
        d.write(x+'.\n')
