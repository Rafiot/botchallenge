mvn install
cd proto
./gen_python.sh
cd ../client
python3 setup.py build
python3 setup.py install

cd "/Users/jhaip/Desktop/Spigot Server/plugins"
PREV_PLUGIN=$(ls *.jar)
mv -f $PREV_PLUGIN "/Users/jhaip/Desktop/Spigot Server/plugins/old"

cd "/Users/jhaip/Code/botchallenge/target"
LATESTFILE=$(ls -t1 | head -n1)
cp -f $LATESTFILE "/Users/jhaip/Desktop/Spigot Server/plugins"
