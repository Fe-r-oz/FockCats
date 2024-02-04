import perceval as pcvl

def get_CCZ():
    processor = pcvl.Processor("SLOS", 6)
    processor.add(4, pcvl.BS.H())
    processor.add(0, pcvl.catalog["postprocessed_ccz"].build_processor())
    processor.add(4, pcvl.BS.H())

    states = {
        pcvl.BasicState([1, 0, 1, 0, 1, 0]): "000",
        pcvl.BasicState([1, 0, 0, 1, 0, 1]): "001",
        pcvl.BasicState([1, 0, 0, 1, 1, 0]): "010",
        pcvl.BasicState([0, 1, 1, 0, 1, 0]): "100",
        pcvl.BasicState([0, 1, 1, 0, 0, 1]): "101",
        pcvl.BasicState([0, 1, 0, 1, 1, 0]): "110",
        pcvl.BasicState([0, 1, 0, 1, 0, 1]): "111"
    }

    ca = pcvl.algorithm.Analyzer(processor, states)

    truth_table = {"000": "000", "001": "001", "010": "010", "011": "011", "100": "100", "101": "101", "110": "110", "111": "111"}
    ca.compute(expected=truth_table)

    pcvl.pdisplay(ca)
    print(f"performance = {ca.performance}, fidelity = {ca.fidelity.real}")

# Uncomment the following line if you want to execute the code when main.py is run
# get_CCZ()
