text = "contoh text pada file \n ini line baru dari"

saveFile = open("contohfile.txt","w")
saveFile.write(text)
saveFile.close()