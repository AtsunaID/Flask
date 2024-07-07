import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Aliases
rc = random.choice
rr = random.randint

def EMAIL(nama, jum):
    try:
        domains = ["@inboxkitten.com", "@gmail.com", "@yahoo.com"]
        bel = ["kanz", "santi", "ryan", "djong", "raffi", "fatih", "rizki", "irwan"]
        bul = ["12773", "rendi", "675", "899", "gaming"]
        
        emails = []
        for x in range(jum):
            BZ = [f'{str(rc(bel))}', f'{str(rr(0, 31))}', f'{str(rc(bul))}', 
                  f'{str(rc(bel))}{str(rr(0, 31))}', f'{x}', 
                  f'{str(rc(bul))}{str(rr(0, 31))}', 
                  f'{str(rc(bel))}{str(rc(bul))}']
            
            email = f"{nama}{rc(BZ)}{rc(domains)}"
            emails.append(email)
        return emails
    except Exception as e:
        return str(e)

@app.route('/generate_emails', methods=['POST'])
def generate_emails():
    data = request.json
    nama = data.get('nama')
    jum = data.get('jum')
    
    if not nama or not isinstance(jum, int):
        return jsonify({"error": "Invalid input"}), 400
    
    emails = EMAIL(nama, jum)
    return jsonify({"emails": emails})

if __name__ == '__main__':
    app.run(debug=True)
