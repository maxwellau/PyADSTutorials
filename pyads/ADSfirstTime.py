import pyads

AMSNETID = "10.123.67.6.1.1"
plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
plc.open()
print(f"Connected?: {plc.is_open}")
print(f"Local Address? : {plc.get_local_address()}")
print(plc.read_state())

# bOut1 = plc.read_by_name("GVL.bOUt1")
# print(f"Orginal State {bOut1}")
#
# plc.write_by_name("GVL.bOut1", True)
#
# bOut1 = plc.read_by_name("GVL.bOUt1")
# print(f"Final State {bOut1}")
#
# bOut2 = plc.read_by_name("GVL.bOUt2")
# print(bOut2)
plc.write_by_name("MAIN.bDummy", False)
print(plc.read_by_name("MAIN.bDummy"))
