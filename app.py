from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#My bond pricing function
def pricer(face_value,coupon_rate,coupon_frequency,maturity,market_rate):

    #calculate the total number of periods and periodic market rate
    total_periods = int(maturity * coupon_frequency)
    periodic_market_rate = market_rate / 100 / coupon_frequency

    #calculate the coupon payment
    coupon_payment = (face_value * coupon_rate / 100) / coupon_frequency

    #calculate the present valu of coupon payments
    coupon_pv = sum(coupon_payment / (1 + periodic_market_rate) ** t for t in range(1, total_periods + 1))

    #calculate the present value of the face value
    face_value_pv = face_value / (1 + periodic_market_rate) ** total_periods

    bond_price = coupon_pv + face_value_pv

    return bond_price

#My helper function
def validate_inputs(face_value, coupon_rate, coupon_frequency, maturity, market_rate):
    errors = []
    if not all([face_value, coupon_rate, coupon_frequency, maturity, market_rate]):
        errors.append("All fields are required.")
    if face_value <= 0:
        errors.append("Face value must be greater than 0.")
    if coupon_rate < 0 or coupon_rate > 100:
        errors.append("Coupon rate must be between 0 and 100.")
    if coupon_frequency not in [1, 2, 4, 12]:
        errors.append("Invalid coupon frequency selected.")
    if maturity <= 0:
        errors.append("Maturity must be greater than 0.")
    if market_rate < 0:
        errors.append("Market rate must be non-negative.")
    return errors


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    bond_price = None

    if request.method == "POST":
        face_value = request.form.get("face_value", type=int)
        coupon_rate = request.form.get("coupon_rate",type=float)
        coupon_frequency = request.form.get("coupon_frequency", type=int)
        maturity = request.form.get("maturity",type=int)
        market_rate = request.form.get("market_rate",type=float)

        errors = validate_inputs(face_value, coupon_rate, coupon_frequency, maturity, market_rate)
        
        if errors:
            error = "; ".join(errors)
        else:
            bond_price = pricer(face_value,coupon_rate,coupon_frequency,maturity,market_rate)
       
        return render_template("index.html",error=error,bond_price=bond_price,face_value=face_value,coupon_rate=coupon_rate,coupon_frequency=coupon_frequency, maturity=maturity, market_rate=market_rate)

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  
   
