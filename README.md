# SHIBA SHIM (SHIBA SIM) Token

SHIBA SHIM is a meme token on Ethereum with Uniswap V3 and Curve pool integrations.

## Token Details
- Name: SHIBA SHIM
- Symbol: SHIBA
- Decimals: 18
- Total Supply: 100,000,000,000 SHIBA
- Contract Address: [0x45960c7afBB50C24ab7a1130216CEa8B049a36Dc](https://etherscan.io/address/0x45960c7afBB50C24ab7a1130216CEa8B049a36Dc)
- Source: [contracts/SHIBA_SIM.sol](contracts/SHIBA_SIM.sol)
- Compiler: v0.8.20+commit.a1b79de6
- License: MIT

## Liquidity Pools
- **Curve Pool**: [0x4f493b7de8aac7d55f71853688b1f7c8f0243c85](https://etherscan.io/address/0x4f493b7de8aac7d55f71853688b1f7c8f0243c85)
  - Paired with JUSDC
- **Uniswap V3 Pool (0.3% Fee)**
  - Tick Range: 83369 to 84883
  - Position NFT: Listed on [Magic Eden](https://magiceden.us) for 0.001 WETH (+27.6% above 0.0008 ETH floor, highest offer $3, expires in 346d 11h 22m)

## Directory Structure
- `contracts/`: Smart contract (`SHIBA_SIM.sol`)
- `assets/`: Images (`logo.png`, `profile.png`, `verified_badge.png`, `shiba_logo.png`)
- `scripts/`: Utilities (`make_badge.py`, `make_profile.py`, `verified-badge.py`, `shiba_browser_logo.py`)
- `pool/`: Pool configs (`uniswap_v3_config.json`, `curve_pool_config.json`)
- `shiba.json`: Token metadata
- `info.json`: Additional metadata
- `whitepaper.md`: Documentation

## Official Links
- Website: [https://jusdt.io](https://jusdt.io)
- Twitter: [@Jsonusdt](https://twitter.com/Jsonusdt)
- Telegram: [t.me/jusdt_stablecoin](https://t.me/jusdt_stablecoin)
- Email: [admin@jsonusdt.com](mailto:admin@jsonusdt.com)

## License
MIT License
