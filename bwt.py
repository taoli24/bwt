def bwt(input_data):
    output = [] if isinstance(input_data, list) else ""
    n = len(input_data)
    # rotations = np.zeros(n,n,dtype=np.int32)
    #
    # for x in range(n):
    #     rotations[x] = np.roll(input_data, x)
    rotations = [input_data[i:] + input_data[:i] for i in range(n)]
    rotations.sort()

    if isinstance(input_data, str):
        output += "".join(x[-1] for x in rotations)

    else:
        output = [x[-1] for x in rotations]
    return output


def bwt_seq(data):
    data = list(data)

    count = {}

    for i, v in enumerate(data):
        count[v] = count.get(v, 0) + 1
        data[i] = str(v) + f"_{count[v]}"
    return data


def bwt_decode_lf_mapping(bwt_encoding):
    first_column = sorted(bwt_encoding)

    eov = "$_1" if isinstance(bwt_encoding[-1], str) else "-1_1"

    lf_mapping = {}
    # code char sequence
    first_column_seq = bwt_seq(first_column)
    last_column_seq = bwt_seq(bwt_encoding)

    # create lf mapping
    for i, (first, last) in enumerate(zip(first_column_seq, last_column_seq)):
        lf_mapping[last] = (i, first)

    v = lf_mapping[eov]
    res = []

    while v[1] != eov:
        res.append(first_column[v[0]])
        v = lf_mapping[v[1]]

    if isinstance(bwt_encoding, str):
        res = "".join(res)
    return res