#library for flask web
import io, os
import time
import shutil
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask import render_template_string, stream_with_context
import pymysql.cursors

###****************************###
#  DEEP CNN LEARNING UTILITIES   #
##################################

###library form deep learning
import os
import numpy as np
import pandas as pd
import librosa
import pickle
import csv  
import tensorflow as tf
import random
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from keras.utils import np_utils
from sklearn.utils import shuffle
from sklearn import metrics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
from werkzeug.utils import secure_filename

##Deep Learning Properties
tf.compat.v1.disable_eager_execution()
max_pad_len = 7223
dataset = 'static/voice'
features = []
header = ['file', 'feature','label']
num_rows = 40
num_columns = 7223
num_channels = 1
num_epochs = 100
num_batch_size = 32
nama_model="models/audio_model.h5"
class_nama=os.listdir(dataset)
class_nama.sort()
num_labels=len(class_nama)
#class_nama=['Abyan', 'Ilmi', 'Itsbat','Lana','Ulya']
#predict_threshold=0.75
accuracy_threshold = 1.0000
val_accuracy_threshold = 1.0000
training_process = False

### Model Fitting Callback
class myCallback(tf.keras.callbacks.Callback):
  def on_train_end(self, logs=None):
    global training_process
    training_process = False
    
  def on_epoch_end(self, epochs, logs={}) :
    global training_process
    global accuracy_threshold
    if((logs.get('accuracy') is not None and logs.get('accuracy') >= accuracy_threshold) 
      and (logs.get('val_accuracy') is not None and logs.get('val_accuracy') >= val_accuracy_threshold)) :
        print('\nSudah mencapai akurasi 100%, maka training dihentikan!')
        self.model.stop_training = True
        training_process = False

      
callbacks = myCallback()

# function to extract feature from audio
def extract_features(file_name):   
  try:
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
    #print(sample_rate)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    #print(mfccs.shape)
    pad_width = max_pad_len - mfccs.shape[1]
    mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
      
  except Exception as e:
    print("Error encountered while parsing file: ", file_name)
    return None 
  return mfccs

## function to extract all audio
def create_metadata():
  global features
  features = []
  with open("metadata.csv", 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    noc=0
    for i in class_nama:
      cursor.execute('SELECT nm_kelas, voice_name from kelas kls, dataset ds WHERE kls.id=ds.kelas AND kls.nm_kelas=%s', (i))
      results = cursor.fetchall()
      for row in results:
        dr=dataset+"/"+row[0]+"/"+row[1]
        data = extract_features(dr)
        features.append([dr,data, noc])
        datacsv=[dr,data, noc]
        writer.writerow(datacsv)
      noc+=1

def data_train_test():
  global features
  global num_labels
  # Convert into a Panda dataframe 
  featuresdf = pd.DataFrame(features, columns=['file','feature','label'])
  featuresdf = shuffle(featuresdf)
  print('Finished feature extraction from ', len(featuresdf), 'files')

  # Convert features and corresponding classification labels into numpy arrays
  X = np.array(featuresdf.feature.tolist())
  y = np.array(featuresdf.label.tolist())

  # Encode the classification labels
  le = LabelEncoder()
  yy = to_categorical(le.fit_transform(y)) 
  # # split the dataset 
  x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.3, random_state = 42)
  x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
  x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)
  num_labels = yy.shape[1]
  data = {
    "x_test" : x_test,
    "y_test" : y_test
  }
  test = open("temp/test.pkl", "wb")
  pickle.dump(data, test)
  test.close()

  return x_train, y_train, x_test, y_test

