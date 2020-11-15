# IoTAnalysis-masked
Test task as part of interview for engineer in IoT company



# Exercise:

Every device belongs to a
particular user and at any given time it is either disconnected or connected to
a particular server.
When a device connects to one of our servers we record
an "online" event. When a device disconnects from one of our servers we record
an "offline" event. Every event contains a timestamp, the id of the device, and
whether the device connected or disconnected. The event also contains the id of
the owner of this device, and the id of the server it connected to.
There are missing events from the stream. For example you
might find an online event for a device that is followed by another online
event, with no offline event in between! Or you might find that an offline
event is followed by another offline event, without an online event in between.
This can happen if, for example, a server crashes and doesn't get a chance to
report a device as offline. Or an online event could be missed during a
database outage.
There is an
accompanying dataset of all the servers that have ever existed together with
the timestamp they were created and destroyed. So, for example, if you have an
online event for a particular server but you see no offline event, then you
could assume that the device was in fact online until that server got
destroyed.

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


### Task 1:
create a stacked chart of **unique online devices per
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

## Findings:
> https://github.com/nalepae/pandarallel great library for parallel processing dataframes