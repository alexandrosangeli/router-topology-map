#!/bin/bash

mkdir traceroute_out
mkdir traceroute_out/v4
mkdir traceroute_out/v6
 
# # # Iterate the command line arguments which are DNS names (e.g. www.example.com)
for val in "$@"; do
   OUT=$(echo $(./dnslookup $val))
   IFS=' ' read -r -a array <<< "$OUT"
   DOMAIN="${array[0]}"

   FAMILY1=${array[1]}
   FAMILY2=${array[4]}

   if [ "$FAMILY1" = "IPv4" ]; then
      V="${array[2]}"
      echo $(traceroute -4 -m 50 -q 1 -n $V > traceroute_out/v4/$V)
   elif [ "$FAMILY1" = "IPv6" ]; then
      V="${array[2]}"
      echo $(traceroute -6 -m 50 -q 1 -n $V > traceroute_out/v6/$V)
   fi


   if [ "$FAMILY2" = "IPv4" ]; then
      V="${array[5]}"
      echo $(traceroute -4 -m 50 -q 1 -n $V > traceroute_out/v4/$V)
   elif [ "$FAMILY2" = "IPv6" ]; then
      V="${array[5]}"
      echo $(traceroute -6 -m 50 -q 1 -n $V > traceroute_out/v6/$V)
   fi
   
done

mkdir traceroute_out/v4/formatted
mkdir traceroute_out/v6/formatted
python3 format.py


# combine all outputs to one file, then process the input to match the .dot format
touch all_ipv4.txt
for file in $(ls traceroute_out/v4/formatted/) ; do 
   cat "traceroute_out/v4/formatted/$file" >> all_ipv4.txt
done

echo "graph routertopology {" > router-topology-v4.dot
cat all_ipv4.txt | sort | uniq >> router-topology-v4.dot
echo "}" >> router-topology-v4.dot

# Do the same for ipv6
touch all_ipv6.txt
for file in $(ls traceroute_out/v6/formatted/) ; do 
   cat "traceroute_out/v6/formatted/$file" >> all_ipv6.txt
done

echo "graph routertopology {" > router-topology-v6.dot
cat all_ipv6.txt | sort | uniq >> router-topology-v6.dot
echo "}" >> router-topology-v6.dot

dot -T pdf -o router-topology-v4.pdf router-topology-v4.dot
dot -T pdf -o router-topology-v6.pdf router-topology-v6.dot

# cleanup
rm -rf all_ipv4.txt all_ipv6.txt traceroute_out router-topology-v4.dot router-topology-v6.dot
