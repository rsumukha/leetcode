for i in range(0,10000):
    if i<10:                           
        os.system("/home/leviathan6/leviathan6 000"+str(i))
    elif i<100:                        
        os.system("/home/leviathan6/leviathan6 00"+str(i))
    elif i<1000:                       
        os.system("/home/leviathan6/leviathan6 0"+str(i))
    else:                              
        os.system("/home/leviathan6/leviathan6 "+str(i))
    time.sleep(0.01)