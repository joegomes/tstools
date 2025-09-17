from ase.calculators.qchem import QChem
from ase.optimize import BFGS

def run(atoms, global_params, job_params):
    """Run an optimization calculation."""

    system = global_params["system"]
    model = global_params.get("model_chemistry", {}).copy()
    model.update({
        k: v for k, v in job_params.items() if k in ("method", "basis")
    })

    calc = QChem(
        label="opt",
        charge=system["charge"],
        multiplicity=system["multiplicity"],
        method=model["method"],
        basis=model["basis"],
    )

    atoms.set_calculator(calc)

    opt = BFGS(atoms)
    opt.run(fmax=0.05, steps=job_params.get("max_cycles", 200))

    return atoms
