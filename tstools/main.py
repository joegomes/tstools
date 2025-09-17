import argparse
from .io import load_config
from .workflow import run_workflow

def main():
    parser = argparse.ArgumentParser(description="Run tstools workflow")
    parser.add_argument("config", help="YAML config file")
    args = parser.parse_args()

    config = load_config(args.config)
    final_atoms = run_workflow(config)

    final_atoms.write("out.xyz")

if __name__ == "__main__":
    main()
