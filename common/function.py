from tabulate import tabulate

def print_table(data, is_dict=False):
    # print table using tabulate
    if is_dict:
        data = [data] # convert dict to list of dict
    for row in data:
        for key, value in row.items():
            if value is None:
                row[key] = "None" 
    print(tabulate(data, headers='keys', tablefmt='psql', showindex=False)) # print table using tabulate and without index column and use keys as headers

