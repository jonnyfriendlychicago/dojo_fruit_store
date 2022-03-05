from flask import Flask, render_template, request, redirect

from datetime import datetime
from pytz import timezone

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # print(request.form)
    
    strawberryCount = request.form['strawberry']
    raspberryCount = request.form['raspberry']
    appleCount = request.form['apple']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    itemTotal = int(strawberryCount) + int(raspberryCount) + int(appleCount)
    dateTimeObj = datetime.now()
    purchaseDateTime = dateTimeObj.strftime("%B %-d, %-I:%M:%S %p") 
    # putyz = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    # %Y %H:%M:%S instead: 

    print(f"Charging {firstName} {lastName} for {itemTotal} fruits.")

    return render_template("checkout.html", 
    display_strawberryCount = strawberryCount,
    display_raspberryCount = raspberryCount,
    display_appleCount = appleCount, 
    display_firstName = firstName, 
    display_lastName = lastName, 
    display_studentId = studentId, 
    display_itemTotal = itemTotal, 
    display_purchaseDateTime = purchaseDateTime, 
    # display_putyz = putyz
    )


@app.route('/fruits')         
def fruits():
    
    imgCodeStart = "{{url_for('static',filename='img/"
    imgCodeEnd = "')}}"
    
    fruitList = [
        {'fruitName' : 'Apple', 'imageLoc' : 'apple.png', 'altText' : 'picture of an apple'},
        {'fruitName' : 'Blackberry', 'imageLoc' : 'blackberry.png', 'altText' : 'picture of blackberries'}
    ]

    return render_template("fruits.html", display_fruitList = fruitList, display_imgCodeStart = imgCodeStart, display_imgCodeEnd = imgCodeEnd)


if __name__=="__main__":   
    app.run(debug=True)    

# JRF entry 