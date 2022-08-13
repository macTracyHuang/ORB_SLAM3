
if __name__ == "__main__":
    addr = set()
    with open('csie_oldfp.txt', 'r') as f: 
        for line in f.readlines():
            if  "Position" in line:
                continue
            sub = line[:17]
            if  sub[:15] not in addr:
                addr.add(sub)
    
    with  open("csiebssid.txt",'w') as fout:
        for e in addr:
            fout.write(e.replace(':','').upper()+'\n')

    print("total ap: " + str(len(addr)))