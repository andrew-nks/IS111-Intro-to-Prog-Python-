with open("transactions.txt", "r") as input:
        date_list = []
    
        for line in input:
            line = line.rstrip("\n")
            column = line.split("\t")
            date = column[0]
            unique_month = date[3:]
            if unique_month not in date_list:
                date_list.append(unique_month)
            
        # print(date_list)
        
with open("transactions-output-2.txt", "w") as output:
    for new_date in date_list:
        total_amount = 0
        transaction_list = []
        with open("transactions.txt", "r") as input:
            for line in input:
                line = line.rstrip("\n")
                column = line.split("\t")
                date = column[0]
                unique_month = date[3:]
                shop = column[1]
                amount_str = column[2]
                amount = float(amount_str.replace("$",""))
                if new_date == unique_month:
                    total_amount += amount
                    transaction_list.append(shop + "\t" + amount_str)

        output.write(f"{new_date}: total transaction amount is ${total_amount}\n")
        for data in transaction_list:
            output.write(f"{data}\n")

        output.write(f"\n")

