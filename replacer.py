import sys
import pandas as pd
import yaml
from datetime import datetime
from glob import glob
from optparse import Option, OptionParser
from os.path import join, relpath

class Replacer(object):
    def import_yaml(self, yamlfile):
        with open(yamlfile) as fr:
            return yaml.load(fr)

    def add_timestamp(self, timestamp, iyaml):
        ts = ""
        if timestamp or iyaml["timestamp"]:
            dt = datetime.now().strftime("%Y%m%d%H%M%S")
            ts = "_" + dt
        return ts

    def replace(self, inputdir, outputdir, group, timestamp, encoding, yamlfile):
        iyaml = self.import_yaml(yamlfile)

        ts = self.add_timestamp(timestamp, iyaml)
        outputfile = "data{0}.xlsx".format(ts)

        writer = pd.ExcelWriter(join(outputdir, outputfile))
        files = [relpath(x, inputdir) for x in glob(join(inputdir, '*'))]

        for i, f in enumerate(files):
            dfcsv = pd.read_csv(join(inputdir, f), encoding=encoding, header=None)
            dfcsv_r = dfcsv.T.dropna(subset=[1])

            d1 = dfcsv_r.ix[:, :1]  # ID, Date
            d2 = dfcsv_r.ix[:, 7:]  # Values
            dm = pd.concat([d1, d2], axis=1)

            dm.ix[:,0] = dfcsv_r.ix[1, 0]   # ID
            dm.ix[0,1] = 'Date'

            dm.columns = dm.as_matrix()[0]

            dm.insert(1, '{0}'.format(group), '')
            dm.ix[0,1] = group

            dd = dm.ix[1:, :]
            latest = dd[dd['Date'] == dd['Date'].max()]
            latest = latest.mask(latest.isin(iyaml["fillna"])).fillna(-1)

            if i == 0:
                dm.ix[0,0] = 'ID'
                header = dm.head(1)
                header.to_excel(writer, index=False, header=False)

            latest.to_excel(writer, index=False, header=False, startrow=i+1)

        writer.save()

    def run_method(self, method_name, options):
        if method_name == "replace":
            self.replace(inputdir=options.inputdir,
                         outputdir=options.outputdir,
                         group=options.group,
                         timestamp=options.timestamp,
                         encoding=options.encoding,
                         yamlfile=options.yamlfile)
        else:
            print("{0} - Not found method".format(method_name))

class MultipleOption(Option):
    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            values.ensure_value(dest, []).append(value)
        else:
            Option.take_action(self, action, dest, opt, value, values, parser)

def main():
    parser = OptionParser(usage="usage: $ python csv2excel.py <method_name> [options]", option_class=MultipleOption)
    parser.add_option("-i", "--inputdir", default="input", help="input directory")
    parser.add_option("-o", "--outputdir", default="output", help="output directory")
    parser.add_option("-g", "--group", default="OUT", help="group column")
    parser.add_option("-t", "--timestamp", default=False, help="add timestamp to the output file name")
    parser.add_option("-e", "--encoding", default="latin_1", help="encoding")
    parser.add_option("-y", "--yamlfile", default="settings.yml", help="input yaml file")

    (options, method_name) = parser.parse_args()

    if len(method_name) != 1:
        parser.print_help()
        sys.exit()

    r = Replacer()
    r.run_method(method_name[0], options)

if __name__ == "__main__":
    main()