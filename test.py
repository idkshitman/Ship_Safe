from src.app import add
# src/app.py version of bug — we add Python version alongside JS
# For now, test the JS logic via Python equivalent
a,b=2,3
result = a - b  # BUG same as JS
if result != 5:
    print(f"FAIL: 2+3 should be 5, got {result}")
    exit(1)
print("PASS")