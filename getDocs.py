import MySQLdb

files = {'ID_Bergus','ID_Burdett','ID_Rusk','ID_Newsom', 'ID_Sisco'}
user = open(data/user);
u = data.readline();
p = data.readline();
db= MySQLdb.connect(user = u, passwd= p,
        host='history-lab.org',db='declassification_frus')
c = db.cursor()
#c.execute("""SELECT raw_body FROM docs WHERE id='frus1961-63v12d251';""")
#row = c.fetchall()
#print(row)
 
for i in files:
    tempfile = open("ID/"+i)
    print("opening ",i)
    for id in tempfile:
        print(id)
        newfile = open("../docs/"+i[3:]+"Docs/"+id+".txt","w+")
        #c.execute(DESC docs)
        #print(c.fetchone())
        c.execute("""SELECT raw_body FROM docs WHERE id=%s""",(id[0:len(id)-1],))
        body = c.fetchone()[0]
        print(body)
        newfile.write(body)
        newfile.close()
    tempfile.close()
db.close()
