# Source
region-specific

```sh
URL=https://raw.githubusercontent.com/adobe-fonts/source-han-sans/master
WEIGHT=Medium
WEIGHT_URL=${URL}/${WEIGHT}
wget ${URL}/FontMenuNameDB.SUBSET
wget ${URL}/UniSourceHanSansCN-UTF32-H
cd ${WEIGHT}
wget ${WEIGHT_URL}/cidfont.ps.CN
wget ${WEIGHT_URL}/features.CN
wget ${WEIGHT_URL}/cidfontinfo.CN

makeotf -f cidfont.ps.CN -ff features.CN -fi cidfontinfo.CN -mf ../FontMenuNameDB.SUBSET -r -nS -cs 25 -ch ../UniSourceHanSansCN-UTF32-H
cd -
```

language-specific

```sh
wget ${URL}/FontMenuNameDB
OTC=${WEIGHT}/OTC
OTC_URL=${URL}/${OTC}
cd ${OTC}
wget ${OTC_URL}/cidfont.ps.OTC.SC
wget ${OTC_URL}/features.OTC.SC
wget ${OTC_URL}/cidfontinfo.OTC.SC

makeotf -f cidfont.ps.OTC.SC -ff features.OTC.SC -fi cidfontinfo.OTC.SC -mf ../../FontMenuNameDB -r -nS -cs 25 -ch ../../UniSourceHanSansCN-UTF32-H
cd -
```

