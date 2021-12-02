def extract_functions(python_filename, output_filename):
    function_terms = ["if","else","elif","for"," while"]
    with open(python_filename) as python_file:
        with open(output_filename, "w") as output_file:
            function_list = []
            doc_string_list = []
            for line in python_file:
                line = line.rstrip("\n")
                row = line.split("\t")
                
                for data in row:
                    line_split = data.split(" ")
                    print(line_split)
                    if "def" in line_split:
                        function_header = " ".join(line_split[1:])
                        function_list.append(function_header)
                    for item in line_split:
                        ch_list = []
                        for ch in item:
                            ch_list.append(ch)
                        print(ch_list)
              
            for i in range(len(function_list)):   
                function_header = function_list[i]     
                output_file.write(f"{i+1}. {function_header}\n")

                for i in range(len(doc_string_list)):    
                    function_doc_string = doc_string_list[i]
                    output_file.write(f"{function_doc_string}\n")



extract_functions("python_script.py","python_functions.txt")