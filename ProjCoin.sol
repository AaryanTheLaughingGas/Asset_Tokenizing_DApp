// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import "@openzeppelin/contracts@4.4.0/token/ERC20/ERC20.sol";

contract ProjCoin is ERC20 {
    constructor() ERC20("ProjCoin", "PBJ") {
        _mint(msg.sender, 1000 * 10 ** decimals());
    }
}