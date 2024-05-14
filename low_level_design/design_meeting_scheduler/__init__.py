"""
Design Pattern:
---------------

In the meeting scheduler design, the entire system revolves around the scheduler which is responsible
for scheduling meetings.
To create a robust design, it is not possible that there can be more than one instance for the scheduler.
Therefore, we use the Singleton design pattern to ensure that only one instance of the scheduler is created
                     --------------------------
and that this instance has a global point of access.
"""