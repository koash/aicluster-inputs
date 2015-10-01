# aicluster
This is input file maker for practical examination of AI. 

Please see [aicluster](https://github.com/takaho/aicluster) of takaho.

## Dependencies
- [pandas](http://pandas.pydata.org/)

## Usage
```
python csv2excel.py <method_name> [options]
```

### Options
```
  -h, --help            show this help message and exit
  -i INPUTDIR, --inputdir=INPUTDIR
                        input directory
  -o OUTPUTDIR, --outputdir=OUTPUTDIR
                        output directory
  -g GROUP, --group=GROUP
                        group column
  -t TIMESTAMP, --timestamp=TIMESTAMP
                        add timestamp to the output file name
```

## Running test
```
./test.sh 
```
