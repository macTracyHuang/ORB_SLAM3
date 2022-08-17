import pandas as pd

fp = pd.read_csv('fingerprint.csv', index_col=False)

col = ['timestamp', 'x', 'y', 'z', 'q1', 'q2', 'q3','q4']
traj = pd.read_csv('traj.txt',sep=' ',index_col=False, names=col)


fp.timestamp = fp.timestamp.round(decimals=0)
# print(fp.head())

traj.timestamp=traj.timestamp.astype('int64')
traj.timestamp = traj.timestamp.round(decimals=0)
traj = traj.drop_duplicates(subset='timestamp', keep="first",inplace=False)
traj = traj.drop(['z','q1','q2','q3','q4'], axis=1)
# print(traj.timestamp[0])
# print(traj.head())

output = pd.merge(traj,fp, how='inner', on='timestamp')

output.to_csv("wrp.csv",index=False)

