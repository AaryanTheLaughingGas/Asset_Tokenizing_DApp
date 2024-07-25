import streamlit as st
import requests
from web3 import Web3
import json
import urllib.parse

def main():
    # Define the Infura URL
    infura_url = "https://sepolia.infura.io/v3/<YOUR_API_KEY>"
    
    # Initialize a Web3 instance
    try:
        if infura_url:
            w3 = Web3(Web3.HTTPProvider(infura_url))
            st.success("Connected to Ethereum node!")
        else:
            st.error("Please provide an Infura URL")
            st.stop()
    except requests.exceptions.RequestException as e:
        st.error(f"Error making request: {e}")

    # Load the contract ABI
    contract_address = "0xeCd49B9Ca959dD3Be9EE2eEe3c56Ece4791a0617"
    with open("contract_abi.json") as f:
        abi = json.load(f)
    
    # Contract instance
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # Get token name
    token_name = contract.functions.name().call()

    # Get token symbol
    token_symbol = contract.functions.symbol().call()

    # Get total supply of tokens
    total_supply = contract.functions.totalSupply().call()
    
    
    # Function to validate Ethereum addresses
    def is_valid_ethereum_address(address: str) -> bool:
        return Web3.is_address(address)
    
    # Define options for the dropdown menu
    options = ["house", "car", "game-assets"]
    
    # Create the app title
    st.title("📦 Asset Transfer App")
    
    # Create the dropdown menu
    selected_asset = st.selectbox("Select Asset Type", options)
    
    # Flags to track validity of addresses
    o_flag = 0
    r_flag = 0
    
    # Create text input fields based on selection
    if selected_asset == "house":
        owner_address = st.text_input("Owner Address")
        if is_valid_ethereum_address(owner_address):
            o_flag = 1
        
        r_add = st.text_input("Recipient Address")
        if is_valid_ethereum_address(r_add):
            r_flag = 2
        
        token_amount = st.number_input("Token Amount", min_value=0.0)
        amount = int(token_amount)
        
        # Add a button for transferring tokens
        if st.button("Transfer Tokens"):
            if o_flag != 1:
                st.error(f"The Owner Address {owner_address} is invalid, try again.")
                st.stop()
                
            if r_flag != 2:
                st.error(f"The Recipient Address {r_add} is invalid, try again.")
                st.stop()
            if owner_address == r_add:
                st.error("Can't double spend!")
                st.stop()
            
            # Create the URL with query parameters
            params = {
                'owner_address': owner_address,
                'recipient_address': r_add,
                'amount': amount,
                'contract_address': contract_address,
                'abi': json.dumps(abi)
            }
            base_url = "https://asset-tokenizing-d-app.vercel.app/"
            url = f"{base_url}?{urllib.parse.urlencode(params)}"
            
            st.markdown(f"[Click here to complete the transaction]({url})")
        
        
        st.subheader("Approve Tokens")
        spender_address = st.text_input("Enter Spender Ethereum Address:")
        approve_amount = st.number_input("Enter Token Amount to Approve:", min_value=0)
        amt = int(approve_amount)

        if st.button("Approve Tokens"):
            if is_valid_ethereum_address(spender_address):
                checksum_spender_address = Web3.to_checksum_address(spender_address)
                params = {
                    'action': 'approve',
                    'spender_address': checksum_spender_address,
                    'amount': amt,
                    'contract_address': contract_address,
                    'abi': json.dumps(abi)
                }
                base_url = "https://asset-tokenizing-d-app.vercel.app/"
                url = f"{base_url}?{urllib.parse.urlencode(params)}"
                st.markdown(f"[Click here to complete the approval]({url})", unsafe_allow_html=True)
            else:
                st.error("Invalid Ethereum address")
        
        
        
        
        if st.button("Name"):
            st.write(f"Token Name: {token_name}")
        if st.button("Symbol"):
            st.write(f"Token Symbol: {token_symbol}")
        if st.button("Total_Supply"):
            st.write(f"Total Supply: {total_supply}")
        
        balcheck = st.text_input("Check Balance of your address")
        if st.button("Check Balance"):
            if is_valid_ethereum_address(balcheck):
                checksum_address = Web3.to_checksum_address(balcheck)
                # Get balance
                balance = contract.functions.balanceOf(checksum_address).call()
                st.write(f"Balance of {balcheck}: {balance} {token_symbol}")
            else:
                st.error("Invalid Ethereum address")

if __name__ == "__main__":
    main()
