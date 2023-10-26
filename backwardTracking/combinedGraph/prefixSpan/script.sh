MIN_LEN=5
MAX_LEN=15

for FNAME in "hbwall3" "vgrall3";
do
    for SEQ_LEN in 1024 512 256;
    do
        for TOPK in 1000 500 200;
        do
            python frequentPattern.py \
            --fname $FNAME \
            --seq_len $SEQ_LEN \
            --topk $TOPK \
            --min_len $MIN_LEN \
            --max_len $MAX_LEN 
        done;
    done;
done;
