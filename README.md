#Capstone Project: Plan your Journey Single Hub

# Website Name: TravelSpace

# Ojective
Our main objective is to globalism, organize and standardize the goal of journey towards perfectionism and to offer a variety of travel services to the customers which help us to make a strong relationship with them, so that they can enjoy the trip of their dreams.  

# Project Scope
Plan your journey (Single Hub) is a web application developed for the customers which help them to plan their complete journey according to their own preferences and customization. This project has a vast scope in a present scenario of covid19 and for the future travelling purposes; as this application will help the customers to find out the proper and the safe place for the travelling purpose.              

# Advantages
1.	User can find best deals and packages according to their budget.
2.	This system will provide display platform in where a tourist or the users can find their tour places according to their choices.
3.	This platform will help the users in minimizing their efforts, time and money for planning their journey.  
4.	This application will be easy to use for every common person because of our easy-to-use interface which will help them to navigate through the site and explore each and every feature of it, for the best travelling experiences.

# Product Function
This system provides following functions:
(I) User Sign In-  
•	Description: Ask the user to enter details in order to become        registered user.
•	Input: Name, Email and Password
•	Processing: Storing the values entered in the database and check if the user with same email is available or not. If not store it in database or generate error.
•	Output: Confirmation message registered successfully.

(ii) User Login: 
•	 Description: Initialize the username and password for login
•	 Input: Username and password in alphanumeric value 
•	 Processing: Storing the values and checking whether true or not
•	 Output: Confirmation message login successful else login failed

(iii) Travelling
•	Description: Tours and Travels
•	Input: Place and number of people travelling
•	Processing: Fetch the list of all the tour plans according to details entered by the user.
•	Output: Displays the tour plan with cost as well as places to be visited and
accommodation details and when clicked on (Book button) redirects to payment gateway.
(iv) Hotel Booking:
•	Description: Search and book hotels
•	Input: Place to go and date 
•	Processing: Fetch the list of all the hotels according to details entered by the user.
•	 Output: Displays the list of all the hotels with cost as per the user requirement and when After clicking on (Book button) redirects to payment gateway.

(v) Flight Booking or Train Booking:
•	Description: Search and Book flight or train.
•	Input: Travelling destination required (From & To), date of travelling and number of passengers.
•	Processing: Check all the Flights or Trains available as per the User Input. If available Shows the list of Train or flights and if not Generates and error message.
•	Output: Displays the list of trains or flight available with its fare.
After clicking on (Book Button) redirects to the payment gateway.

(vi) Payment Gateway
•	Description: Payment methods available.
•	Input: Payment via Third-Party-Apps (Paytm, Gpay). Or through Credit Card (Requires CVV and expiry date)
•	Processing: Create an order in your order system and then generate a transaction token by Initiate Transaction API. This will redirect the customer to Razorpay payment page. Customer fills payment details and completes the payment authentication.
•	Output: A message with payment Successful/failed appears.


![pic2](https://user-images.githubusercontent.com/65865851/112747982-8f025480-8fd6-11eb-85a7-965f5fec7440.png)

