import streamlit as st

# Your business logic (modified slightly for web use)
class BankApplication:
    bank_name = 'SBI'

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction successful. Collected ₹{amount}. Remaining balance: ₹{self.balance}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount} Deposited Successfully. Total balance: ₹{self.balance}"

    def check_balance(self):
        return f"Available Balance: ₹{self.balance}"


# Streamlit UI
st.title("🏦 Bank Application")

name = st.text_input("Enter Name")
account_number = st.text_input("Enter Account Number")
age = st.number_input("Enter Age", min_value=1)
mobile_number = st.text_input("Enter Mobile Number")
balance = st.number_input("Enter Initial Balance", min_value=0)

if st.button("Create Account"):
    user = BankApplication(name, account_number, age, mobile_number, balance)
    st.success("Account Created Successfully!")

    option = st.selectbox("Choose Operation", ["Deposit", "Withdraw", "Check Balance"])

    if option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=1)
        if st.button("Deposit"):
            st.success(user.deposit(amount))

    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            st.success(user.withdraw(amount))

    elif option == "Check Balance":
        if st.button("Check"):
            st.info(user.check_balance())

    #venv\Scripts\activate py -m streamlit run app.py