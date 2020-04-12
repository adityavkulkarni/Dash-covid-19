progressbar() {
    local duration=${1}

    already_done() { for ((doneq=0; doneq<$elapsed; doneq++)); do printf "▇"; done }
    remaining() { for ((remain=$elapsed; remain<$duration; remain++)); do printf " "; done }
    percentage() { printf "| %s%%" $(($elapsed)); }
    clean_line() { printf "\r"; }

  for (( elapsed=1; elapsed<=$duration; elapsed++ )); do
      already_done; remaining; percentage
      sleep 1
      clean_line
  done
  clean_line
}


while true
do
	printf "\r"
 	echo "Starting Data Update"
	python3 getter.py
	echo "Data Update Complete"
	
	echo "Pushing to Heroku Server"
	git add .
	git commit -m "first commit"
	git push heroku master
	echo "Done"

	ssmtp kuladitya09@gmail.com < message.txt
	echo "Mail Sent" 
	sleep 5
	echo "Sleeping"
progressbar 60
	echo "1 minutes done since last update"
	progressbar  60
echo "2 minutes done since last update"
	progressbar  60
echo "3 minutes done since last update"
	progressbar  60
echo "4 minutes done since last update"
	progressbar  60
echo "5 minutes done since last update"
	progressbar  60
echo "6 minutes done since last update"
	progressbar  60
echo "7 minutes done since last update"
	progressbar  60
echo "8 minutes done since last update"
	progressbar  60
echo "9 minutes done since last update"
	progressbar  60
echo "10 minutes done since last update"
	progressbar  60
echo "11 minutes done since last update"
	progressbar  60
echo "12 minutes done since last update"
	progressbar  60
echo "13 minutes done since last update"
	progressbar  60
echo "14 minutes done since last update"
	progressbar  60
echo "15 minutes done since last update"
	progressbar  60
echo "16 minutes done since last update"
	progressbar  60
echo "17 minutes done since last update"
	progressbar  60
echo "18 minutes done since last update"
	progressbar  60
echo "19 minutes done since last update"
	progressbar  60
echo "20 minutes done since last update"
	progressbar  60
echo "21 minutes done since last update"
	progressbar  60
echo "22 minutes done since last update"
	progressbar  60
echo "23 minutes done since last update"
	progressbar  60
echo "24 minutes done since last update"
	progressbar  60
echo "25 minutes done since last update"
	progressbar  60
echo "26 minutes done since last update"
	progressbar  60
echo "27 minutes done since last update"
	progressbar  60
echo "28 minutes done since last update"
	progressbar  60
echo "29 minutes done since last update"
	progressbar  60
echo "30 minutes done since last update"
	progressbar  60
echo "31 minutes done since last update"
	progressbar  60
echo "32 minutes done since last update"
	progressbar  60
echo "33 minutes done since last update"
	progressbar  60
echo "34 minutes done since last update"
	progressbar  60
echo "35 minutes done since last update"
	progressbar  60
echo "36 minutes done since last update"
	progressbar  60
echo "37 minutes done since last update"
	progressbar  60
echo "38 minutes done since last update"
	progressbar  60
echo "39 minutes done since last update"
	progressbar  60
echo "40 minutes done since last update"
	progressbar  60
echo "41 minutes done since last update"
	progressbar  60
echo "42 minutes done since last update"
	progressbar  60
echo "43 minutes done since last update"
	progressbar  60
echo "44 minutes done since last update"	
	progressbar  60
echo "45 minutes done since last update"
	progressbar  60
	
clear
done
