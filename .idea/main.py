from g11 import golomb
import sys

path = "test.txt"

g= golomb(path)

output_path = g.compress()
print("Compressed file path: " + output_path)

decom_path = g.decompress(output_path)
print("Decompressed file path: " + decom_path)