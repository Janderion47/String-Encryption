from L6_SuperQuadratic import L6_Encoder, L6_Decoder

test = L6_Encoder.Encoder([10, 20], [10, 20], [10, 20], 2)
test.enc()

test = L6_Decoder.Decoder([10, 20], [10, 20], [10, 20], 2)
test.dec()
