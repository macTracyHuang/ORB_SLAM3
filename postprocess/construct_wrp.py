import pandas as pd
from parse_wifi import parsewifi


def construct(bagname, trajname):

    fp_file = parsewifi(bagname)
    fp = pd.read_csv(fp_file, index_col=False)

    col = ['timestamp', 'x', 'y', 'z', 'q1', 'q2', 'q3','q4']
    traj_file = './traj/' + trajname
    traj = pd.read_csv(traj_file,sep=' ',index_col=False, names=col)

    print("start constructing wrp of " + bagname)

    fp.timestamp = fp.timestamp.round(decimals=0)

    traj.timestamp=traj.timestamp.astype('int64')
    traj.timestamp = traj.timestamp.round(decimals=0)
    traj = traj.drop_duplicates(subset='timestamp', keep="last",inplace=False)
    traj = traj.drop(['y','q1','q2','q3','q4'], axis=1)

    output = pd.merge(traj,fp, how='inner', on='timestamp')
    print("finished constructing wrp of " + bagname)
    return output

def constructList(baglist, trajlist):
    # res = pd.DataFrame()
    for idx, bagname in enumerate(baglist):
        trajname = trajlist[idx]
        filename = 'wrp' + str(idx) + '.csv'
        output = construct(bagname, trajname)
        output.to_csv(filename,index=False)
        # res = pd.concat([res,output], ignore_index=True, sort=True)
    # res = res.fillna(-100)
    # return res
        
if __name__ == "__main__":
    baglist = ['1010.bag']
    trajlist = ['traj1010.txt']
    constructList(baglist, trajlist)

    # output = constructList(baglist, trajlist)

    # output.to_csv(filename,index=False)
    
    # print("save wrp at: " + filename)




    # fp = pd.read_csv('fingerprint.csv', index_col=False)

    # col = ['timestamp', 'x', 'y', 'z', 'q1', 'q2', 'q3','q4']
    # traj = pd.read_csv('traj.txt',sep=' ',index_col=False, names=col)

    # print("start constructing wrp.....")

    # fp.timestamp = fp.timestamp.round(decimals=0)
    # # print(fp.head())

    # traj.timestamp=traj.timestamp.astype('int64')
    # traj.timestamp = traj.timestamp.round(decimals=0)
    # traj = traj.drop_duplicates(subset='timestamp', keep="first",inplace=False)
    # traj = traj.drop(['y','q1','q2','q3','q4'], axis=1)
    # # print(traj.timestamp[0])
    # # print(traj.head())

    # output = pd.merge(traj,fp, how='inner', on='timestamp')

    # filename = "wrp.csv"

    # output.to_csv(filename,index=False)

    # print("save wrp at" + filename)
