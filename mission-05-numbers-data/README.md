# Mission 5 — Number systems, Python and text encoding

## 1. Task / objective
Practise decimal, binary and hexadecimal conversions, verify them using Python, explore ASCII and build a small number converter.

## 2. Work completed

### Manual conversions
| Conversion | Answer |
|---|---|
| Decimal 13 to binary | `1101` |
| Decimal 25 to binary | `11001` |
| Binary `1010` to decimal | `10` |
| Binary `1101` to decimal | `13` |
| Hexadecimal `A` to decimal | `10` |
| Hexadecimal `1F` to decimal | `31` |
| Binary `1111` to hexadecimal | `F` |

### Python verification
```python
bin(13)       # '0b1101'
bin(25)       # '0b11001'
int("1010", 2)  # 10
int("1101", 2)  # 13
int("A", 16)    # 10
int("1F", 16)   # 31
hex(15)       # '0xf'
```

### ASCII and encoding
- ASCII code for uppercase `A`: decimal 65.
- ASCII code for lowercase `a`: decimal 97.
- Character encoding maps characters to numeric values so computers can store and exchange text.
- An example outside basic ASCII is `€` (the euro sign), which can be represented in Unicode and encoded using UTF-8.

### Run the converter
From this folder, run `python3 number_converter.py`. Test at least three positive decimal integers and record your actual results: `[FILL IN test values and outputs]`.

## 3. Commands / tools used
Python 3; `bin()`, `hex()` and `int(value, base)`. Actual test command/output: `[FILL IN]`.

## 4. My understanding
Binary uses base 2, decimal uses base 10 and hexadecimal uses base 16. Python provides built-in functions that make conversions easy to verify. Character encodings represent text as numbers/bytes.

## 5. Difficulties faced
[FILL IN actual difficulties.]

## 6. How I resolved them
[FILL IN actual steps.]

## 7. Evidence / files
- `number_converter.py`
- This README and your actual test results.

## 8. Commit details
Suggested commit: `Build and test number conversion program`
Actual commit hash / push status: `[FILL IN]`.
