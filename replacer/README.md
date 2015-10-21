# Input file maker for aicluster
aicluster-inputs is input file maker for practical examination of AI. 

Please see [aicluster](https://github.com/takaho/aicluster) of takaho.

## Dependency
- [pandas](http://pandas.pydata.org/)
- [openpyxl](http://packages.python.org/openpyxl/)

e.g.
```
pip install openpyxl==1.8.6
```

[Because](http://pandas.pydata.org/pandas-docs/stable/install.html#optional-dependencies
):
> penpyxl version 1.6.1 or higher, but lower than 2.0.0


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
  -e ENCODING, --encoding=ENCODING
                        encoding
```

## Running test
```
./test.sh 
```