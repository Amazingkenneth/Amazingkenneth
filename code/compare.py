import subprocess
import random
import difflib


def compile_cpp(source_file: str, output_executable) -> None:
    """
    Compiles a C++ source file using g++.
    """
    if not source_file.endswith(".cpp"):
        raise ValueError("Source file must have a .cpp extension")
    if output_executable is None:
        output_executable = source_file.removesuffix(".cpp")
    try:
        subprocess.run(
            ["g++", source_file, "-Wall", "-o", output_executable], check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"{__file__}: Failed to compile {source_file}. Error: {e}")
        raise


def generate_data() -> str:
    """
    Generates test data.
    Customize this function based on the input format your programs expect.
    """
    n = 5
    a = " ".join(str(random.randint(1, 100)) for _ in range(n))
    return f"{n}\n{a}\n"


def run_executable(executable: str, input_data: str) -> str:
    """
    Runs an executable with the provided input data and captures its output.
    """
    result = subprocess.run(
        executable, input=input_data, text=True, capture_output=True, check=True
    )
    return result.stdout.strip()


def compare_outputs(output1: str, output2: str) -> bool:
    """
    Compares two outputs, ignoring differences in whitespace.
    """
    output1_lines = output1.strip().splitlines()
    output2_lines = output2.strip().splitlines()

    # Using difflib to compare outputs line by line, ignoring whitespace
    diff = list(difflib.unified_diff(output1_lines, output2_lines, lineterm=""))
    if diff:
        return False
    return True


def main():
    executable1 = "./brute_force_program"
    executable2 = "./solution_program"

    compile_cpp("bf.cpp", executable1)
    compile_cpp("sol.cpp", executable2)

    test_case_count = 0
    while True:
        test_case_count += 1
        data = generate_data()

        try:
            output1 = run_executable(executable1, data)
            output2 = run_executable(executable2, data)
        except subprocess.CalledProcessError as e:
            print(f"Error running executables. Error: {e}")
            continue

        if not compare_outputs(output1, output2):
            print(f"Mismatch found in test case {test_case_count}:")
            print(f"Data:\n{ '=' * 20 }\n{data}")
            print(f"{executable1}:\n{ '=' * 20 }\n{output1}")
            print(f"{executable2}:\n{ '=' * 20 }\n{output2}")
            break
        if test_case_count % 100 == 0:
            print(f"Test case {test_case_count} passed.")


if __name__ == "__main__":
    main()
