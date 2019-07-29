from Older_Encrpyters.L5 import L5_Decoder, L5_Encoder

test_e = L5_Encoder.Encoder(1, [1, 1, 2], [1, 1, 2], [1, 1, 2])
test_e.enc()

test_d = L5_Decoder.Decoder(1, [1, 1, 2], [1, 1, 2], [1, 1, 2])
test_d.dec()
