from ase.calculators.qchem import QChem

def run(atoms, global_params, job_params):
    """Run a single-point energy calculation with Q-Chem."""

    # Pull system-level info from global
    system = global_params["system"]

    # Start with global model chemistry
    model = global_params.get("model_chemistry", {}).copy()

    # Override with job-level model chemistry if provided
    model.update({
        k: v for k, v in job_params.items() if k in ("method", "basis")
    })

    calc = QChem(
        label="sp",
        charge=system["charge"],
        multiplicity=system["multiplicity"],
        method=model["method"],
        basis=model["basis"],
    )

    atoms.set_calculator(calc)

    energy = atoms.get_potential_energy()
    print(f"[Singlepoint] {model['method']}/{model['basis']} Energy = {energy:.6f} eV")

    return atoms
