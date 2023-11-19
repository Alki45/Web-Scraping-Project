def remove_duplicates_from_text(file_path):
    with open(file_path, 'r') as file:
        data = eval(file.read())
    data=[item for item in data if ",\n," not in item]
    unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]
    
    print(unique_data)

file_path = "C:\\Users\\Admin\\OneDrive\\Desktop\\Web_scrap\\LIst_job.txt"
remove_duplicates_from_text(file_path)