## 🏡🪙 Welcome to the _WDapp_ Asset Tokenization Distributed App 🏡🪙

📜 To create your own Token Contract check out:
- [How to run ERC-20 and ERC-721 locally from OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master).
- or, paste this contract (modify as you like) and run it on the [Remix Web IDE](https://remix.ethereum.org/).

For (web) test deploying, you can use the _Remix VM_ to check your contract's functionality\
For deploying using your own Injected Web3 Provider (only works on Web), You can connect Remix to your MetaMask Wallet and run (remember, it costs some test Ether to deploy and to run functions like `transfer` and `approve`).

### ⚠️ Important:
🪙 Remember to create your own project [API key Infura](https://docs.infura.io/dashboard/create-api) and get your Ethereum or Testnet (I have used Sepolia Testnet) endpoint URL and Replace it in the WDApp code `line 9 infura_url`.\
🪙 Once you deploy your contract, you will receive the Contract ABI and Address. Save the ABI (in-place of this one in the repo) and replace those in the code too `line 23 contract_address` and `line 24 "contract_abi.json"`.

👉 API keys have rate limits, so be sure to use them carefully! :)

---
💡 This is a web deployment based app that supports local hosting on Vercel and Streamlit. I will be working on the _contract compilation_ using `npm hardhat` 👷 and update this repo to completely make it local 💻!

To try local compilation yourself, check out this [link](https://www.infura.io/blog/post/getting-started-with-infura-28e41844cc89).
