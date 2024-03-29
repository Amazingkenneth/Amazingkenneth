import subprocess
import random
import difflib
import time


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
    n = 5000
    test_case_str = f"{n}\n"

    for _ in range(n):
        # Generate l_i and r_i such that 0 < l_i < r_i ≤ 10^9
        l_i = random.randint(1, 10**9 - 1)
        r_i = random.randint(l_i + 1, 10**9)
        # l_i = random.randint(1, 8)
        # r_i = random.randint(l_i + 1, 9)
        k_i = random.randint(1, r_i - l_i)

        test_case_str += f"{l_i} {r_i} {k_i}\n"

    # return f"{n} {k}\n{a}\n{b}\n"
    return test_case_str


def run_executable(executable: str, input_data: str) -> str:
    """
    Runs an executable with the provided input data and captures its output.
    """
    start_time = time.process_time()  # Start measuring CPU time
    result = subprocess.run(
        executable, input=input_data, text=True, capture_output=True, check=True
    )
    end_time = time.process_time()  # End measuring CPU time

    cpu_time = end_time - start_time  # Calculate the CPU time taken
    if cpu_time > 1:
        print(
            f"CPU time for {executable}: {cpu_time:.3f} seconds"
        )  # Print the CPU time

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
    overall_start_time = time.process_time()
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
            overall_end_time = time.process_time()
            overall_cpu_time = (
                overall_end_time - overall_start_time
            )
            print(
                f"Test case {test_case_count} passed. Overall CPU time: {overall_cpu_time:.3f} seconds"
            )


if __name__ == "__main__":
    main()
