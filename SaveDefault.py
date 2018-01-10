import pickle
f=open("Userdata.txt","wb")
pickle.dump([['USERNAME','NAME','DOB','TAGLINE']],f)
f.close()
