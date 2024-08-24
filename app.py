from flask import Flask,render_template,jsonify

app = Flask(__name__)

PROBLEMS = [
    {
        id : 1,
        'Organization': 'Godrej Appliances',
        'Problem Statement': 'Innovating for Sustainability: Driving Smart Resource Conservation (Energy & Water) in Home Appliances (Refrigerators, Air Conditioners, Washing Machines and Desert Air Coolers)',
        'Theme': 'Hardware',
        'Funding': 'Rs. 50,00,000'
    },
    {
        id : 2,
        'Organization': 'AICTE',
        'Problem Statement': 'Development of a Paperless Scholarship Disbursement System for PMSSS',
        'Theme': 'Software',
        'Funding': 'Rs. 25,00,000'
    },
    {
        id : 3,
        'Organization': 'AICTE, MIC-Student Innovation',
        'Problem Statement': 'Provide ideas in a decentralized and distributed ledger technology used to store digital information that powers cryptocurrencies and NFTs and can radically change multiple sectors',
        'Theme': 'Blockchain & Cybersecurity',
        'Funding': 'Rs. 15,00,000'
    },
    {
        id : 4,
        'Organization': 'Government of Rajasthan',
        'Problem Statement': 'Intelligent platform to Interconnect Alumni and Student for Technical Education Department, Govt. of Rajasthan',
        'Theme': 'Software',
        'Funding': 'Rs. 2,00,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', problems=PROBLEMS)

@app.route('/api/problems')
def list_problems():
    return jsonify(PROBLEMS)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)