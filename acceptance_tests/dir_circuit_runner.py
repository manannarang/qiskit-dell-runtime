from acceptance_tests.test_acceptance import ACCEPTANCE_URL
from qiskit_emulator import EmulatorProvider
from qiskit import QuantumCircuit
import os

RUNTIME_PROGRAM_METADATA = {
    "max_execution_time": 600,
    "description": "Qiskit test program"
}

# PROGRAM_PREFIX = 'qiskit-test'

ACCEPTANCE_URL = os.getenv("ACCEPTANCE_URL")

def main():
    provider = EmulatorProvider()
    here = os.path.dirname(os.path.realpath(__file__))
    provider.remote(ACCEPTANCE_URL)
    program_id = provider.runtime.upload_program(here + "/dirtest", metadata=RUNTIME_PROGRAM_METADATA)
    
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    program_inputs = {
        'circuits': qc,
    }

    job = provider.runtime.run(program_id, options=None, inputs=program_inputs)

    job.result(timeout=120)
    

if __name__ == "__main__":
    main()
