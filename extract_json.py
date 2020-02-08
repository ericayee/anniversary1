import csv
import pandas as pd
import json
from datetime import datetime

csvfilename = 'chatdata.csv'
jsonfiles = ['messages/inbox/BenFickes_cw7Pu7TBsQ/message_1.json', 'messages/inbox/BenFickes_cw7Pu7TBsQ/message_2.json', 'messages/inbox/BenFickes_cw7Pu7TBsQ/message_3.json']

#     with open(filename) as json_file:
#         data = json.load(json_file)
#         for m in data['messages']:
#             timestamp = datetime.fromtimestamp(m['timestamp_ms']//1000.0)
#             date = datetime.strftime(timestamp, '%Y-%m-%d')
#             time = datetime.strftime(timestamp, '%H:%M:%S')
#             name = m['sender_name']
#             # print('%s %s %s' % (timestamp, date, time))
#             row = [timestamp, date, time, name]

with open(csvfilename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['timestamp', 'date', 'time', 'name']
    writer.writerow(header)
    for f in jsonfiles:
        with open(f) as json_file:
            data = json.load(json_file)
            for m in data['messages']:
                timestamp = datetime.fromtimestamp(m['timestamp_ms']//1000.0)
                date = datetime.strftime(timestamp, '%Y-%m-%d')
                time = datetime.strftime(timestamp, '%H:%M:%S')
                name = m['sender_name']
                # print('%s %s %s' % (timestamp, date, time))
                row = [timestamp, date, time, name]
                writer.writerow(row)

# why are there empty rows?

# def write_to_csv(filename):
#     csvfile = csv.writer(open("chatdata.csv", "w"))
#     csvfile.writerow(["date"])
#     with open(filename) as fp:
#         soup = BeautifulSoup(fp, 'lxml')
#     dates = soup.findAll('div', {'class' : 'uiBoxWhite'})
#     dates = soup.select('div.uiBoxWhite')
#     for date in dates:
#         data = date.select('div')[-1].text
#         data = ''.join(data.split(',')[:2])
#         csvfile.writerow([data])
#
# def count_messages_bydate():
#     df = pd.read_csv('chatdata.csv')
#     df.groupby(df.date).size().to_csv("count.csv", header=True)
#     ab = pd.read_csv('count.csv')
#     ab['date'] = pd.to_datetime(ab.date)
#     ab.sort_values('date').to_csv("sorted.csv", header=True)
#
# filename = 'messages/inbox/BenFickes_cw7Pu7TBsQ/message_1.html'
# write_to_csv(filename)
# count_messages_bydate()
