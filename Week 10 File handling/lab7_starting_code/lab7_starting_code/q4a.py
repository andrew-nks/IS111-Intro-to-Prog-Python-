with open("transactions.txt", "r") as input:
    with open("transactions-output-1.txt", "w") as output:
        for line in input:
            line = line.rstrip("\n")
            column = line.split("\t")
            price_str = column[2]
            price = float(price_str.replace("$",""))
            if price >= 30:
                output.write("\t".join(column)+ "\n")