def my_model():
  global num_labels
  model = Sequential()
  model.add(Conv2D(filters=16, kernel_size=2, input_shape=(num_rows, num_columns, num_channels), activation='relu'))
  model.add(MaxPooling2D(pool_size=2))
  model.add(Dropout(0.2))

  model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
  model.add(MaxPooling2D(pool_size=2))
  model.add(Dropout(0.2))

  model.add(Conv2D(filters=64, kernel_size=2, activation='relu'))
  model.add(MaxPooling2D(pool_size=2))
  model.add(Dropout(0.2))

  model.add(Conv2D(filters=128, kernel_size=2, activation='relu'))
  model.add(MaxPooling2D(pool_size=2))
  model.add(Dropout(0.2))
  model.add(GlobalAveragePooling2D())

  model.add(Dense(num_labels, activation='softmax'))

  model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

  return model

def save_chart_loss_acc(history):
  training_process=False
  plt.figure(figsize=(10, 4))
  plt.subplot(1, 2, 1)
  plt.title('model accuracy')
  plt.ylabel('accuracy')
  plt.xlabel('epoch')
  plt.plot(history.history['accuracy'], color='g')
  plt.plot(history.history['val_accuracy'], color='m')
  plt.legend(['train', 'val'], loc='upper left')

  plt.subplot(1, 2, 2)
  plt.title('model loss')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.plot(history.history['loss'], color='r')
  plt.plot(history.history['val_loss'], color='m')
  plt.legend(['train', 'val'], loc='upper left')
  plt.savefig('static/grafik/train_chart.png')

###**********************###
#    END DEEP LEARNING     #
############################ 

###=>>FLASK ROOT SETTING
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app.secret_key = 'ini kunci rahasia'
###=>>END FLASK ROOT SETTING

###=>>KONEKSI DATABASE
# cursor=conn=None
# def openDb():
#   global conn, cursor
#   conn = pymysql.connect(host="localhost",
#    user="root",
#     password="",
#      database="voice_classif",
#       port=3306,
#        autocommit=True)
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
###=>>ENDKONEKSI DATABASE

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

  rowData = []
  sql = "SELECT * FROM log_identifikasi"
  cursor.execute(sql)
  results = cursor.fetchall()
  for data in results:
    rowData.append(data)
  return render_template('log/index.html', rowData=rowData)

#####################
# KELAS             #
#####################

#fungsi view index() untuk menampilkan kelas
@app.route('/kelas')
def indexKelas():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  rowData = []
  sql = "SELECT * FROM kelas"
  cursor.execute(sql)
  results = cursor.fetchall()
  for data in results:
    rowData.append(data)
  return render_template('kelas/index.html', rowData=rowData)

