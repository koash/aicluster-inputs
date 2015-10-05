import sys
import pandas as pd
from datetime import datetime
from glob import glob
from optparse import Option, OptionParser
from os.path import join, relpath

class Csv2Excel(object):
    def replace(self, inputdir, outputdir, group, timestamp):

        ts = ""
        if timestamp:
            dt = datetime.now().strftime("%Y%m%d%H%M%S")
            ts = "_" + dt

        outputfile = "data{0}.xlsx".format(ts)

        writer = pd.ExcelWriter(join(outputdir, outputfile))
        files = [relpath(x, inputdir) for x in glob(join(inputdir, '*'))]

        for i, f in enumerate(files):
            dfcsv = pd.read_csv(join(inputdir, f), header=None)
            dfcsv_r = dfcsv.T.dropna()

            d1 = dfcsv_r.ix[:1, :1]
            d2 = dfcsv_r.ix[:1, 5:]
            dm = pd.concat([d1, d2], axis=1)

            dm.insert(1, '{0}'.format(group), '')

            dm.columns = dm.as_matrix()[0]

            dm.ix[:,0] = dm.ix[1,0]
            dm.ix[0,0] = 'ID'
            dm.ix[0,1] = group

            if i == 0:
                header = dm.head(1)
                header.to_excel(writer, index=False, header=False)
            
            result = dm.ix[1:, :]
            result.to_excel(writer, index=False, header=False, startrow=i+1)

        writer.save()

    def run_method(self, method_name, options):
        if method_name == "replace":
            self.replace(inputdir=options.inputdir,
                         outputdir=options.outputdir,
                         group=options.group,
                         timestamp=options.timestamp)
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

    (options, method_name) = parser.parse_args()

    if len(method_name) != 1:
        parser.print_help()
        sys.exit()

    ce = Csv2Excel()
    ce.run_method(method_name[0], options)

if __name__ == "__main__":
    main()