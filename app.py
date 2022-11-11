from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)

#CONFIG
#db = yaml.load(open('db.yaml'))
db = yaml.safe_load(open('db.yaml'))

app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# @app.route('/student')

# def student():
    
#    cur = mysql.connection.cursor()
#    resultValue = cur.execute("SELECT * FROM student")
#    print("hi executed DB fetch")
#    if resultValue>0:
#      userDetails = cur.fetchall()
#      return render_template('student.html',userDetails=userDetails)
    
#      return redirect('/student/update')    
######################################################
@app.route('/student',methods = ['GET','POST'])
def student():
    
   cur = mysql.connection.cursor()
   resultValue = cur.execute("SELECT * FROM student")
   print("hi executed DB fetch")
   
   if resultValue>0:
     userDetails = cur.fetchall()
     x= cur.execute("SELECT RollNo,Name,PaperType FROM studentdata.student WHERE PaperType = 'Test'" ) 
     if x<1:
     #return redirect('/student/update')
     #x= cur.execute("SELECT RollNo,Name,PaperType FROM studentdata.student WHERE PaperType = 'Test' " )
     #else:
      return "<h1> There is no key word called Test in db "
       
   return render_template('student.html',userDetails=userDetails) 
     

@app.route('/update')
def update():
    
     return render_template('index.html')


@app.route('/student/up/lastdb')
def lastdb():
    
     return render_template('lastdb.html')

@app.route('/student/up/lastdb/update2')
def update2():
   
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    userDetails = cur.fetchall()
    return render_template('update2.html',userDetails=userDetails) 

# @app.route('/loop')
# def loop():
#     cur = mysql.connection.cursor()
#     x= cur.execute("SELECT RollNo,Name,PaperType FROM studentdata.student WHERE PaperType = 'Test'" ) 
#     if x>0:
#      return redirect('/student/update')
#      return render_template('index.html')
#      x= cur.execute("SELECT RollNo,Name,PaperType FROM studentdata.student WHERE PaperType = 'Test' " )
#     else:
#      return "<h1> There is no key word called Test in db "  
     
# @app.route('/')
# def firstpage():
#     if (true): 
#      return "<h1> Add 'student' in the end of url</h1>"  
#     return redirect('/student')

@app.route('/student/up',methods = ['GET','POST'])
def index():
    
    if request.method =='POST':
        
       
        userDetails = request.form
        print(userDetails)
        name = userDetails['name']
        print(name)
        cur = mysql.connection.cursor()               
        sql = "UPDATE student SET PaperType ='%s' WHERE PaperType = '%s'" % (name,"Test")        
        cur.execute (sql)
        mysql.connection.commit()
        cur.close()
        return render_template('lastdb.html')
        return 'SUCCESS !!!!!   All the keyword Test got changed to User Input . THERE IS NO KEYWORD TEST IN DATABASE ' 
      
 
    return render_template('index.html')


    
if __name__ == '__main__':
    app.run(debug=True)
    


