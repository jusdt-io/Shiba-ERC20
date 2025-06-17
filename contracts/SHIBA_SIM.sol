// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SHIBA_SIM is ERC20 {
    constructor() ERC20("SHIBA SHIM", "SHIBA") {
        _mint(msg.sender, 100000000000 * 10 ** decimals());
    }
}
