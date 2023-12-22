from flask import Flask, render_template
from firebase_admin import credentials, db, initialize_app

app = Flask(__name__)

cred = credentials.Certificate("credentials.json")
initialize_app(cred, {
    "databaseURL":"https://fir-fd908-default-rtdb.firebaseio.com/"
})
ref = db.reference("/human")
ref1 = db.reference("/hour")
ref2 = db.reference("/mins")
ref3 = db.reference("/sec")
ref4 = db.reference("/DN")
@app.route('/')
def dashboard():
    # Retrieve IoT data from Firebase
    hu = ref.get()
    h = ref1.get()
    m = ref2.get()
    s = ref3.get()
    dn=ref4.get()

    data = {"hu": hu, "h": h, "m": m, "s": s,"dn":dn}
    print(data)
    #data={}
    #Day = [t="DAY" for t in  h if((t>= 18 and t<= 23) or (t>= 0 and t<=6)) t="NIGHT"]
    v_list = []
    # print(ref4.get().values())
    '''for i in ref4.get().values():
        v_list.append(i)
    watt = v_list[-1]
    keys = ['hu', 'h', 'm', "s",'watt']'''
    #data = {ref.get(), ref1.get(),ref2.get(), ref3.get()}

    '''for key, value in zip(keys, values):
        data[key] = value
    #print(data)'''
    return render_template('newdashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
