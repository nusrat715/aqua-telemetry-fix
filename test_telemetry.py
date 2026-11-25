from telemetry import depth_status

test_cases = [
    (None, "NO DATA"),
    (1.9, "LIVE"),
    (2.0, "STALE"),
    (3.0, "STALE")
]

for age, expected in test_cases:
    try:
        assert depth_status(age) == expected
        print(f"PASS: age={age}, expected={expected}")
    except AssertionError:
        print(f"FAIL: age={age}, expected={expected}, got={depth_status(age)}")
