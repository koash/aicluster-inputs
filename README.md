# Input file maker for aicluster
aicluster-inputs is input file maker for practical examination of AI. 

Please see [aicluster](https://github.com/takaho/aicluster) by [Takaho A. Endo](https://github.com/takaho).

## Dependency
- [PyYAML](https://pypi.python.org/pypi/PyYAML) 3.11
- [pandas](http://pandas.pydata.org/) 0.16.2
- [openpyxl](http://packages.python.org/openpyxl/) 1.8.6

e.g.
```
pip install openpyxl==1.8.6
```

[Because](http://pandas.pydata.org/pandas-docs/stable/install.html#optional-dependencies
):
> penpyxl version 1.6.1 or higher, but lower than 2.0.0


## Usage
```
python replacer.py <method_name> [options]
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
  -y YAMLFILE, --yamlfile=YAMLFILE
                        input yaml file
```

## Running test
```
./test.sh 
```
