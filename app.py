from  flask import Flask
from  flask import render_template
from  flask import request
from  flask import jsonify

app = Flask(__name__)

def remove_common_chars(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)
    
    for char in name1_list[:]:  
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
            
    return len(name1_list) + len(name2_list)

def get_flames_result(count):
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]


def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    uncommon_char_count = remove_common_chars(name1, name2)
    result = get_flames_result(uncommon_char_count)
    
    return result

    # name1 = input("Enter the first name: ")
    # name2 = input("Enter the second name: ")

    # relation = flames_game(name1, name2)
    # print(f"The relationship between {name1} and {name2} is: {relation}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flames', methods=['POST'])
def flames():
    data = request.json
    name1 = data['name1']
    name2 = data['name2']
    relation = flames_game(name1,name2)
    return jsonify({'relation':relation})

if __name__ == '__main__':
    app.run(debug=True)

