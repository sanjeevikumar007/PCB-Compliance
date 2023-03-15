from flask import Flask, render_template, request, session
import level1

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sanjeevi'

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        lead = request.args.get('Lead')
        mercury = request.args.get('Mercury')
        cadmium = request.args.get('Cd')
        hexavalentchromium = request.args.get('HCr')
        polybrominatedbiphenyls = request.args.get('PBB')
        polybrominateddiphenylethers = request.args.get('PBDE')
        session.pop('sent', None)
        if lead != None:
            level1.level1(float(lead), float(mercury), float(cadmium), float(hexavalentchromium), float(polybrominatedbiphenyls), float(polybrominateddiphenylethers))
            session['sent'] = True
        return render_template('webpage.html')
    
    session.pop('sent', None)
    return render_template('webpage.html')

if __name__ == '__main__':

    app.run(debug=True)