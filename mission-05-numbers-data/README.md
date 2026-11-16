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
