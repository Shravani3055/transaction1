import streamlit as st
import random

st.title("🧱 Blockchain Simulator")

# Section 1: Display basic blockchain info
st.header("🔢 Block Details")

block_number = 123456
transaction_fee = 0.0005
wallet_address = "0xABC123XYZ"
transactions = [10, 50, 200, 5]

transaction1 = {
    "sender": "Alice",
    "receiver": "Bob",
    "amount": 50
}

if st.button("Show Block Info"):
    st.write("**Block Number:**", block_number)
    st.write("**Transaction Fee:**", transaction_fee)
    st.write("**Wallet Address:**", wallet_address)
    st.write("**Transactions List:**", transactions)
    st.write("**Transaction Details:**", transaction1)

st.divider()

# Section 2: Display individual transactions
st.header("📜 Transaction Amounts")

transactions_list = [10, 20, 50, 100]

if st.button("Show All Transactions"):
    for amount in transactions_list:
        st.write("Transaction Amount:", amount)

st.divider()

# Section 3: Mining blocks simulation
st.header("⛏️ Mining Blocks")

if st.button("Start Mining Blocks"):
    for block in range(1, 6):
        st.success(f"Mining Block: {block}")

st.divider()

# Section 4: While Loop Example - Blockchain task
st.header("🔁 Blockchain Tasks Repeater")

if st.button("Run Blockchain Tasks"):
    count = 0
    while count < 3:
        st.write("Blockchain task")
        count += 1

st.divider()

# Section 5: Balance Deduction Simulation
st.header("💸 Balance Payment Processing")

if st.button("Process Payments"):
    balance = 100
    while balance > 0:
        st.warning(f"Processing payment... Remaining balance: {balance}")
        balance -= 20

st.divider()

# Section 6: Guess the Transaction Game
st.header("🎯 Guess the Transaction Amount")

transactions_game = [100, 200, 300, 400, 500]
chosen_transaction = random.choice(transactions_game)

guess = st.number_input("Enter your guess:", min_value=100, max_value=500, step=100)

if st.button("Submit Guess"):
    if guess == chosen_transaction:
        st.success("🎉 Congratulations! You guessed the right amount.")
    else:
        st.error(f"❌ Wrong! The correct transaction was {chosen_transaction}.")

