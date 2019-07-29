from L6_SuperQuadratic import L6_Encoder, L6_Decoder

test = L6_Encoder.Encoder([10, 10, 20], [10, 10, 20], [10, 10, 20], 5)
test.enc()

test = L6_Decoder.Decoder([10, 10, 20], [10, 10, 20], [10, 10, 20], 5)
test.dec()
