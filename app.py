#cnn
from helper.cnn import *
#library for flask web
import io, os
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask import render_template_string, stream_with_context
import pymysql.cursors

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app.secret_key = 'ini kunci rahasia'

### Database connection configuration
# def openDb():
#   global conn, cursor
#   conn = pymysql.connect(host="localhost",
#    user="root",
#     password="",
#      database="voice_classif",
#       autocommit=True)
#   cursor = conn.cursor()

cursor=conn=None
def openDb():
  global conn, cursor
  conn = pymysql.connect(host="voice-classif-2.c89o8ilr3iqe.us-east-1.rds.amazonaws.com",
   user="ambyar",
    password="myawsdb221",
     database="voice_classification",
      port=3306,
       autocommit=True)
  cursor = conn.cursor()

def closeDb():
  global conn, cursor
  cursor.close()
  conn.close()

#No caching at all for API endpoints.
@app.after_request
def add_header(response):
  # response.cache_control.no_store = True
  response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '-1'
  return response

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/login', methods=['GET', 'POST'])
def login():
  openDb()
  # Output message if something goes wrong...
  msg = ''
  # Check if "username" and "password" POST requests exist (user submitted form)
  if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']
    # Check if account exists using MySQL
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
    # Fetch one record and return result
    account = cursor.fetchone()
    # If account exists in accounts table in out database
    if account:
      # Create session data, we can access this data in other routes
      session['loggedin'] = True
      session['id'] = account[0]
      session['username'] = account[2]
      # Redirect to home page
      return redirect(url_for('indexDs'))
    else:
      # Account doesnt exist or username/password incorrect
      msg = 'Username atau password salah!'
  closeDb()
  # Show the login form with message (if any)
  return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  # Remove session data, this will log the user out
  session.pop('loggedin', None)
  session.pop('id', None)
  session.pop('username', None)
  # Redirect to login page
  return redirect(url_for('login'))

#fungsi view index() untuk menampilkan data dari database
@app.route('/log')
def log():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  openDb()
  rowData = []
  sql = "SELECT * FROM log_identifikasi"
  cursor.execute(sql)
  results = cursor.fetchall()
  for data in results:
    rowData.append(data)
  closeDb()
  return render_template('log/index.html', rowData=rowData)

#fungsi view index() untuk menampilkan data dari database
@app.route('/ds')
def indexDs():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  openDb()
  rowData = []
  sql = "SELECT * FROM dataset"
  cursor.execute(sql)
  results = cursor.fetchall()
  for data in results:
    rowData.append(data)
  closeDb()
  return render_template('ds/index.html', rowData=rowData)

#fungsi view tambah() untuk membuat form tambah
@app.route('/ds/tambah', methods=['GET','POST'])
def tambahDs():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  if request.method == 'POST':
    kelas = request.form['kelas']
    voice = request.files['voice']
    nm_voice = voice.filename

    openDb()
    sql = "INSERT INTO dataset (kelas, voice_name) VALUES (%s, %s)"
    val = (kelas, nm_voice)
    cursor.execute(sql, val)
    conn.commit()
    closeDb()

    if voice.filename != '':
      os.makedirs(os.path.dirname('static/voice/%s' % (kelas)), exist_ok=True) 
      path = 'static/voice/%s/%s' % (kelas, nm_voice)  
      voice.save(path)

    return redirect(url_for('indexDs'))
  else:
    return render_template('ds/tambah.html')

