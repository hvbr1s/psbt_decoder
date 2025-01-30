This tool can decode hex PSBT data such as "0x70736274..."

1. Start Bitcoin CLI:
```bash
bitcoind -daemon
```
2. Verify we're fully indexed:
```bash
bitcoin-cli getblockchaininfo
```
3. If needed give system permission to run the tool:
```bash
chmod +x decode_hex_psbt.py
```
4. Run decoder:
```bash
./psbt_decoder.py 0x70736274ff0100...
```