'EOF'
#!/usr/bin/env python3

def main():
    print("Hello Jenkins AutoBuild!")
    print("Python Application Running...")
    result = add(2, 3)
    print(f"2 + 3 = {result}")

def add(a, b):
    return a + b

if __name__ == "__main__":
    main()
EOF

# Create test file
cat > tests/test_main.py << 'EOF'
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from main import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_add()
EOF