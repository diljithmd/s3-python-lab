import pickle
f=open("text.txt","wb")
pickle.dump(12.3,f)
pickle.dump(12.3,f)
f.close()
