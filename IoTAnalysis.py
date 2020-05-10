import pandas as pd
import datetime

def prepare_final(row):
    if(row.prev_server_id == None):
        return False
    elif(row.connected == False and row.prev_connected == False):
        return True
    elif(row.prev_connected and row.connected == False
        and row.server_id != row.prev_server_id):
        return True

print("start:{}".format(datetime.datetime.now()))
names=['id','created_at','destroyed_at']
servers = pd.read_csv('data/servers.csv',names=names)


names = ['timestamp','device_id', 'user_id','server_id','connected']
events = pd.read_csv('data/connectivity_events.csv',names=names)#,nrows=1000)


pd.set_option('display.max_columns',None)


events_merged=events.merge(servers,left_on='server_id',right_on='id')

events_merged['prev_server_id']=(events_merged.sort_values(by=['timestamp'], ascending=True)
                               .groupby(['device_id'])['server_id'].shift(1))
events_merged['prev_connected']=(events_merged.sort_values(by=['timestamp'], ascending=True)
                         .groupby(['device_id'])['connected'].shift(1))
events_merged['prev_timestamp']=(events_merged.sort_values(by=['timestamp'], ascending=True)
                                         .groupby(['device_id'])['timestamp'].shift(1))

events_merged['ignored']=events_merged.apply(prepare_final,axis=1)
print("end:{}".format(datetime.datetime.now()))
"""
Your first task is to create a stacked chart of **unique online devices per
day**, segregated by fleet size. The fleet size is an attribute of each user
and is defined as the number of online devices that this user had at a
particular day. You can split the dataset in the following fleet sizes:

* 1-2 devices
* 3-9 devices
* 10-99 devices
* 100-999 devices

A device should be counted as online for a particular day if it was online for
any amount of time during that day. For example, a device that appear online
for only a second should still be counted for that day.

The specific rules we have selected to deal with problematic sections
of a device's timeline can be summarised in the following table:

| current event | current server | next event | next server | rule        |
|---------------|----------------|------------|-------------|-------------|
| online        | X              | online     | X           | Assume device was online from current event's timestamp until next event's timestamp
| online        | X              | online     | Y           | Assume device was online from current event's timestamp until X's destruction time or next event's timestamp, whichever is smaller
| online        | X              | offline    | X           | Normal case
| online        | X              | offline    | Y           | Assume device was online from current event's timestamp until X's destruction time. Ignore next event.
| offline       | X              | online     | X           | Normal case
| offline       | X              | online     | Y           | Normal case
| offline       | X              | offline    | X           | Ignore next event
| offline       | X              | offline    | Y           | Ignore next event
"""