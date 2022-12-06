d = open('input').readline()
print([i+4 for i in range(len(d)-4-1) if len(set(d[i:i+4]))==4][0])
print([i+14 for i in range(len(d)-14-1) if len(set(d[i:i+14]))==14][0])