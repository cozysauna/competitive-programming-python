#!/bin/zsh

# ./in/0000.txtのようにテストデータを保存する

#テストの数
N=5
#実行ファイル
excecute_file=main.py 

#ログファイル
logfile=".log"

#テスト実行中に書き換えが起こらないように、ファイルをコピーする
eval cp $excecute_file .test.py 

#ログファイルが存在する場合
if [ -e $logfile ];then
    eval cp /dev/null $logfile
#ログファイルが存在しない場合
else
    eval touch $logfile
fi

for ((i=0;i<N;i++))
do 
    file_number=$(printf "%04d\n" "${i}") 
    echo;
    echo TEST $i is working
    test_file_name=in/$file_number.txt
    eval python3 .test.py < $test_file_name
done

eval cat $logfile | awk 'BEGIN{OFMT="%.16f"; print "******* 結果 *******"}{total_score+=$1;print "TEST", NR, "SCORE", $1}END{print "AVERAGE", int(total_score / NR)}'
