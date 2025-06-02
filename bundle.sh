#!/bin/sh
TO_BUNDLE="BurningChr0me.py unbundle.sh run.sh"
PYCRYPTODOME_REPO="https://github.com/Legrandin/pycryptodome.git"
PYCRYPTODOME_BRANCH="v3.17.0" # python 3.6 support
CURRENT_DIR=$(cd $(dirname $0); pwd)
WORKDIR=$(mktemp -d)
echo "Working in $WORKDIR"
BASENAME=bchrome
OUTDIR=$WORKDIR/$BASENAME
OUTFILE=/tmp/$BASENAME.tar.gz
mkdir $OUTDIR

for file in $TO_BUNDLE; do
    echo "Bundling $file"
    cp $CURRENT_DIR/$file $OUTDIR
done

cd $WORKDIR
git clone --depth=1 $PYCRYPTODOME_REPO -b $PYCRYPTODOME_BRANCH
tar -zcvf $OUTDIR/pycryptodome.tar.gz pycryptodome
tar -zcvf $OUTFILE $(basename $OUTDIR)

echo "Bundled to $OUTFILE"
