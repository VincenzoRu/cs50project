# BOND PRICER WEB APP
#### Video Demo: https://youtu.be/tHtqiml2wM4
#### Description:
# Bond Pricer Web App

## Introduction
The **Bond Pricer Web App** is a simple tool with the goal to be user-friendly and to simplify the calculation of bond prices based on user inputs. The technologies used are Python, Flask, HTML and CSS. This project is developped to help users understand the pricing of a fixed-rate bond with very minimal effort. Just inserts the bond's face value, coupon rate, coupon frequency , time to maturity, and the market interest rate. Then, by clicking the price button, the bond price will be instantly calculated.

This app is designed for professionals, for students, but also anyone who wants to understand how bond prices are calculated.

---

## Motivation and reasons
The choice to create this project was simply due to that Bond pricing is an important task in daily finance job. We do a lot of manual calculations and sometimes they can be tedious and are prone to errors.
By creating this web tool, people can have a simple bond pricing tool with an intuitive interface and with accurate calculations.

---

## Main Features
- **Interactive form for user inputs**
- **Instant bond pricing based on user inputs**
- **Error validation to make sure data entry is correct**

---

## Files + Functionality
List of files of the project + main functionalities:

1. **`app.py`**:
   - This is the main app , written in python using the Flask framework.
   - It has 2 main functions:
     - `pricer` : Which is the main function that calculates the bond based on the user's inputs
     - `validate_inputs` : function that is called before the pricer function to make sure the user's inputs are valid
   - Routes handling:
     - `GET /`: Displays the main form to the users
     - `POST /`: Processes form inputs from the users, validates the data, calculates the bond price, and finally returns the result.
   - Implements the bond pricing logic using the formula for fixed rate bonds.

2. **`templates/index.html`**:
   - The main HTML file that defines the layout of the webpage.
   - Includes the main form with input fields:
     - Face value
     - Coupon rate
     - Coupon frequency
     - Time to maturity
     - Market interest rate
   - Displays the final bond price and potential validation errors.

3. **`static/styles.css`**:
   - Main file for the styling of the webpage. 
   - It centers the form on the page and it aligns the input fields. But it also adds a border radius and a border shadow to make it more elegant and user-friendly.

4. **`README.md`**:
   - Explains the project, the features, the files, the challenges experienced and the future improvements.

---

## Design decisions
- I chose server-side validation for security reasons. This ensures no unintended inputs are used and that all inputs are validated before processing.
- Only 1 webpage for inputs and results. This decision was done to keep the app user-friendly.
- I decided to chose Flask as the main framework for my webapp compared to others ones like Django. Reason is because I got first hand experience during the week9 cs50 and I found it pretty easy to understand. This also allowed me to strengthen the skills I learnt during week9 cs50.

---

## Challenges I experienced and lessons I learnt
- The hardest part I experienced was the bond pricing formula. I initially took a formula I had in one of my old excel files. But the excel formula I used was wrong as it used static variables. It also did not take into account discounted cash flows and annuity calculations. So I checked my financial school notes to check the formula for a fixed-rate formula and convert it into python.
- The second challenge I experienced was mainly CSS related. I wanted to align labels and inputs in the form to make it clean. I did many experimentations. I used cs50.ai to give me some hints, which was helpful to get in the right direction.
- The third and last challenge was everything related to command lines, especially git commands, as I never had experience with git before. I had to learn how to initialize a git, how to commit, how to push etc.

---

## Possible future improvements
Some potential enhancements ideas I may integrate in the future:
1. **Support for more Bond Types**: Eg zero-coupon, floating-rate, callable bonds, etc.
2. **Advanced graphs**: Interactive graphs that shows the bond yield curves
3. **Use of API to get real-time data of interest rates**
4. **Cashflow table**: A table that displays cashflows calculated at present value. This is for a better understanding of the bond's value distributed over time.
 
---

## Conclusion
Building this project was a fun experience. It has helped me to strengthen my skills in Python, Flask and CSS. It also allowed me to deepen my knowledge on the concepts around bond pricing.

Thank you for reading until here :) 
