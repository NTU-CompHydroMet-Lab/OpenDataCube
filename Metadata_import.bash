for m1 in {01..12}
do
   for d1 in {01..29}
      do
         echo datacube dataset add ./improve/2020/$m1/$d1/improve_2020-$m1-$d1.odc-metadata.yaml
         datacube dataset add ./improve/2020/$m1/$d1/improve_2020-$m1-$d1.odc-metadata.yaml
      done
done

for m2 in {01,03,04,05,06,07,08,09,10,11,12}
   do
      echo datacube dataset add ./improve/2020/$m2/30/improve_2020-$m2-30.odc-metadata.yaml
      datacube dataset add ./improve/2020/$m2/30/improve_2020-$m2-30.odc-metadata.yaml
   done

for m3 in {01,03,05,07,08,10,12}
   do
      echo datacube dataset add ./improve/2020/$m2/30/improve_2020-$m2-30.odc-metadata.yaml
      datacube dataset add ./improve/2020/$m3/31/improve_2020-$m3-31.odc-metadata.yaml
   done
