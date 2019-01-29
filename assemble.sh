# Download and assemble database

for i in $(seq -f "%02g" 0 16); do
wget "https://github.com/dgerosa/spops/releases/download/v0.2/spops.h5_"$i;
done
cat spops.h5_* > spops.h5
rm spops.h5_*
