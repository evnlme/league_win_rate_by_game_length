from pathlib import Path
from subprocess import run

script_path = Path(__file__).resolve().parent
venv_path = script_path / '.venv'
python_path = venv_path / 'Scripts' / 'python'
requirements_path = script_path / 'requirements.txt'

if not venv_path.exists():
    args = ['python', '-m', 'venv', str(venv_path)]
    run(args=args, cwd=script_path)

    pip_install = [str(python_path), '-m', 'pip', 'install']

    args = [*pip_install, '--upgrade', 'pip']
    run(args=args, cwd=script_path)

    args = [*pip_install, '--requirement', str(requirements_path)]
    run(args=args, cwd=script_path)

args = [str(python_path), '-m', 'jupyter', 'lab']
run(args=args, cwd=script_path)
