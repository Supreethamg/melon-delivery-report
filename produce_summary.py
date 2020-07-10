def produce_summary(day_no, file_name):
    ''' Prints summary report when day number and
     path to the file is passed in parameter of the function.'''
    print("Day ", day_no)
    #opens the file
    the_file = open(file_name)
    #Generates report by reading line by line.
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[0]
        amount = words[0]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()
#calling the produce_summary function with different day number and file names
produce_summary(1, "um-deliveries-20140519.txt")
produce_summary(2, "um-deliveries-20140520.txt")
produce_summary(3, "um-deliveries-20140521.txt")