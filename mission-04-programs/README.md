# Mission 4 — How programs run

## 1. Task / objective
Run a simple Python program and compare a compiler with an interpreter.

## 2. Work completed
The `hello.py` file prints a greeting. Run it from the repository root:

```bash
python3 mission-04-programs/hello.py
```

Expected output:

```text
Hello from Python
```

### Compiler and interpreter comparison
| Point | Compiler | Interpreter |
|---|---|---|
| Translation | Usually translates source code into another form before execution | Executes source code through an interpreter, often as it processes it |
| Output | May produce a separate executable or object code | Often does not create a standalone native executable |
| Example | C compiler such as `clang` | Python interpreter |
| Advantage | Can produce fast executable programs after compilation | Convenient for testing and interactive development |

In practice, language implementations can combine compilation and interpretation techniques. This table is a beginner-level comparison.