#fungsi untuk menghapus data
@app.route('/kelas/hapus/<id>', methods=['GET','POST'])
def hapusKelas(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  cursor.execute('SELECT * FROM kelas WHERE id=%s', (id,))
  row = cursor.fetchone()
  #remove folder kelas
  shutil.rmtree(f"static/voice/{row[1]}")   
  cursor.execute('DELETE FROM dataset WHERE kelas=%s', (row[0],))
  conn.commit()
  cursor.execute('DELETE FROM kelas WHERE id=%s', (id,))
  conn.commit()
  return redirect(url_for('indexKelas'))

#fungsi view edit() untuk form edit
@app.route('/kelas/edit/<id>', methods=['GET','POST'])
def editKelas(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  cursor.execute('SELECT * FROM kelas WHERE id=%s', (id))
  data = cursor.fetchone()
  if request.method == 'POST':
    old_id = request.form['id']
    old_kelas = request.form['old_kelas']

    kelas = request.form['kelas'].capitalize()
    cursor.execute('SELECT * FROM kelas WHERE nm_kelas=%s', (kelas))

    if cursor.fetchone() != None:
      return render_template('kelas/edit.html', msg='Nama Kelas Sudah Ada!', data=data)
    else:
      sql = "UPDATE kelas SET nm_kelas=%s WHERE id=%s"
      val = (kelas, old_id)
      cursor.execute(sql, val)
      conn.commit()
      os.rename(f"static/voice/{old_kelas}", f"static/voice/{kelas}")

    return redirect(url_for('indexKelas'))
  else:
    return render_template('kelas/edit.html', data=data, msg='')

#fungsi view tambah() untuk membuat form tambah
@app.route('/kelas/tambah', methods=['GET','POST'])
def tambahKelas():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  if request.method == 'POST':
    kelas = request.form['kelas'].capitalize()
    cursor.execute('SELECT * FROM kelas WHERE nm_kelas=%s', (kelas))

    if cursor.fetchone() != None:
      return render_template('kelas/tambah.html', msg='Nama Kelas Sudah Ada!')
    else :
      sql = "INSERT INTO kelas (nm_kelas) VALUES (%s)"
      val = (kelas)
      cursor.execute(sql, val)
      conn.commit()
      if not os.path.exists(f"static/voice/{kelas}"):
        os.mkdir(f"static/voice/{kelas}")

    return redirect(url_for('indexKelas'))
  else:
    return render_template('kelas/tambah.html', msg='')

####################
#END KELAS         #
####################

#fungsi view index() untuk menampilkan data dari database
@app.route('/ds')
def indexDs():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  rowData = []
  sql = "SELECT ds.id, nm_kelas, voice_name from kelas kls, dataset ds WHERE kls.id=ds.kelas"
  cursor.execute(sql)
  results = cursor.fetchall()
  for data in results:
    rowData.append(data)

  return render_template('ds/index.html', rowData=rowData)

###get semua record kelas dataset
def getKelas():
  rowKelas = []
  cursor.execute("select * from kelas")
  results = cursor.fetchall()
  for row in results:
    rowKelas.append(row)
  return rowKelas

#fungsi view tambah() untuk membuat form tambah
@app.route('/ds/tambah', methods=['GET','POST'])
def tambahDs():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')
  
  if request.method == 'POST':
    kelas = request.form['kelas'].split('::')
    voices = request.files.getlist("voice[]")

    for voice in voices:
      nm_voice = voice.filename
      
      sql = "INSERT INTO dataset (kelas, voice_name) VALUES (%s, %s)"
      val = (kelas[0], nm_voice)
      cursor.execute(sql, val)
      conn.commit()

      if voice.filename != '':
        if os.path.isdir(f'static/voice/{kelas[1]}'):
          path = 'static/voice/%s/%s' % (kelas[1], nm_voice)
          voice.save(path)

    return redirect(url_for('indexDs'))
  else:
    return render_template('ds/tambah.html', rowKelas=getKelas())

#fungsi view edit() untuk form edit
@app.route('/ds/edit/<id>', methods=['GET','POST'])
def editDs(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  cursor.execute('SELECT ds.id, kls.id, nm_kelas, voice_name from kelas kls, dataset ds WHERE kls.id=ds.kelas AND ds.id=%s', (id))
  data = cursor.fetchone()
  if request.method == 'POST':
    old_id = request.form['id']
    old_kelas = request.form['old_kelas']
    old_voice = request.form['old_voice']

    kelas = request.form['kelas'].split('::')
    voice = request.files['voice']
    nm_voice = voice.filename or request.form['old_voice']
    sql = "UPDATE dataset SET kelas=%s, voice_name=%s WHERE id=%s"
    val = (kelas[0], nm_voice, old_id)
    cursor.execute(sql, val)
    conn.commit()
    
    if voice.filename == '' and old_kelas != kelas[1]:
      shutil.move(f"static/voice/{old_kelas}/{old_voice}", f"static/voice/{kelas[1]}/{old_voice}")
  
    elif voice.filename != '':
      path = 'static/voice/%s/%s' % (old_kelas, old_voice)
      if os.path.exists(path):
        os.remove(path)
      voice.save('static/voice/%s/%s' % (kelas[1], nm_voice))

    return redirect(url_for('indexDs'))
  else:
    return render_template('ds/edit.html', data=data, rowKelas=getKelas())

#fungsi untuk menghapus data
@app.route('/ds/hapus/<id>', methods=['GET','POST'])
def hapusDs(id):
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  cursor.execute('SELECT nm_kelas, voice_name from kelas kls, dataset ds WHERE kls.id=ds.kelas AND ds.id=%s', (id,))
  row = cursor.fetchone()
  os.remove(f"static/voice/{row[0]}/{row[1]}")
  cursor.execute('DELETE FROM dataset WHERE id=%s', (id,))
  conn.commit()

  return redirect(url_for('indexDs'))

###>>PAGE PLAYING AUDIO 
@app.route('/play/<table>/<id>', methods=['GET','POST'])
def playAudio(table, id):
  if table == 'ds':
    cursor.execute('SELECT ds.id, nm_kelas, voice_name from kelas kls, dataset ds WHERE kls.id=ds.kelas AND ds.id=%s', (id,))
    row = cursor.fetchone()
    kelas = row[1]
    audioName = row[2]
    fileAudio = 'voice/%s/%s' % (row[1], row[2])
  elif table == 'li':
    cursor.execute('SELECT * FROM log_identifikasi WHERE id=%s', (id,))
    row = cursor.fetchone()
    kelas = 'Guest'
    audioName = row[1]
    fileAudio = 'voice_upload/%s' % (row[1])
  data = [kelas, audioName, fileAudio]
  return render_template('playaudio.html', data=data)

@app.route("/trainmodel")
def trainmodel():
  global training_process
  cursor.execute('SELECT * FROM hyperparam where id=1')
  row = cursor.fetchone()
  num_epochs = row[1]
  num_batch_size = row[2]

  if training_process == True:
    return f"[INFO] Please Wait.. <br> [INFO] Training parameter {num_epochs} epoch and {num_batch_size} batch size <br> [INFO] Model Training in Progress..."

  def generate():
    global training_process
    training_process = True

    print("training start")
    yield "<p> <a href='/training'><< back to training page</a> </p>\n"
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
    f.write('<li>[INFO] Training process finish...</li></ul>')
    f.close()

    hist = model.fit(x_train, y_train,
     batch_size=num_batch_size,
      epochs=num_epochs,
       validation_data=(x_test, y_test),
        callbacks=[callbacks],
         verbose=1)
    model.save(nama_model)
    save_chart_loss_acc(hist)
    acc, loss = model.evaluate(x_test,y_test, verbose=0)

    yield "<li>Accuracy : {:.2f} Loss : {:.2f} </li>\n".format(acc, loss) 
    # f.write('<li>Accuracy : {:.2f} Loss : {:.2f} </li>'.format(acc, loss))
    yield "[INFO] Training process finish... <a href='/training'>back to admin</a> \n"
    training_process = False
    print("training selesai")

  return app.response_class(generate())

@app.route('/training', methods=['GET', 'POST'])
def training():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')

  train_model = False
  cursor.execute('SELECT * FROM hyperparam where id=1')
  rowData = cursor.fetchone()

  if request.method == 'POST':
    if 'train_model' in list(request.form):
      sql = "UPDATE hyperparam SET epoch=%s, bs=%s WHERE id=1"
      val = (request.form['epoch'], request.form['bs'])
      cursor.execute(sql, val)
      conn.commit()
      train_model = False
      return redirect(url_for('trainmodel'))

  f = open("temp/log_train.txt", "r")
  return render_template('training.html', train_model=train_model, training_process=training_process, row=rowData, log=f.read())

@app.route("/stoptrain")
def stoptrain():
  global training_process
  training_process=False
  return redirect(url_for('training'))

@app.route('/testing', methods=['GET', 'POST'])
def testing():
  #jika admin belum login munculkan 404
  if 'loggedin' not in session:
    return render_template('404.html')
  
  fileTesting = "temp/test.pkl"
  if request.method == 'POST' and os.path.exists(fileTesting):
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
    sql = "INSERT INTO log_identifikasi (voice_name, result, tgl) VALUES (%s, %s, %s)"
    val = (temp_file, OUTPUT, datetime.now())
    cursor.execute(sql, val)
    conn.commit()
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
  openDb()
  app.run(host='0.0.0.0',port=8000, debug=True)