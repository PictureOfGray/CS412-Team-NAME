for i in $(seq 3 50); do
  python3 ../cs412_tsp_exact.py test < ./${i}.txt
done

