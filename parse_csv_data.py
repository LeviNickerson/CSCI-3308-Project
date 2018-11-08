def get_map_data(input_string):

    #open first file
    export_file = open(input_string, "r")
    #get all lines from file
    raw_data = export_file.readlines()
    #amount var is the amount of items in out spreadsheet (-1 subtracts header)
    amount = len(raw_data) - 1
    #parse header and get columns
    titles = parse_header(raw_data[0])
    #split all data into 2D list
    data = sort_lines(raw_data[1:])

    output_data = {}

    #Place all data on coresponding lists

    #Location info
    output_data["geoX_List"] = transpose(data,titles["GEO_X"])
    output_data["geoY_List"] = transpose(data,titles["GEO_Y"])
    output_data["LON_List"] = transpose(data,titles["GEO_LON"])
    output_data["LAT_List"] = transpose(data,titles["GEO_LAT"])

    #Crime info
    output_data["OffenseType_List"] = transpose(data,titles["OFFENSE_TYPE_ID"])


    #convert all strings in the following lists to floats
    for i in ["geoX_List","geoY_List","LON_List","LAT_List"]:
        output_data[i] = convertlist_float(output_data[i])

    #convert strings in the following lists to ints
    for i in ["OffenseType_List"]:
        output_data[i] = convertlist_int(output_data[i])

    return output_data



def get_centerpoint_data(input_string):

        #open second file
        centerpoint_file = open(input_string, "r")
        #get all lines from file
        centerpoint_raw = centerpoint_file.readline()
        centerpoint_coordinantes = centerpoint_raw.split(",")
        centerpoint_coordinantes = convertlist_float(centerpoint_coordinantes)

        return centerpoint_coordinantes


def parse_header(head):

    col_names = head.split(",")
    name_to_idx = { }
    for i, n in enumerate(col_names):
        name_to_idx[n.strip()] = i
    return name_to_idx

def sort_lines(raw_data):

    data = []

    for i in range(len(raw_data)):
        line = raw_data[i].split(",")
        data.append(line)

    return data

def transpose(input_list,index):

    Target_List = []

    for i in range(len(input_list)):
        Target_List.append(input_list[i][index])

    return Target_List

def convertlist_int(input_list):
    #converts each list item to an int
    for i in range(len(input_list)):
        input_list[i] = float(input_list[i])
        input_list[i] = int(input_list[i])

    return input_list

def convertlist_float(input_list):
    #converts each list item to an float
    for i in range(len(input_list)):
        input_list[i] = float(input_list[i])

    return input_list

def map_to_idx(idx_List):
    #creats a dictionary to associate values to lists
    mapped_idx_list = {}
    for i, n in enumerate(idx_List):
        mapped_idx_list[n] = i

    return mapped_idx_list

def get_idx_from_user_input(mapped_seat_list,user_input):

    user_input = int(user_input)

    idx = mapped_seat_list[user_input]

    return idx,user_input
