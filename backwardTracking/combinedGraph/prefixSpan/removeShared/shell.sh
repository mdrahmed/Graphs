MIN_LEN=5
MAX_LEN=15

FNAME="hbwall3 vgrall3"
SEQ_LEN="512"
TOPK="2000"

# "python3 find_and_remove.py --fnames hbwall3-vgrall3 --split_mode overlapping --seq_len 512 --topk 2000 --fname_to_remove hbwall3 --common_threshold 0.1"

for seq_len in $SEQ_LEN; do
    for topk in $TOPK; do
        python3 find_and_remove-v2.py \
            --fnames hbwall3-vgrall3 \
            --split_mode overlapping \
            --seq_len $seq_len \
            --topk $topk \
            --fname_to_remove hbwall3 \
            --common_threshold 0.1
            #--min_len $MIN_LEN \
            #--max_len $MAX_LEN
    done
done

