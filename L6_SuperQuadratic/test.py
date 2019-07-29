from L6_SuperQuadratic import L6_Encoder, L6_Decoder

test = L6_Encoder.Encoder([1, 1, 2], [1, 1, 2], [1, 1, 2], 2)
test.enc()

test = L6_Decoder.Decoder([1, 1, 2], [1, 1, 2], [1, 1, 2], 2)
test.dec()