#fungsi view edit() untuk form edit
@app.route('/ds/edit/<id>', methods=['GET','POST'])
def editDs(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  openDb()
  cursor.execute('SELECT * FROM dataset WHERE id=%s', (id))
  data = cursor.fetchone()
  if request.method == 'POST':
    old_id = request.form['id']
    old_kelas = request.form['old_kelas']
    old_voice = request.form['old_voice']

    kelas = request.form['kelas']
    voice = request.files['voice']
    nm_voice = voice.filename or request.form['old_voice']
    sql = "UPDATE dataset SET kelas=%s, voice_name=%s WHERE id=%s"
    val = (kelas, nm_voice, old_id)
    cursor.execute(sql, val)
    conn.commit()
    closeDb()

    if voice.filename != '':
      path = 'static/voice/%s/%s' % (old_kelas, old_voice)
      if os.path.exists(path):
        os.remove(path)
      voice.save('static/voice/%s/%s' % (kelas, nm_voice))

    return redirect(url_for('indexDs'))
  else:
    return render_template('ds/edit.html', data=data)

#fungsi untuk menghapus data
@app.route('/ds/hapus/<id>', methods=['GET','POST'])
def hapusDs(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  openDb()
  cursor.execute('SELECT * FROM dataset WHERE id=%s', (id,))
  row = cursor.fetchone()
  os.remove('static/voice/%s/%s' % (row[1], row[2])  )
  cursor.execute('DELETE FROM dataset WHERE id=%s', (id,))
  conn.commit()
  closeDb()
  return redirect(url_for('indexDs'))

@app.route("/stream")
def stream():
  openDb()
  cursor.execute('SELECT * FROM hyperparam where id=1')
  row = cursor.fetchone()
  num_epochs = row[1]
  num_batch_size = row[2]
  closeDb()

  @stream_with_context
  def generate():
    model = my_model()
    f = open("temp/log_train.txt", "w")

    stream = io.StringIO()
    model.summary(print_fn=lambda x:stream.write(x + '<br>'))
    summary_string = stream.getvalue()
    stream.close()
    yield summary_string + '\n'
    f.write(f'<ul><li>{summary_string}</li>')

    yield "[INFO] Preparing... <br>\n"
    f.write('<li>[INFO] Preparing...</li>')
    create_metadata()
    x_train, y_train, x_test, y_test = data_train_test()

    yield "[INFO] Training process running... <br>\n"
    f.write('<li>[INFO] Training process running...</li>')
    time.sleep(0.8)
    yield f"[INFO] Parameter set with {num_epochs} epoch and {num_batch_size} batch size <br>\n"
    f.write(f'<li>[INFO] Parameter set with {num_epochs} epoch and {num_batch_size} batch size</li>')
    time.sleep(0.6)
    yield "[INFO] Please wait. don't refresh browser until the finished... <br>\n"
    f.write('<li>[INFO] Please wait. dont refresh browser until the finished...</li>')

    hist = model.fit(x_train, y_train,
     batch_size=num_batch_size,
      epochs=num_epochs,
       validation_data=(x_test, y_test),
        callbacks=[callbacks],
         verbose=0)
    model.save(nama_model)
    save_chart_loss_acc(hist)
    acc, loss = model.evaluate(x_test,y_test, verbose=0)

    yield "<li>Accuracy : {:.2f} Loss : {:.2f} </li>\n".format(acc, loss) 
    f.write('<li>Accuracy : {:.2f} Loss : {:.2f} </li>'.format(acc, loss))
    yield "<li>[INFO] Training process finish...</li>\n"
    f.write('<li>[INFO] Training process finish...</li></ul>')
    f.close()

  return app.response_class(generate())

@app.route('/training', methods=['GET', 'POST'])
def training():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  train_model = False
  openDb()
  cursor.execute('SELECT * FROM hyperparam where id=1')
  rowData = cursor.fetchone()

  if request.method == 'POST':
    if 'train_model' in list(request.form):
      sql = "UPDATE hyperparam SET epoch=%s, bs=%s WHERE id=1"
      val = (request.form['epoch'], request.form['bs'])
      cursor.execute(sql, val)
      conn.commit()
      train_model = True
  closeDb()

  f = open("temp/log_train.txt", "r")
  return render_template('training.html', train_model=train_model, row=rowData, log=f.read())


@app.route('/testing', methods=['GET', 'POST'])
def testing():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')
  
  fileTesting = "temp/test.pkl"
  if request.method == 'POST' and os.path.exist(fileTesting):
    test = pickle.load(open(fileTesting, "rb"))
    model = load_model('models/audio_model.h5')
    y_pred = model.predict(test["x_test"])
    # Argmax will classify the classes which has the highest probability 
    y_predc=y_pred.argmax(axis=1)
    y_testc=test["y_test"].argmax(axis=1)
    #Plot confusion matrix
    cm = confusion_matrix(y_testc, y_predc)
    matrix = pd.DataFrame(data=cm, columns=class_nama, index=class_nama)
    plt.figure()
    sns.heatmap(data=matrix, vmin=-1, vmax=1, annot=True, cmap=plt.cm.Greens_r)
    cmChart = 'static/grafik/confusion_matrix.png'
    if os.path.exists(cmChart):
      os.remove(cmChart)
      plt.savefig(cmChart)

    # Plot classification report
    report=classification_report(y_testc, y_predc, target_names=class_nama, output_dict=True)
    reportFile = open("temp/report.pkl", "wb")
    pickle.dump(report, reportFile)
    reportFile.close()
  else:
    report = pickle.load(open("temp/report.pkl", "rb"))

  return render_template('testing.html', report=report)

def prediksi(f):
  global nama_model
  global num_columns
  CNNmodel = load_model(nama_model)
  test_features = extract_features(f)
  test_features = np.asarray(test_features)
  test_features = test_features.reshape(num_channels,num_rows, num_columns, 1)
  prediction = CNNmodel.predict(test_features)
  return class_nama[np.argmax(prediction)]

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
  global OUTPUT
  OUTPUT = 'Not Recognized'
  f = request.files['audio_data']
  temp_file = secure_filename(f.filename)
  f.save(f'static/voice_upload/{temp_file}')
  OUTPUT=prediksi(f'static/voice_upload/{temp_file}')
  if OUTPUT != 'Not Recognized':    
    openDb()
    sql = "INSERT INTO log_identifikasi (voice_name, result, tgl) VALUES (%s, %s, %s)"
    val = (temp_file, OUTPUT, datetime.now())
    cursor.execute(sql, val)
    conn.commit()
    closeDb()
  return 0

OUTPUT = 'Not Recognized'
@app.route('/')
def main():
  OUTPUT = 'Not Recognized'
  return render_template('index.html', result=0)

@app.route('/result')
def result():
  return render_template('index.html', result=1, output=OUTPUT)

if __name__ == '__main__':
  # Start the Flask server in a new thread
  app.run(host='0.0.0.0', port=80)