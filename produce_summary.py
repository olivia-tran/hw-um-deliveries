
def get_delivery_data(day_num, file_path):
    """accepts day number and data summary file, outputs a report by day
    """
    print("Day ", day_num)
    the_file = open(file_path)
    for line in the_file:
        line = line.rstrip()  # remove extra whitespace to the right of the line
        words = line.split('|')  # create list of strings separated by '|'
        fruit = words[0]
        count = words[1]
        amount = words[2]
        print(f'Delivered {count} {fruit}s for total of ${amount}. ')
    the_file.close()


get_delivery_data(1, 'um-deliveries-day-1.txt')
get_delivery_data(2, 'um-deliveries-day-2.txt')
get_delivery_data(3, 'um-deliveries-day-3.txt')
