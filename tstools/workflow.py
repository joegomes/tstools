from tstools.io import load_geometry
from tstools.jobs import optimization, singlepoint

JOB_REGISTRY = {
    "optimization": optimization.run,
    "singlepoint": singlepoint.run,
}

def run_workflow(config):
    atoms = load_geometry(config["global"]["geometry"])
    
    for job in config["jobs"]:
        job_name = job["name"]
        job_params = job.get("parameters", {})
        if job_name not in JOB_REGISTRY:
            raise ValueError(f"Unknown job: {job_name}")
        atoms = JOB_REGISTRY[job_name](atoms, config["global"], job_params)
    return atoms

