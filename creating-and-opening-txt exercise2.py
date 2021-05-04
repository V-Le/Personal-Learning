def create_cast_list(filename):
    with open('flying_circus_cast.txt', 'r') as file_data:     #use with to open the file filename
        cast_list = [line.split(',')[0] for line in file_data]    #list comp to read and append names only

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
