# coding=utf-8
import rosbag
import rospy
import sys
import os
from collections import defaultdict


if __name__ == "__main__":
    file_num = len(sys.argv) - 1
    if file_num <= 0:
        print("Not enough input files, exit. You should input one bag filepath at least.")
    else:
        bag_path = sys.argv[1]
        save_path = os.getcwd() + os.path.sep + "fingerprint.csv"
        fout = open(save_path, "w")
        data = defaultdict(list)
        unique_addr = dict()

        csiebssid = []
        with  open("csiebssid.txt",'r') as f:
            for id in f.read().splitlines():
                csiebssid.append(id)


        # print(csiebssid)
        # raise
        with rosbag.Bag(bag_path, 'r') as bag:
            for topic, msg, t in bag.read_messages():
                cur_time = msg.header.stamp.to_sec()
                if topic == "/wifi_fp":
                    # print(msg.list)
                    timestr = "%.6f" % msg.header.stamp.to_sec() # s TUM
                    fingerprint = msg.list
                    for addressRSSI in fingerprint:
                        bssid = addressRSSI.address
                        rssi = int(addressRSSI.rssi)
                        data[timestr].append([bssid, rssi])
                        if bssid in unique_addr:
                            unique_addr[bssid]+=1
                        else:
                            unique_addr[bssid]=1

                    print(timestr + " finished")

        # print(unique_addr)
        # remove bssid not exit in old fingerprint collected by senors or appear less than 1/5th  of total timestamps
        # maybe need to remain addr with '**' in wifi_ap code : multple bssid => virtual ap
        for k in list(unique_addr.keys()):
            if k  not in csiebssid or unique_addr[k] < len(data) / 20:
                del unique_addr[k]

        num_ap = len(unique_addr)
        print("total ap: " +  str(num_ap))
        addr_map = {} # look up idx from bssid
        fout.write("timestamp ")

        for idx, addr in enumerate(unique_addr):
            addr_map[addr] = idx
            fout.write(addr + ' ')
        
        fout.write('\n') # end bssid title 

        wrp = [[0]*num_ap for _ in range(len(data))] # row: timestamp , col: rssi of bssid 

        count = 0
        minAp = 1e9
        maxAp = 0
        for t, v in data.items():
            minAp = min(minAp, len(v))
            maxAp = max(maxAp,len(v))
            for bssid, rssi in v:
                if bssid in unique_addr:
                    idx = addr_map[bssid]
                    wrp[count][idx] = rssi
            count+=1

        print("min_ap: " + str(minAp) + ", max_ap:" + str(maxAp))
        assert count == len(data)

        keys = sorted(data.keys())

        for i, t in enumerate(keys):
            fout.write(t + ' ')
            for rssi in wrp[i]:
                fout.write(str(rssi) + ',')
            fout.write('\n')


        # fout.close()
        print("Timestamp file has been saved at:" + save_path)