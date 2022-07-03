# import csv
# # with open('contacts.csv', newline='') as csvfile:
# #     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
# #     for row in spamreader:
# #         print(row)
# #         print(type(row))

# # Spam, Spam, Spam, Spam, Spam, Baked Beans
# # Spam, Lovely Spam, Wonderful Spam

# # with open('contacts.csv', 'r+', newline='') as csvfile:
# #     spamwriter = csv.writer(csvfile, delimiter=',',
# #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
# #     spamwriter.writerow(['bu eka', '+67544'])
# #     spamwriter.writerow(['Spam', '+76786'])

# import csv

# with open('contacts.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     # writer.writerow({'first_name': 'Baked ,  snkjnksd'})
#     # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful'})
#     # writer.writerow({'last_name': 'Spam'})

from get_message_info import *

data = getDictAllData()
print(data)

addData('idx', '0')
addData('nama','Egi')
addData('kelas', '7a')
addData('pesan', 'nskanknxknklsanlnaslkndn')

addData('idx', '0')

