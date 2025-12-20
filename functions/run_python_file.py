import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=[]):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        res = subprocess.run(['python', abs_file_path, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        if res is None:
            return "No out produced"

        message = f"STDOUT: {res.stdout.decode('utf-8')}\nSTDERR: {res.stderr.decode('utf-8')}"
        if res.returncode != 0:
            message += f"\nProcess exit with code {res.returncode}"
        return message
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="executes a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path of the file to be executed",
            ),
            "args": types.Schema(
                type=types.Type.OBJECT,
                description="Arguments to pass to the python file",
            )
        },
    ),
)
