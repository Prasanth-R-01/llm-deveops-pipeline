from app import run_threads

def test_thread_race_condition():
    result = run_threads()
    assert result == 5, f"counter={result}"